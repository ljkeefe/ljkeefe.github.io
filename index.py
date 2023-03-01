#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jupyter_dash import JupyterDash
from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from navbar import create_navbar
from page_2 import create_page_2, df2
from page_3 import create_page_3, df
from page_4 import create_page_4
from home import create_page_home

server = app.server
app.config.suppress_callback_exceptions = True
png_list = []

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
    if pathname == '/page-4':
        return create_page_4()
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

@app.callback(
    Output('dd-output-container', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return figgies[value]

@app.callback(
    Output({"type": "download", "index": ALL}, "data"),
    [
        Input("close", "n_clicks"),
        State({"type": "graph", "index": ALL}, "figure")
    ],
    prevent_initial_call=True
)
def download_figure(n_clicks, figs):
    with open('Dendrograms', 'w') as f:
        for fig in png_list:
            if separator:
                f.write(separator)
            f.write(figgies[fig].to_html(full_html=False, include_plotlyjs=False))
    return dcc.send_file(f)

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return
    return is_open

@app.callback(
    Output("multi-selected-value", "children"), Input("framework-multi-select", "value")
)
def select_value(value):
    png_list.append(value)

if __name__ == '__main__':
    app.run_server(debug=False)
