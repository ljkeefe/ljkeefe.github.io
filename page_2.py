#!/usr/bin/env python
# coding: utf-8

# In[15]:


from dash import html, dcc, dash_table
import pandas as pd
from navbar import create_navbar
from app import app
from data import MD_agg_df

nav = create_navbar()

df = MD_agg_df.sort_values('MaxDiff Score', ascending=False)

df['MaxDiff Score'] = [str(i)+'%' for i in df['MaxDiff Score']]

def create_page_2():
    header = html.Div(children=[
        html.Div(children=[
            html.H1(children='Project 1 - MaxDiff Analysis',style={'display':'inline-block', "margin": "15px", 'margin-right':-100, 'textAlign' : 'center', 'color' : '#0480B4'}),
            html.Button("Download Excel", id="btn_xlsx", style={'float': 'right', 'margin': '15px', 'background-color':'#0480B4', 'color':'white', 'border-radius':'5px'}),
            dcc.Download(id="download-dataframe-xlsx")
        ], style={'textAlign': 'center'}),
        html.H3(children='MaxDiff Scores',style={"margin-top": "15px", "margin": "15px", 'textAlign' : 'center', 'color' : '#0480B4'}),
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
                        'filter_query': '{MaxDiff Score} > 100'
                    },
                    'backgroundColor': '#04B490'
                },
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
                'maxHeight': '300px', 
                 'overflow': 'scroll'
            }
        ),
    html.H3(children='Top Concepts',style={"margin-top": "15px", "margin": "15px", 'textAlign' : 'center', 'color' : '#0480B4'}),
    html.Ol(children=[
        html.Li(children=df.loc[x,'Item']) for x in df.index if df.loc[x,'MaxDiff Score'] > df['MaxDiff Score'].mean()
    ], style={'textAlign':'center', 'list-style-position': 'inside', 'margin' : 'auto'})
])

    layout = html.Div([
        nav,
        header,
    ])
    return layout
