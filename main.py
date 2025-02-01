import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import Gui, navigate, Icon
import numpy as np
import plotly as plt

data=pd.read_csv('mobile_phone_data.csv')
data_copy=data.copy()

scatter_chart=data.groupby(['Brand','Battery Capacity (mAh)'])['Weight (grams)'].mean().reset_index()

scatter_chart2=data.groupby(['Brand','Battery Capacity (mAh)'])['Price in(USD)'].mean().reset_index()

brand = list(data["Brand"].unique())
selected_brand = "Apple"


def apply_change(state):
    state.data_copy = state.data[state.data["Brand"] == state.selected_brand]
    state.scatter_chart=(state.data_copy.groupby(['Brand','Battery Capacity (mAh)'])['Weight (grams)']
                         .mean()
                         .reset_index())
    state.scatter_chart2=(state.data_copy.groupby(['Brand','Battery Capacity (mAh)'])['Price in(USD)']
                         .mean()
                         .reset_index())
    
pie_chart1={'category_s':['Communication','Consumer Electronics','Semiconductors','Display Panels'],'revenue_s':[86,42,50,26]}
pie_chart2={'category_a':['iPad','Mac','iPhone','iPod','Services','Accessories'],'revenue_a':[19.24,23.47,102.40,3.33,27.31,13.06]}
pie_chart3={'category_m':['Products and Systems Integration','Software and Services'],"revenue_m":[2.85, 17.36]}


with tgb.Page() as Home:
    with tgb.part(class_name="body"):
        tgb.text('# The Tech Titans: Samsung vs. Apple vs. Motorola',mode='md')
        with tgb.layout(columns='2 3 '):
            with tgb.part():
                tgb.selector(value = "{selected_brand}",
                    lov=brand , 
                    dropdown=True,
                    width="50%"
                
                    )
                tgb.button('Apply',
                          on_action=apply_change
                )
            with tgb.part():
                tgb.navbar(
                    width="100%"
                )
        tgb.html('br')

        with tgb.layout(columns='1 1'):
                with tgb.part(class_name='card'):
                    tgb.chart ('{scatter_chart}',
                           title='Relation Between Battery capacity and weight',
                           mode="markers",
                           y = 'Battery Capacity (mAh)',
                           x = 'Weight (grams)'
                           )
                with tgb.part(class_name='card'):
                    tgb.chart ('{scatter_chart2}',
                           title='Relation Between Battery capacity and Price',
                           mode="markers",
                           y = 'Battery Capacity (mAh)',
                           x = 'Price in(USD)',
                           
                )
                
                      


        tgb.html('br')
        with tgb.layout(columns='1 1'):
                with tgb.part(class_name='card'):
                 tgb.chart ('{pie_chart1}',
                           title='Samsung Revenue by Segments',
                           type='pie',
                           labels='category_s',
                           values="revenue_s"
                )
                with tgb.part(class_name='card'):
                    tgb.chart ('{pie_chart2}',
                           title='Apple Revenue by Segments',
                           type='pie',
                           labels='category_a',
                           values="revenue_a"
                )
                    tgb.html('br')

        with tgb.layout(columns='1 1 1'):
            with tgb.part():
                tgb.text('')

            with tgb.part(class_name='card'):
                tgb.chart ('{pie_chart3}',
                           title='Motorola Revenue by Segments',
                           type='pie',
                           labels='category_m',
                           values="revenue_m",
                           width='100%')
                
            with tgb.part():
                tgb.text('')
                

revenue= pd.read_csv('Revenue.csv')
revenue_copy=revenue.copy()

Company = list(revenue["Company"].unique())
selected_company = "Samsung"

bar_chart=revenue.groupby('Year')['Revenue(in Billion)'].mean().reset_index()

def apply_change_revenue(state):
    state.revenue_copy = state.revenue[state.revenue["Company"] == state.selected_company]

    state.bar_chart = (state.revenue_copy.groupby('Year')['Revenue(in Billion)']
                       .mean()
                       .reset_index())



with tgb.Page() as Page2:
    with tgb.part(class_name="body"):
        tgb.text('# The Tech Titans: Samsung vs. Apple vs. Motorola',mode='md')
        with tgb.layout(columns='2 3 '):
            with tgb.part():
                tgb.text(" ")
            with tgb.part(): 
                tgb.navbar()
            tgb.html('br')
        with tgb.layout(columns='1 3'):
            with tgb.part():
                tgb.selector(value = "{selected_company}",
                    lov=Company , 
                    dropdown=True,
                     )
            with tgb.part():
                tgb.button('Apply',
                           on_action=apply_change_revenue)
                
        tgb.html('br')   
                
        with tgb.layout(columns='1'):
            with tgb.part(class_name='card'):
                tgb.chart ('{bar_chart}',
                           title= 'Yearly Revenue',
                           type='bar',
                           x='Year',
                           y='Revenue(in Billion)'
                           
                                                     
                           ) 
                
with tgb.Page() as Page3:
    with tgb.part(class_name="body"):
        tgb.text('# The Tech Titans: Samsung vs. Apple vs. Motorola',mode='md')
        with tgb.layout(columns='2 3 '):
            with tgb.part():
                tgb.text(" ")
            with tgb.part(): 
                tgb.navbar()
            tgb.html('br')
            
        with tgb.part():
            tgb.text('## Overview page Reference', mode='md')
            tgb.table("{data}")
            tgb.html('br')

        with tgb.part():
            tgb.text('## Comparison page Reference', mode='md')
            tgb.table("{revenue}")
            
        
    

pages = {"Overview" : Home,
         "Comparison" : Page2,
          "Data" : Page3 }

app = Gui(pages=pages)


app.run(use_reloader=False,
        title='Mobile Brand Comparison',
        port='auto',
        watermark='Designed by Shreya'
        )
