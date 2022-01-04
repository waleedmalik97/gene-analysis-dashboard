import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import os


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG],meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
app.title = "Dashboard"

server = app.server

adult_ciliary_body = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Adult_Ciliary_Body.csv')
fetal_ciliary_body = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Fetal_Ciliary_Body.csv')
adult_cornea = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Adult_Cornea.csv')
fetal_cornea = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Fetal_Cornea.csv')
adult_trabecular_meshwork = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Adult_Trabecular_Meshwork.csv')
fetal_trabecular_meshwork = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/Fetal_Trabecular_Meshwork.csv')

df_adult_ciliary_body = pd.read_csv(adult_ciliary_body)
df_fetal_ciliary_body = pd.read_csv(fetal_ciliary_body)
df_adult_cornea = pd.read_csv(adult_cornea)
df_fetal_cornea = pd.read_csv(fetal_cornea)
df_adult_trabecular_meshwork = pd.read_csv(adult_trabecular_meshwork)
df_fetal_trabecular_meshwork = pd.read_csv(fetal_trabecular_meshwork)

genes_list = ['HAS1','HAS2','HAS3','CD44','LYVE1','HYAL1','HYAL2','HYAL3','HYAL4','VCAN','GGCX','VKORC1','VKORC1L1','BGLAP','PROS1','ATP12A','ATP4A','MGP']

df_adult_cornea_spe = df_adult_cornea[df_adult_cornea['Gene Id'].isin(genes_list)]
df_adult_cornea_spe.sort_values('Gene Id',inplace=True)
df_fetal_cornea_spe = df_fetal_cornea[df_fetal_cornea['Gene Id'].isin(genes_list)]
df_fetal_cornea_spe.sort_values('Gene Id',inplace=True)
df_adult_ciliary_body_spe = df_adult_ciliary_body[df_adult_ciliary_body['Gene Id'].isin(genes_list)]
df_adult_ciliary_body_spe.sort_values('Gene Id',inplace=True)
df_fetal_ciliary_body_spe = df_fetal_ciliary_body[df_fetal_ciliary_body['Gene Id'].isin(genes_list)]
df_fetal_ciliary_body_spe.sort_values('Gene Id',inplace=True)
df_adult_trabecular_meshwork_spe = df_adult_trabecular_meshwork[df_adult_trabecular_meshwork['Gene Id'].isin(genes_list)]
df_adult_trabecular_meshwork_spe.sort_values('Gene Id',inplace=True)
df_fetal_trabecular_meshwork_spe = df_fetal_trabecular_meshwork[df_fetal_trabecular_meshwork['Gene Id'].isin(genes_list)]
df_fetal_trabecular_meshwork_spe.sort_values('Gene Id',inplace=True)

# df_adult_cornea.sort_values('FPKM',ascending=False,inplace=True)
# df_adult_cornea = df_adult_cornea.head(100)
# df_fetal_cornea.sort_values('FPKM',ascending=False,inplace=True)
# df_fetal_cornea = df_fetal_cornea.head(100)
# df_adult_ciliary_body.sort_values('FPKM',ascending=False,inplace=True)
# df_adult_ciliary_body = df_adult_ciliary_body.head(100)
# df_fetal_ciliary_body.sort_values('FPKM',ascending=False,inplace=True)
# df_fetal_ciliary_body = df_fetal_ciliary_body.head(100)
# df_adult_trabecular_meshwork.sort_values('FPKM',ascending=False,inplace=True)
# df_adult_trabecular_meshwork = df_adult_trabecular_meshwork.head(100)
# df_fetal_trabecular_meshwork.sort_values('FPKM',ascending=False,inplace=True)
# df_fetal_trabecular_meshwork = df_fetal_trabecular_meshwork.head(100)

fig1 = go.Figure()
fig1_1 = go.Figure()
fig2 = go.Figure()
fig2_2 = go.Figure()
fig3 = go.Figure()
fig3_3 = go.Figure()
fig4 = go.Figure()
fig4_4 = go.Figure()
fig5 = go.Figure()
fig5_5 = go.Figure()
fig6 = go.Figure()
fig6_6 = go.Figure()
fig1.add_trace(go.Bar(x=df_adult_cornea_spe['Gene Id'],
                y=df_adult_cornea_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig1.add_trace(go.Bar(x=df_adult_cornea_spe['Gene Id'],
                y=df_adult_cornea_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig1.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Cornea',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig1.update_xaxes(showgrid=False, zeroline=False)
fig1.update_yaxes(showgrid=False, zeroline=False)

fig1_1.add_trace(go.Bar(x=df_adult_cornea_spe['Gene Id'],
                y=df_adult_cornea_spe['FPKM'],
                name='FPKM',
                ))
fig1_1.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Cornea',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig1_1.update_xaxes(showgrid=False, zeroline=False)
fig1_1.update_yaxes(showgrid=False, zeroline=False)



fig2.add_trace(go.Bar(x=df_fetal_cornea_spe['Gene Id'],
                y=df_fetal_cornea_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig2.add_trace(go.Bar(x=df_fetal_cornea_spe['Gene Id'],
                y=df_fetal_cornea_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig2.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Cornea',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig2.update_xaxes(showgrid=False, zeroline=False)
fig2.update_yaxes(showgrid=False, zeroline=False)


fig2_2.add_trace(go.Bar(x=df_fetal_cornea_spe['Gene Id'],
                y=df_fetal_cornea_spe['FPKM'],
                name='FPKM',
                ))

fig2_2.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Cornea',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig2_2.update_xaxes(showgrid=False, zeroline=False)
fig2_2.update_yaxes(showgrid=False, zeroline=False)



fig3.add_trace(go.Bar(x=df_adult_ciliary_body_spe['Gene Id'],
                y=df_adult_ciliary_body_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig3.add_trace(go.Bar(x=df_adult_ciliary_body_spe['Gene Id'],
                y=df_adult_ciliary_body_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig3.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Ciliary Body',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig3.update_xaxes(showgrid=False, zeroline=False)
fig3.update_yaxes(showgrid=False, zeroline=False)

fig3_3.add_trace(go.Bar(x=df_adult_ciliary_body_spe['Gene Id'],
                y=df_adult_ciliary_body_spe['FPKM'],
                name='FPKM',
                ))

fig3_3.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Ciliary Body',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig3_3.update_xaxes(showgrid=False, zeroline=False)
fig3_3.update_yaxes(showgrid=False, zeroline=False)


fig4.add_trace(go.Bar(x=df_fetal_ciliary_body_spe['Gene Id'],
                y=df_fetal_ciliary_body_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig4.add_trace(go.Bar(x=df_fetal_ciliary_body_spe['Gene Id'],
                y=df_fetal_ciliary_body_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig4.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Ciliary Body',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig4.update_xaxes(showgrid=False, zeroline=False)
fig4.update_yaxes(showgrid=False, zeroline=False)


fig4_4.add_trace(go.Bar(x=df_fetal_ciliary_body_spe['Gene Id'],
                y=df_fetal_ciliary_body_spe['FPKM'],
                name='FPKM',
                ))
fig4_4.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Ciliary Body',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig4_4.update_xaxes(showgrid=False, zeroline=False)
fig4_4.update_yaxes(showgrid=False, zeroline=False)




fig5.add_trace(go.Bar(x=df_adult_trabecular_meshwork_spe['Gene Id'],
                y=df_adult_trabecular_meshwork_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig5.add_trace(go.Bar(x=df_adult_trabecular_meshwork_spe['Gene Id'],
                y=df_adult_trabecular_meshwork_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig5.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Trabecular Meshwork',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig5.update_xaxes(showgrid=False, zeroline=False)
fig5.update_yaxes(showgrid=False, zeroline=False)


fig5_5.add_trace(go.Bar(x=df_adult_trabecular_meshwork_spe['Gene Id'],
                y=df_adult_trabecular_meshwork_spe['FPKM'],
                name='FPKM',
                ))

fig5_5.update_layout(
    yaxis=dict(title='FPKM'),
    title='Adult Trabecular Meshwork',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)
fig5_5.update_xaxes(showgrid=False, zeroline=False)
fig5_5.update_yaxes(showgrid=False, zeroline=False)



fig6.add_trace(go.Bar(x=df_fetal_trabecular_meshwork_spe['Gene Id'],
                y=df_fetal_trabecular_meshwork_spe['FPKM Lower CI'],
                name='FPKM Lower CI',
                ))
fig6.add_trace(go.Bar(x=df_fetal_trabecular_meshwork_spe['Gene Id'],
                y=df_fetal_trabecular_meshwork_spe['FPKM Higher CI'],
                name='FPKM Higher CI',
                ))

fig6.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Trabecular Meshwork',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)

fig6.update_xaxes(showgrid=False, zeroline=False)
fig6.update_yaxes(showgrid=False, zeroline=False)


fig6_6.add_trace(go.Bar(x=df_fetal_trabecular_meshwork_spe['Gene Id'],
                y=df_fetal_trabecular_meshwork_spe['FPKM'],
                name='FPKM',
                ))

fig6_6.update_layout(
    yaxis=dict(title='FPKM'),
    title='Fetal Trabecular Meshwork',
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1,
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',
    font=dict(color='#adafae')
)

fig6_6.update_xaxes(showgrid=False, zeroline=False)
fig6_6.update_yaxes(showgrid=False, zeroline=False)



# fig1.update_xaxes(type='category')



app.layout = dbc.Container(
                          [
                          html.Div([
                          html.H3(['Dashboard for Genes Analysis'],style={'text-align':'center','color':'#adafae'}),
                          html.Hr(style={'background-color':'rgba(61,61,61,0.5)'}),
                          ],style={'margin-top':'10px'}),
                          dbc.Row(
                                 [
                                 dbc.Col(id='col-1',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-1',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-1',figure=fig1)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-1-1',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-1-1',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-1-1',figure=fig1_1)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-2',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-2',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-2',figure=fig2)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-2-2',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-2-2',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-2-2',figure=fig2_2)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-3',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-3',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-3',figure=fig3)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-3-3',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-3-3',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-3-3',figure=fig3_3)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-4',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-4',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-4',figure=fig4)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-4-4',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-4-4',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-4-4',figure=fig4_4)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-5',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-5',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-5',figure=fig5)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-5-5',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-5-5',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-5-5',figure=fig5_5)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-6',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-6',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-6',figure=fig6)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 ),
                                 dbc.Col(id='col-6-6',
                                         children=[
                                         dbc.Card(
                                                  [
                                                  dbc.CardBody(
                                                               [
                                                               dbc.Button(id='btn-6-6',children=["Expand"], color="primary", className="me-1"),
                                                               dcc.Graph(id='graph-6-6',figure=fig6_6)
                                                               ]
                                                  )
                                                  ]
                                         )
                                         ],style={'padding':'10px'},md=3
                                 )

                                 ]
                          ),
                          dbc.Row(
                                  [
                                  dbc.Col(
                                          [
                                          dbc.Card(
                                                   [
                                                   dbc.CardBody(
                                                                [
                                                                dbc.Input(id="gene-search", placeholder="Type Gene ID", type="text"),
                                                                dbc.Button(id='btn-7',children=["Submit"],color='primary',className='me-1',style={'margin-top':'10px'}),
                                                                html.Div(id='graph-7')
                                                                ]
                                                   )
                                                   ]
                                          )
                                          ],style={'padding':'10px'}
                                  )
                                  ]
                          )

                          ],fluid=True
)

@app.callback(
    [Output('col-1','style'),Output('btn-1','children')],
    [Input('btn-1','n_clicks')]
)

def update_graph_1(btn1):

    if (btn1 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]

@app.callback(
    [Output('col-1-1','style'),Output('btn-1-1','children')],
    [Input('btn-1-1','n_clicks')]
)

def update_graph_1_1(btn1):

    if (btn1 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]



@app.callback(
    [Output('col-2','style'),Output('btn-2','children')],
    [Input('btn-2','n_clicks')]
)

def update_graph_2(btn2):

    if (btn2 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]


@app.callback(
    [Output('col-2-2','style'),Output('btn-2-2','children')],
    [Input('btn-2-2','n_clicks')]
)

def update_graph_2_2(btn2):

    if (btn2 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]



@app.callback(
    [Output('col-3','style'),Output('btn-3','children')],
    [Input('btn-3','n_clicks')]
)

def update_graph_3(btn3):

    if (btn3 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]


@app.callback(
    [Output('col-3-3','style'),Output('btn-3-3','children')],
    [Input('btn-3-3','n_clicks')]
)

def update_graph_3_3(btn3):

    if (btn3 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]




@app.callback(
    [Output('col-4','style'),Output('btn-4','children')],
    [Input('btn-4','n_clicks')]
)

def update_graph_4(btn4):

    if (btn4 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]


@app.callback(
    [Output('col-4-4','style'),Output('btn-4-4','children')],
    [Input('btn-4-4','n_clicks')]
)

def update_graph_4_4(btn4):

    if (btn4 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]




@app.callback(
    [Output('col-5','style'),Output('btn-5','children')],
    [Input('btn-5','n_clicks')]
)

def update_graph_5(btn5):

    if (btn5 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]


@app.callback(
    [Output('col-5-5','style'),Output('btn-5-5','children')],
    [Input('btn-5-5','n_clicks')]
)

def update_graph_5_5(btn5):

    if (btn5 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]





@app.callback(
    [Output('col-6','style'),Output('btn-6','children')],
    [Input('btn-6','n_clicks')]
)

def update_graph_6(btn6):

    if (btn6 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]


@app.callback(
    [Output('col-6-6','style'),Output('btn-6-6','children')],
    [Input('btn-6-6','n_clicks')]
)

def update_graph_6_6(btn6):

    if (btn6 % 2 == 0):
        return [{'padding':'10px'},"Expand"]
    else:
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse"]






@app.callback(
    [Output('graph-7','children')],
    [Input('btn-7','n_clicks')],
    [State('gene-search','value')]
)

def update_graph_7(btn7,id):
    button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'btn-7':
        df_filtered1 = df_adult_cornea[df_adult_cornea['Gene Id']  == id]
        df_filtered1.reset_index(drop=True,inplace=True)
        df_filtered1['dataset'] = ["Adult Cornea"]
        df_filtered2 = df_fetal_cornea[df_fetal_cornea['Gene Id'] == id]
        df_filtered2.reset_index(drop=True,inplace=True)
        df_filtered2['dataset'] = ["Fetal Cornea"]
        df_filtered3 = df_adult_ciliary_body[df_adult_ciliary_body['Gene Id'] == id]
        df_filtered3.reset_index(drop=True,inplace=True)
        df_filtered3['dataset'] = ["Adult Ciliary Body"]
        df_filtered4 = df_fetal_ciliary_body[df_fetal_ciliary_body['Gene Id'] == id]
        df_filtered4.reset_index(drop=True,inplace=True)
        df_filtered4['dataset'] = ["Fetal Ciliary Body"]
        df_filtered5 = df_adult_trabecular_meshwork[df_adult_trabecular_meshwork['Gene Id'] == id]
        df_filtered5.reset_index(drop=True,inplace=True)
        df_filtered5['dataset'] = ["Adult Trabecular Meshwork"]
        df_filtered6 = df_fetal_trabecular_meshwork[df_fetal_trabecular_meshwork['Gene Id'] == id]
        df_filtered6.reset_index(drop=True,inplace=True)
        df_filtered6['dataset'] = ["Fetal Trabecular Meshwork"]

        df = pd.concat([df_filtered1,df_filtered2,df_filtered3,df_filtered4,df_filtered5,df_filtered6],ignore_index=True)

        print(df)

        fig7 = go.Figure()

        fig7.add_trace(go.Bar(x=df['dataset'],
                        y=df['FPKM Lower CI'],
                        name='FPKM Lower CI',
                        ))
        fig7.add_trace(go.Bar(x=df['dataset'],
                        y=df['FPKM Higher CI'],
                        name='FPKM Higher CI',
                        ))

        fig7.update_layout(
            yaxis=dict(title='FPKM'),
            title='Gene ID: '+id,
            barmode='group',
            bargap=0.15,
            bargroupgap=0.1,
            paper_bgcolor='rgba(255, 255, 255, 0)',
            plot_bgcolor='rgba(255, 255, 255, 0)',
            font=dict(color='#adafae')
        )

        fig7.update_xaxes(showgrid=False, zeroline=False)
        fig7.update_yaxes(showgrid=False, zeroline=False)

        content = [dcc.Graph(figure=fig7)]

        return [content]
    else:
        return []


if __name__ == "__main__":
    app.run_server(debug=True)
