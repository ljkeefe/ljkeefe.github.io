#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dash import html
from navbar import create_navbar

nav = create_navbar()

def create_page_home():
    header = html.Div(children=[
        html.H1('Welcome to the Analysis Dashboard!'),
        
        
    ], style={'margin-top': '15px', 'textAlign': 'center', 'color': '#0480B4'})
    layout = html.Div([
        nav,
        header,
    ])
    return layout


# In[ ]:





# In[ ]:




