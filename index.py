#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyter_dash import JupyterDash
from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from navbar import create_navbar
from page_2 import create_page_2, long_data
from page_3 import create_page_3, df
from home import create_page_home

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={'height':'100vh'})
], style={'background-color':'#FFFFFF', 'height': '100vh'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/page-2':
        return create_page_2()
    if pathname == '/page-3':
        return create_page_3()
    else:
        return create_page_home()
    
@app.callback(
        Output("download-dataframe-xlsx", "data"),
        Input("btn_xlsx", "n_clicks"),
        prevent_initial_call=True,
    )
def func(n_clicks):
    return dcc.send_data_frame(long_data.to_excel, "mydf.xlsx", sheet_name="Sheet_name_1")

@app.callback(
        Output("download-dataframe-xlsx2", "data"),
        Input("btn_xlsx2", "n_clicks"),
        prevent_initial_call=True,
    )
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "mydf.xlsx", sheet_name="Sheet_name_1")

if __name__ == '__main__':
    app.run_server(debug=False)
