from dash import html, dcc, ALL
import numpy as np
from plotly.figure_factory import create_dendrogram
import dash_mantine_components as dmc
from navbar import nav

%run navbar.ipynb

nav = create_navbar()

figgies = {
    'New York City':create_dendrogram(np.random.rand(5,5),orientation='right', labels=[1,2,3,4,5]),
    'Montreal':create_dendrogram(np.random.rand(5,5),orientation='right', labels=[6,7,8,9,10]),
    'San Francisco':create_dendrogram(np.random.rand(5,5),orientation='right', labels=[11,12,13,14, 15]),
}
def create_page_4():
    header = html.Div(children=[
        html.Div(children=[
            html.H1(children='Project 3 - Dendrograms',style={'display':'inline-block', "margin": "15px", 'margin-right':-120, 'textAlign' : 'center', 'color' : '#0480B4'}),
            dbc.Button("Export Dendrograms", id="open", n_clicks=0, style={'float': 'right', 'margin': '5px', 'background-color':'#0480B4', 'color':'white', 'border-radius':'5px', 'padding':'5px', 'padding-left':'7px', 'padding-right':'7px'}),
        ], style={'textAlign': 'center'}),
        html.Div(
            [
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Download Dendrograms"), style={'textAlign':'center'}),
                        html.Center(html.Div(
                            [
                                dmc.MultiSelect(
                                    label="Select the categories of the dendrograms you wish to download",
                                    placeholder="Select categories",
                                    id="framework-multi-select",
                                    value=["ng", "vue"],
                                    data=['New York City', 'Montreal', 'San Francisco'],
                                    searchable=True,
                                    style={"width": 400, "marginBottom": 10, 'textAlign':'left'},
                                )
                            ]
                        )),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Download", id="close", className="ms-auto", n_clicks=0
                            ),
                            #dcc.Download(id="downlo-xlsx2")
                        ),
                    ],
                    id="modal",
                    is_open=False,
                    centered=True
                ),
            ]
        ),
        html.Center(html.Div(
            dcc.Dropdown(
                options=['New York City', 'Montreal', 'San Francisco'],
                value='Montreal', 
                id='demo-dropdown'
            ),
            style={
                'width':'95vw',
                'textAlign': 'left'
            }
        )),
        html.Center(html.Div(
            dcc.Graph(id = 'dd-output-container',responsive=True, style={'height': '80vh'}),
            style={
                'width':'100vw',
                'height':'80vh',
                'justify':'center'
            }
        ))
])
    layout = html.Div([
        nav,
        header,
    ])
    return layout
