
# Importing Libraries
import pandas as pd
import taipy.gui.builder as tgb
from taipy.gui import Gui, navigate, Icon
import numpy as np
import plotly as plt

#Read CSV file

data=pd.read_csv('mobile_phone_data.csv')
segment_revenue=pd.read_csv('brand_segment_revenue.csv')

#merging csv file
merged=pd.merge(segment_revenue,data,on='Brand',how='outer')
merged_copy=merged.copy()

#Filter the data according to charts
scatter_chart=merged.groupby(['Brand','Battery Capacity (mAh)'])['Weight (grams)'].mean().reset_index()

scatter_chart2=merged.groupby(['Brand','Battery Capacity (mAh)'])['Price in(USD)'].mean().reset_index()

pie_chart=merged.groupby(['Brand','Segment'])['Revenue (Billion USD)'].mean().reset_index()

#get unique values for selector
brand = list(merged["Brand"].unique())

selected_brand = "Apple"

layout = {"title": "Revenue by Segments"}

#Function to filter data based on selected companies
def apply_change(state):
    state.merged_copy = state.merged[state.merged["Brand"] == state.selected_brand]
          
    state.scatter_chart=(state.merged_copy.groupby(['Brand','Battery Capacity (mAh)'])['Weight (grams)']
                         .mean()
                         .reset_index())
    state.scatter_chart2=(state.merged_copy.groupby(['Brand','Battery Capacity (mAh)'])['Price in(USD)']
                         .mean()
                         .reset_index())
    state.pie_chart=(state.merged_copy.groupby(['Brand','Segment'])['Revenue (Billion USD)']
                     .mean()
                     .reset_index())
    state.layout= {"title":f"Revenue by Segments of {state.selected_brand}"}


# Create the Taipy page
with tgb.Page() as Home:
    with tgb.part(class_name="body"):
        tgb.text('# The Tech Titans: Samsung vs. Apple vs. Motorola',mode='md')
        with tgb.layout(columns='2 3 '):
            with tgb.part():
                #selector for companies
                tgb.selector(value = "{selected_brand}",
                    lov=brand , 
                    dropdown=True,
                    width="50%"
                    )
                #Button with trigger apply_change 
                tgb.button('Apply',
                          on_action=apply_change #Trigger update on button is clicked
                          )
            with tgb.part():
                #Vavigation Bar
                tgb.navbar(
                    width="100%"
                    )
        tgb.html('br')
        # Chart display
        with tgb.layout(columns='1 1'):
                with tgb.part(class_name='card'):
                    #Scatter plot to shoe relation between battery capacity and weight
                    tgb.chart ('{scatter_chart}',
                           title='Relation Between Battery capacity and weight',
                           mode="markers",
                           y = 'Battery Capacity (mAh)',
                           x = 'Weight (grams)'
                           )
                with tgb.part(class_name='card'):
                    #Scatter plot to shoe relation between battery capacity and Price
                    tgb.chart ('{scatter_chart2}',
                           title='Relation Between Battery capacity and Price',
                           mode="markers",
                           y = 'Battery Capacity (mAh)',
                           x = 'Price in(USD)'
                           )
                                    
        tgb.html('br')
        with tgb.layout(columns='1 2 1'):
                with tgb.part():
                    tgb.text(' ')
                with tgb.part(class_name='card'):
                 #Segmentwise revenue of comapany
                 tgb.chart ('{pie_chart}',
                           layout = "{layout}",
                           type='pie',
                           labels='Segment',
                           values="Revenue (Billion USD)"
                           )
                 with tgb.part():
                    tgb.text(' ')

#Read CSV file for second page
       
revenue= pd.read_csv('Revenue.csv')
revenue_copy=revenue.copy()
revenue_copy_1=revenue.copy()

#get unique values for selector
Company = list(revenue["Company"].unique())
selected_company = "Samsung"
selected_company_1 = "Apple"

#Filter the data according to chart
bar_chart=revenue.groupby(['Year','Company'])['Revenue(in Billion)'].mean().reset_index()
bar_chart_1=revenue.groupby(['Year','Company'])['Revenue(in Billion)'].mean().reset_index()

#layout for title
layout_1={"title":'Yearly Revenue'}
layout_2={"title":'Yearly Revenue'}

#Function to filter data based on selected companies
def apply_change_revenue(state):
    state.revenue_copy = state.revenue[state.revenue["Company"] == state.selected_company]
    state.revenue_copy_1 = state.revenue[state.revenue["Company"] == state.selected_company_1]

    state.bar_chart = (state.revenue_copy.groupby(['Year','Company'])['Revenue(in Billion)']
                       .mean()
                       .reset_index())
    state.bar_chart_1 = (state.revenue_copy_1.groupby(['Year','Company'])['Revenue(in Billion)']
                       .mean()
                       .reset_index())
    state.layout_1 = {"title":f'Yearly Revenue {selected_company}'}
    state.layout_2 = {"title":f'Yearly Revenue {selected_company_1}'}
    

# Create the 2nd Taipy page
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
                #selector for companies
                tgb.selector(value = "{selected_company}",
                    lov=Company , 
                    dropdown=True,
                     )
                tgb.selector(value = "{selected_company_1}",
                    lov=Company , 
                    dropdown=True,
                )
            #Button with trigger apply_change_revenue
            with tgb.part():
                tgb.button('Apply',
                           on_action=apply_change_revenue)  #Trigger update on button is clicked
                
        tgb.html('br')   
        # Chart display
        with tgb.layout(columns='1 1'):
            with tgb.part(class_name='card'):
            # Bar chart to show yearly and comparison between two selected companies
                tgb.chart ('{bar_chart}',
                           layout='{layout_1}',
                           type='bar',
                           x='Year',
                           y='Revenue(in Billion)'                      
                           ) 
            with tgb.part(class_name='card'):
                tgb.chart ('{bar_chart_1}',
                           layout='{layout_2}',
                           type='bar',
                           x='Year',
                           y='Revenue(in Billion)'                      
                           ) 
                
# Create the 3rd Taipy page
with tgb.Page() as Page3:
    with tgb.part(class_name="body"):
        tgb.text('# The Tech Titans: Samsung vs. Apple vs. Motorola',mode='md')
        with tgb.layout(columns='2 3 '):
            with tgb.part():
                tgb.text(" ")
            with tgb.part(): 
                tgb.navbar()
            tgb.html('br')
        #showing table used for this analysis
        with tgb.part():
            tgb.text('## Reference', mode='md')
            tgb.table("{merged}")
            tgb.html('br')
        with tgb.part():
            tgb.table('{revenue}')
            
        
# Create and run the GUI 

pages = {"Overview" : Home,
         "Comparison" : Page2,
          "Data" : Page3 }

app = Gui(pages=pages)


app.run(use_reloader=False,
        title='Mobile Brand Comparison',
        port='auto',
        watermark='Designed by Shreya'
        )
