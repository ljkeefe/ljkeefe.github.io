#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dash import html, dcc, dash_table
import pandas as pd
from navbar import create_navbar
from data import pie_df
import plotly.graph_objects as go

nav = create_navbar()
def TURF(data):
    my_frame = data.copy()
    r = 1
    f = 1
    rr=1
    turf = []
    cum_reach = 0
    remaining=len(data)
    while (r > 0) and (f != 0) and (rr > 0):
        summy = my_frame.sum()
        flavor = summy[summy == summy.max()]
        f = flavor.values[0]
        removed = len(my_frame[my_frame[flavor.index[0]] == 1])
        inc_reach = removed/len(data)
        cum_reach+=inc_reach
        remaining-=removed
        if removed > 0:
            turf.append([flavor.index[0], len(data), removed, remaining, round(inc_reach,3), round(cum_reach,3)])
            my_frame = my_frame[my_frame[flavor.index[0]] != 1]
        r = remaining
        rr = removed
        
    analysis_frame = pd.DataFrame(turf, columns = ['Flavor', 'Base Size', 'Removed', 'Remaining', 'Incremental Reach', 'Cumulative Reach'])
    return analysis_frame
df = TURF(pie_df)

def create_page_3():
    header = html.Div(children=[
        html.Div(children=[
            html.H1(children='Project 2 - TURF Analysis',style={'display':'inline-block', "margin": "15px", 'margin-right':-100, 'textAlign' : 'center', 'color' : '#0480B4'}),
            html.Div(children=[
                dcc.Slider(0, 10,
                    step=2,
                    marks={
                        0: '0°F',
                        10: '10°F'
                    })],
                 style={'float':'left'}
            ),
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
                'maxHeight': '80vh', 
                 'overflow': 'scroll'
            },
            style_as_list_view=True,
        ),
        dcc.Graph(figure=go.Figure(
            data=[go.Bar(x=df['Flavor'], y=df['Incremental Reach'])],
            layout=dict(title=dict(text="Incremental Reach of Flavors"))
        ))
])
    layout = html.Div([
        nav,
        header,
    ])
    return layout
