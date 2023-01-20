#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dash import html, dcc, dash_table
import pandas as pd
from navbar import create_navbar
from data import pie_df

nav = create_navbar()
def TURF(data):
    my_frame = data.copy()
    r = 1
    f = 1
    turf = []
    cum_reach = 0
    remaining=len(data)
    while (r > 0) and (f != 0):
        summy = my_frame.sum()
        flavor = summy[summy == summy.max()]
        f = flavor.values[0]
        removed = len(my_frame[my_frame[flavor.index[0]] == 1])
        inc_reach = removed/len(data)
        cum_reach+=inc_reach
        remaining-=removed
        turf.append([flavor.index[0], len(data), removed, remaining, inc_reach, cum_reach])
        my_frame = my_frame[my_frame[flavor.index[0]] != 1]
        r = remaining
        
    analysis_frame = pd.DataFrame(turf, columns = ['Flavor', 'N', 'Removed', 'Remaining', 'Incremental Reach', 'Cumulative Reach'])
    return analysis_frame
df = TURF(pie_df)

def create_page_3():
    header = html.Div(children=[
        html.Div(children=[
            html.H1(children='Project 2 - TURF Analysis',style={'display':'inline-block', "margin": "15px", 'margin-right':-100, 'textAlign' : 'center', 'color' : '#0480B4'}),
            html.Button("Download Excel", id="btn_xlsx2", style={'float': 'right', 'margin': '15px', 'background-color':'#0480B4', 'color':'white', 'border-radius':'5px'}),
            dcc.Download(id="download-dataframe-xlsx2")
        ], style={'textAlign': 'center'}),
        html.H3(children='Top Box',style={"margin-top": "15px", "margin": "15px", 'textAlign' : 'center', 'color' : '#0480B4'}),
        dash_table.DataTable(
            df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
            style_data={
                'color': 'black',
                'border': '1px solid #0480B4',
                'backgroundColor': '#FFFFFF'
            },
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'State'
                    },
                    'textAlign': 'center'
                },
            ],
            style_cell={
                    # all three widths are needed
                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                },
            fixed_rows={'headers': True},
            style_header={
                'backgroundColor': '#AEAEAE',
                'color': 'black',
                'border': '1px solid #0480B4',
                'fontWeight': 'bold',
                'textAlign' : 'center'
            },
            style_table={
                'width': '90%',
                'margin' : 'auto',
                'box-shadow': '5px 5px 10px 3px rgba(0, 0, 0, 0.39)',
                'border': '1px solid #0480B4',
                'maxHeight': '240px', 
                 'overflow': 'scroll'
            },
            style_as_list_view=True,
        )
])
    layout = html.Div([
        nav,
        header,
    ])
    return layout
