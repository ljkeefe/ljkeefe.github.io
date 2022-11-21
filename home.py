#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dash import html
from navbar import create_navbar

nav = create_navbar()

def create_page_home():
    header = html.Div(children=[
        html.H1('Welcome to the Analysis Dashboard!', style={'color' : '#0480B4'}),
        html.Br(),
        html.H3('Project List'),
        html.A('Project 1 - MaxDiff Analysis', href='\page-2'),
        html.Br(),
        html.A('Project 2 - TURF Analysis', href='\page-3')
        
        
    ], style={'margin-top': '15px', 'textAlign': 'center', 'color': '#0480B4'})
    layout = html.Div([
        nav,
        header,
    ])
    return layout
