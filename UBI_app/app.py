from scipy.stats.mstats import gmean
import scipy.stats as ss
import holoviews as hv
import pandas as pd
import numpy as np
import param as pm
import panel as pn
import hvplot.pandas
import warnings
warnings.filterwarnings('ignore')

#%%
# Importing data
data = pd.read_csv("praise_distributions.csv")


#%%
class DistributionInterventions(pm.Parameterized):
    top_percent_hatchers = pm.Number(0.5, bounds=(0,1), step=0.01)
    ubi = pm.Number(5, bounds=(0, 100), step=1)
    pareto_beta = pm.Number(0.4, bounds=(0,1), step=0.01, precedence=-1)
    apply_constant_ubi = pm.Boolean(True)
    
    def __init__(self, data, **params):
        super(DistributionInterventions, self).__init__(**params)
        self.original_data = data
        self.data = data.copy()
        self.add_ubi()
        
        
    @pm.depends('ubi', 'apply_constant_ubi', watch=True)    
    def add_ubi(self):
        if self.apply_constant_ubi:
            self.data['Impact Hours'] = self.original_data['Impact Hours'] + self.ubi
        else:
            self.data['Impact Hours'] = self.original_data['Impact Hours']

        
    def filtered_data(self):
        data = self.data.iloc[:round(len(self.data)*self.top_percent_hatchers)]
        data['% of distribution'] = data['Impact Hours'] / data['Impact Hours'].sum()
        return data
        
    def total_impact_hours(self):
        return pn.Column(
            pn.Row(pn.Column(
                "Filtered Impact Hours:", 
                round(self.filtered_data()['Impact Hours'].sum(), 2),
                ), pn.Column(
                "Percent of total Impact Hours:", 
                round(self.filtered_data()['Impact Hours'].sum() / self.data['Impact Hours'].sum(), 2),
                )),
            "Summary:",
            self.filtered_data()['Impact Hours'].describe(),
        )

    def percent_line(self):
        return hv.VLine(len(self.data)*self.top_percent_hatchers, color='red').opts(hv.opts.VLine(color='red'))

    def distribution(self):
        return (self.augmented_data().hvplot.area(y='Impact Hours', title='Impact Hours Distribution', height=320) * self.data.hvplot.line(y='Impact Hours', title='Impact Hours Distribution') * self.percent_line()).opts(shared_axes=False)

    def cum_dist(self, val): #cumulative distribution function
        prob_lt_val = (self.augmented_data()['Impact Hours'] < val).mean() # you can get proportions by taking average of boolean values
        return prob_lt_val
    
    def filtered_pareto(self):
        pct_values = np.arange(self.filtered_data()['Impact Hours'].min(),self.augmented_data()['Impact Hours'].max())
        cum_dist_values = [self.cum_dist(p) for p in pct_values]

        pareto_rv = ss.pareto(self.pareto_beta)
        pareto = [pareto_rv.cdf(p) for p in range(len(pct_values))]

        distributions = pd.DataFrame(zip(cum_dist_values, pareto), columns=['IH Cumulative Distribution', f'Pareto Distribution beta={self.pareto_beta}'])
        
        return distributions.hvplot.line().opts(hv.opts.VLine(color='red')).opts(shared_axes=False)
    
    def augmented_data(self):
        return self.filtered_data()
    
    def resources_percentage(self, p):
        data = self.augmented_data()
        relevant_percentile = np.percentile(data['Impact Hours'],p)
        is_gt_relevant_percentile = data['Impact Hours'] > relevant_percentile
        filtered_data = data[is_gt_relevant_percentile]
        filtered_hours = filtered_data['Impact Hours']
        pct_hours = filtered_hours.sum()/data['Impact Hours'].sum()
        return pct_hours

    def view_resources_percentage(self):
        message = ""
        for p in [50,80,90,95,99]:
            message += "The top {} percent of the population\n".format(100-p)
            message += "received {:0.2f} percent of the Impact Hours \n \n".format(self.resources_percentage(p))
            
        return pn.Pane(message)
    
    def gini_coefficient(self):
        x = self.augmented_data()['Impact Hours'].values
        n = len(x)
        x_bar = np.mean(x)
        abs_diffs = np.array([np.sum(np.abs(x[i] - x)) for i in range(n)])
        sum_abs_diffs = np.sum(abs_diffs)
        denominator = 2*n*n*x_bar
        return sum_abs_diffs/denominator
    
    def view_data(self):
        return self.augmented_data().head(10)
    



#%%

class GaussianIntervention(DistributionInterventions):
    gubi_spread = pm.Number(0.03, bounds=(0,0.05), step=0.01, doc="Standard Deviation")
    apply_constant_ubi = pm.Boolean(True)
    apply_gaussian_ubi = pm.Boolean(True)
    ubi = pm.Number(5, bounds=(0, 100), step=1)
    gubi = pm.Number(15, bounds=(0, 100), step=1)
    
    def gaussian_function(self, x):
        mean = len(self.data[self.data['Impact Hours'] > gmean(self.filtered_data()['Impact Hours'])])
        return self.gubi * np.exp(-((x - mean)**2) / 2*self.gubi_spread**2)
    
    def intervention(self):
        xs = np.linspace(0, len(self.filtered_data()), len(self.filtered_data()))
        ys = self.gaussian_function(xs)
        return pd.DataFrame(zip(xs,ys), columns=['x','y'])
    
    def view_intervention(self):
        intervention = self.intervention()
        return intervention.hvplot.line(x='x',y='y', title='Gaussian Intervention', height=320).opts(labelled=[])
    
    def augmented_data(self):
        data = self.filtered_data()
        if self.apply_gaussian_ubi:
            data = pd.DataFrame(data['Impact Hours'] + self.intervention()['y'], columns=['Impact Hours'])
        else:
            data = pd.DataFrame(data['Impact Hours'], columns=['Impact Hours'])
        data['% of distribution'] = data['Impact Hours'] / data['Impact Hours'].sum()
        return data
    
    def ubi_info(self):
        if self.apply_gaussian_ubi:
            gubi = round(self.intervention()['y'].sum(),0)
        else:
            gubi = 0
            
        if self.apply_constant_ubi:
            ubi = round(len(self.filtered_data())*self.ubi,0)
        else:
            ubi = 0
        return pd.DataFrame({
            'Gaussian UBI Hours': gubi,
            'Constant UBI Hours': ubi,
            'Total': ubi+gubi,
        },index=['value'])
        
        
#%%
gaus = GaussianIntervention(data)
merged_data = pd.read_csv('wage_deductions.csv').sort_values('Total Impact', ascending=False)
merged_data = gaus.data.join(merged_data[['Deducted Impact Hours']], how='left')
#%%
class InterventionDashboard(GaussianIntervention):
    apply_wage_intervention = pm.Boolean(False)
    wage_deductions = pm.Number(0.85, bounds=(0, 0.85), step=0.01)
    
    def __init__(self, data, **params):
        self.original_data = data
        self.original_wage_data = data
        super(InterventionDashboard, self).__init__(data, **params)
        self.data = data.copy()
        self.add_ubi()
        self.original_impact_hours_deducted = abs(self.original_data['Deducted Impact Hours'].sum())
        self.total_impact_hours_deducted = self.original_impact_hours_deducted
    
    @pm.depends('wage_deductions', 'apply_wage_intervention', watch=True)    
    def wage_data(self):
        if self.apply_wage_intervention:
            wage_data = self.original_data.copy()
            deductions = wage_data['Deducted Impact Hours']*(0.85-self.wage_deductions)
            wage_data['Impact Hours'] = wage_data['Impact Hours'] - deductions
            self.total_impact_hours_deducted = self.original_impact_hours_deducted - abs(deductions.sum())
            self.original_wage_data = wage_data[['Handle', 'Impact Hours']]
            self.add_ubi()
        else:
            self.original_wage_data = self.original_data
            self.add_ubi()
        
    @pm.depends('ubi', 'apply_constant_ubi', watch=True)    
    def add_ubi(self):
        if self.apply_constant_ubi:
            self.data['Impact Hours'] = self.original_wage_data['Impact Hours'] + self.ubi
        else:
            self.data['Impact Hours'] = self.original_wage_data['Impact Hours']
            
    def wage_info(self):
        return pd.DataFrame({
            'Total Impact Hours Deducted From Wages': self.total_impact_hours_deducted,
            'Estimated Value': f"${round(self.total_impact_hours_deducted * 50, 2)}"
        }, index=['IH'])

#%%
dashboard = InterventionDashboard(merged_data)   
# dins = DistributionInterventions(data)
gini_coef = dashboard.gini_coefficient()
#%%
vanilla = pn.template.VanillaTemplate(
    logo='https://static.tildacdn.com/tild6265-6232-4633-b761-383632303436/Group_2.png',
    favicon='https://static.tildacdn.com/tild6334-3163-4633-a335-333337386131/favicon_final.ico',
    site="The Commons Stack",
    title="Praise Analysis",
    header_background="#514d4e",
    header_color="#ff861c",)

pn.config.sizing_mode = 'stretch_width'

vanilla.sidebar.append(pn.Column(dashboard,
                                pn.pane.Markdown(''' *** \n<p style="text-align: center;"><strong>Developed by <a title="Shawn Anderson" href="https://github.com/LinuxIsCool" target="_blank" rel="noopener">ygg_anderson</a> &amp;<br />deployed by <a title="Mohammad" href="https://github.com/spacelover92" target="_blank" rel="noopener">maghaali</a><br /></strong><strong>at <a title="Longtail Financial (github)" href="https://github.com/longtailfinancial" target="_blank" rel="noopener">Longtail Financial</a>&nbsp;<a title="Longtail Financial" href="https://longtailfinancial.com/" target="_blank" rel="noopener"><img style="vertical-align: middle;" src="https://longtailfinancial.com/wp-content/uploads/2020/03/Longtail-Logo-white-center.png" alt="Longtail Financial" width="20" height="20" /></a></strong></p> ''')))


vanilla.main.append(pn.Row(pn.Column(dashboard.distribution,
                                     dashboard.view_intervention ),
                           pn.Column(dashboard.view_data,
                                     pn.pane.Markdown(''' *** '''),
                                     dashboard.ubi_info,
                                     f"GINI Coefficient of filtered data: {gini_coef}",
                                     dashboard.wage_info,
                                     sizing_mode='stretch_height',
                                     max_width=300)))

vanilla.servable()
