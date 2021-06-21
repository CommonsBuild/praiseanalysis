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
df.columns = ['To', 'From', 'Reason for dishing', 'Server', 'Room', 'v1 norm', 'v2 norm', 'v3 norm', 'Avg %',
              'IH per Praise', 'IH per person', 'Day of Week', 'TEC Tags', 'Kmean Tag', 'Kmean Tag2_', 'Kmean Tag2']
data = df.copy()

class PraiseClustering(pm.Parameterized):
    
    

    x_col = pm.ObjectSelector(label='X axis', default="Avg %", objects=["Avg %", "IH per Praise", "IH per person", 'Day of Week'])
    y_col = pm.ObjectSelector(label='Y axis', default='IH per Praise', objects=["Avg %", "IH per Praise", "IH per person", 'Day of Week'])
    col_color = pm.ObjectSelector(label='Color', default='Kmean Tag', objects=['Kmean Tag', 'Day of Week','TEC Tags','Kmean Tag2'])
    query_col = pm.ObjectSelector(label='Query Column', default='Kmean Tag', objects=['To', 'From', 'Room', 'v1 norm',
                                                                                      'v2 norm', 'v3 norm', 'Avg %', 'IH per Praise',
                                                                                      'IH per person', 'Day of Week', 'TEC Tags', 'Kmean Tag',
                                                                                      'Kmean Tag2'])
    query_str = pm.String(label='Query String', default="== All", doc="A string")
    
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


    @pm.depends('col_color') 
    def plot_box(self):
        data_ = self.final_data_()
        return px.box(data_, x='Avg %', y='Day of Week', points='all', hover_data=[self.col_color])
    
    
    @pm.depends('x_col', 'y_col') 
    def show_corr(self):
        return pn.widgets.DataFrame(df[[self.x_col, self.y_col]].corr(), name='DataFrame')
 
    def query_data(self, data, col_name, query_str):
        df = data
        col_loc = df.columns.get_loc(f'{col_name}')
        try:
            symbol_, query_ = query_str.split(" ")
        except:
            symbol_, query1_, query2_ = query_str.split(" ")
            query_ = query1_+" "+ query2_
        if query_str=='== All':
            return df
        elif col_loc in [0, 1, 4, 11, 12]:
            query = df[df[f"{col_name}"] == query_]
            if query.shape[0] != 0:
                return query
            else:
                return None
        elif col_loc in [13, 15]:
            query = df[df[f"{col_name}"] == query_]
            if query.shape[0] != 0:
                return query
            else:
                return None
        elif col_loc in [5, 6, 7, 8, 9, 10, 14]:
            query = df.query(f'`{col_name}`'+symbol_+query_)
            if query.shape[0] != 0:
                return query
            else:
                return None
        else:
            return None

        
    @pm.depends('query_col', 'query_str')
    def show_data(self):
        data_ = self.data
        query_result = self.query_data(data=data_, col_name=self.query_col, query_str=self.query_str)
        return pn.widgets.DataFrame(query_result, name='DataFrame', height=400)
    
    
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
        pc.param.x_col,
        pc.param.y_col,
        pc.param.col_color,
        pn.pane.Markdown('''
        #### __Correlation between two columns__
        '''),
        pc.show_corr,
        pn.pane.Markdown('''
        #### Description:
        * __Kmean Tag__ is based on _'Avg %'_ & _'IH per Praise'_ columns
        * __Kmean Tag2__ is based on _'To'_, _'From'_, _'Reason for dishing'_, _'Server'_ & _'Room'_ columns
        * __TEC Tag__ is based on 17 TEC tags
        * __Min Max Scaler__ is used to transform numeric data by scaling each feature to (0, 1) range to be suitable for use in machine learning algorithm
        '''),
        pn.pane.Markdown('''
        <h4><strong>Developed by&nbsp;<a title="Mohammad" href="https://github.com/spacelover92" target="_blank" 
        rel="noopener">@maghaali#6154</a>&nbsp;at <a title="Longtail Financial" href="https://longtailfinancial.com/" target="_blank" 
        rel="noopener">LTF<img style="vertical-align: middle;" src="https://longtailfinancial.com/wp-content/uploads/2020/03/Longtail-
        Logo-white-center.png" alt="Longtail Financial" width="20" height="20" /></a></strong></h4>
        ''')))

tab_u = pn.Tabs(("Scatter plot", pc.plot_kmean))
tab_d = pn.Tabs(('Box plot', pc.plot_box))
        
tab_d.extend([('Show data', pn.Column(pn.Row(pc.param.query_col, pc.param.query_str,"","", ""),pc.show_data))])

vanilla.main.append(pn.Column(tab_u, pn.pane.Markdown(''' *** '''), tab_d))
vanilla.servable()
