import plotly.express as px
import pandas as pd
import panel as pn
import param as pm

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pn.extension('plotly')

'''
The order of executing the files to get clustering_vectorized_praise.csv file is as follow:
1. clustering_praise.ipynb
2. vectorizing_praise.ipynb
3. clustering_vectorized_praise.ipynb
'''
df = pd.read_csv("clustering_vectorized_praise.csv", index_col=0)
data = df.copy()

class PraiseClustering(pm.Parameterized):
    
    

    x_col = pm.ObjectSelector(label='X axis', default="Avg %", objects=["Avg %", "IH per Praise", "IH per person", 'day_of_week'])
    y_col = pm.ObjectSelector(label='Y axis', default='IH per Praise', objects=["Avg %", "IH per Praise", "IH per person", 'day_of_week'])
    col_color = pm.ObjectSelector(label='Color', default='Kmean tag', objects=['Kmean tag', 'day_of_week','tag','New Kmean str tag'])
       
    def __init__(self, data, **params):
        super().__init__(**params)
        self.data = data
    
    def final_data_(self):
        data_ = self.data
        return data_
    
    @pm.depends('x_col', 'y_col', 'col_color') 
    def plot_kmean(self):
        data_ = self.final_data_()
        praise_plot_df = data_.sort_values(by=[self.col_color], ascending=True)
        return px.scatter(praise_plot_df, x=self.x_col, y=self.y_col, render_mode='webgl', color=self.col_color)

    
    def plot_box(self):
        data_ = self.final_data_()
        return px.box(data_, x='Avg %', y='day_of_week', points='all')
    
    
    @pm.depends('x_col', 'y_col') 
    def show_corr(self):
        return pn.widgets.DataFrame(df[[self.x_col, self.y_col]].corr(), name='DataFrame')
 
        
        
    def show_data(self):
        return pn.widgets.DataFrame(self.final_data_(), name='DataFrame', height=400)
    
    
pc = PraiseClustering(data, name='Kmean Clustering of Praise data')


vanilla = pn.template.VanillaTemplate(
    logo='https://static.tildacdn.com/tild6265-6232-4633-b761-383632303436/Group_2.png',
    favicon='https://static.tildacdn.com/tild6334-3163-4633-a335-333337386131/favicon_final.ico',
    site="The Commons Stack",
    title="Praise Analysis",
    header_background="#514d4e",
    header_color="#ff861c",)

pn.config.sizing_mode = 'stretch_width'

vanilla.sidebar.append(
    pn.Column(
        pc.param, 
        pn.pane.Markdown('''
        #### __Correlation between two columns__
        '''),
        pc.show_corr,
        pn.pane.Markdown('''
        #### Description:
        * __Kmean tag__ is based on _'Avg %'_ & _'IH per Praise'_ columns
        * __New Kmean str tag__ is based on _'To'_, _'From'_, _'Reason for dishing'_, _'Server'_ & _'Room'_ columns
        * __tag__ is based on 17 TEC tags
        '''),
        pn.pane.Markdown('''
        <h4><strong>Developed by:&nbsp;<a title="Mohammad" href="https://github.com/spacelover92" target="_blank" 
        rel="noopener">@maghaali#6154</a>&nbsp;at <a title="Longtail Financial" href="https://longtailfinancial.com/" target="_blank" 
        rel="noopener">LTF<img style="vertical-align: middle;" src="https://longtailfinancial.com/wp-content/uploads/2020/03/Longtail-
        Logo-white-center.png" alt="Longtail Financial" width="20" height="20" /></a></strong></h4>
        ''')))

tab_u = pn.Tabs(("Scatter plot", pc.plot_kmean), height=420)
tab_d = pn.Tabs(('Box plot', pc.plot_box))

tab_d.extend([('Show data', pc.show_data)])

vanilla.main.append(pn.Column(tab_u, pn.pane.Markdown(''' *** '''), tab_d))
vanilla.servable()
