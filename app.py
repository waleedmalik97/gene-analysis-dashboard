import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import os
import random


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG],meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
app.title = "Dashboard"

server = app.server

df_arr1 = []
df_arr2 = []
df_arr3 = []
df_arr4 = []
df_arr5 = []
df_arr6 = []
df_arr7 = []

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
df_adult_cornea_spe.reset_index(drop=True,inplace=True)
df_fetal_cornea_spe = df_fetal_cornea[df_fetal_cornea['Gene Id'].isin(genes_list)]
df_fetal_cornea_spe.sort_values('Gene Id',inplace=True)
df_fetal_cornea_spe.reset_index(drop=True,inplace=True)
df_adult_ciliary_body_spe = df_adult_ciliary_body[df_adult_ciliary_body['Gene Id'].isin(genes_list)]
df_adult_ciliary_body_spe.sort_values('Gene Id',inplace=True)
df_adult_ciliary_body_spe.reset_index(drop=True,inplace=True)
df_fetal_ciliary_body_spe = df_fetal_ciliary_body[df_fetal_ciliary_body['Gene Id'].isin(genes_list)]
df_fetal_ciliary_body_spe.sort_values('Gene Id',inplace=True)
df_fetal_ciliary_body_spe.reset_index(drop=True,inplace=True)
df_adult_trabecular_meshwork_spe = df_adult_trabecular_meshwork[df_adult_trabecular_meshwork['Gene Id'].isin(genes_list)]
df_adult_trabecular_meshwork_spe.sort_values('Gene Id',inplace=True)
df_adult_trabecular_meshwork_spe.reset_index(drop=True,inplace=True)
df_fetal_trabecular_meshwork_spe = df_fetal_trabecular_meshwork[df_fetal_trabecular_meshwork['Gene Id'].isin(genes_list)]
df_fetal_trabecular_meshwork_spe.sort_values('Gene Id',inplace=True)
df_fetal_trabecular_meshwork_spe.reset_index(drop=True,inplace=True)


def random_color():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color


def create_graph_1(df,title):
    fig = go.Figure()
    traces = []
    for i,gene in zip(range(len(df)),df['Gene Id'].tolist()):
        traces.append({'type':'bar','x':[df['Gene Id'][i]], 'y':[df['FPKM'][i].tolist()],'name':gene,'marker':{'color':random_color()}})
        fig = {
              'data': traces,
              'layout': dict(
                        yaxis=dict(title='FPKM',showgrid=False, zeroline=False),
                        xaxis=dict(tickangle=45),
                        title=title,
                        paper_bgcolor='rgba(255, 255, 255, 0)',
                        plot_bgcolor='rgba(255, 255, 255, 0)',
                        font=dict(color='#adafae')
              )
        }
    return fig


fig1 = create_graph_1(df_adult_cornea_spe,"Adult Cornea")

fig2 = create_graph_1(df_fetal_cornea_spe,"Fetal_Cornea")

fig3 = create_graph_1(df_adult_ciliary_body_spe,"Adult Ciliary Body")

fig4 = create_graph_1(df_fetal_ciliary_body_spe,"Fetal Ciliary Body")

fig5 = create_graph_1(df_adult_trabecular_meshwork_spe,"Adult Trabecular Meshwork")

fig6 = create_graph_1(df_fetal_trabecular_meshwork_spe,"Fetal Trabecular Meshwork")

figs = [fig1,fig2,fig3,fig4,fig5,fig6]

col_content = []

for i,fig in zip(range(1,7),figs):
    col_content.append(dbc.Col(id='col-'+str(i),
            children=[
            dbc.Card(
                     [
                     dbc.CardBody(
                                  [
                                  dbc.Input(id="input-gene-"+str(i), placeholder="Type Gene ID", type="text",style={'display':'none'}),
                                  dbc.Button(id='btn-add-gene-'+str(i),children=["Add Gene"],color='primary',className='me-1',style={'display':'none'}),
                                  dbc.Button(id='btn-'+str(i),children=["Expand"], color="primary", className="me-1"),
                                  dcc.Graph(id='graph-'+str(i),figure=fig)
                                  ]
                     )
                     ]
            )
            ],style={'padding':'10px'},md=4
    ))



app.layout = dbc.Container(
                          [
                          html.Div([
                          html.H3(['Dashboard for Genes Analysis'],style={'text-align':'center','color':'#adafae'}),
                          html.Hr(style={'background-color':'rgba(61,61,61,0.5)'}),
                          ],style={'margin-top':'10px'}),
                          dbc.Row(col_content),
                          dbc.Row(
                                  [
                                  dbc.Col(
                                          [
                                          dbc.Card(
                                                   [
                                                   dbc.CardBody(
                                                                [
                                                                dbc.Input(id="gene-search", placeholder="Type Gene ID", type="text"),
                                                                dbc.Button(id='btn',children=["Submit"],color='primary',className='me-1',style={'margin-top':'10px'}),
                                                                html.Div(id='graph')
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
    [Output('col-1','style'),Output('btn-1','children'),Output('input-gene-1','style'),Output('btn-add-gene-1','style'),Output('graph-1','style')],
    [Input('btn-1','n_clicks')]
)

def update_col_1(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-1','figure')],
    [Input('btn-add-gene-1','n_clicks')],
    [State('input-gene-1','value')]
)

def add_trace_1(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-1':
        df_filtered = df_adult_cornea[df_adult_cornea['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr1.append(df_filtered)
        df_arr1.append(df_adult_cornea_spe)
        df_final = pd.concat(df_arr1,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Adult Cornea")
        return [fig]


@app.callback(
    [Output('col-2','style'),Output('btn-2','children'),Output('input-gene-2','style'),Output('btn-add-gene-2','style'),Output('graph-2','style')],
    [Input('btn-2','n_clicks')]
)

def update_col_2(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-2','figure')],
    [Input('btn-add-gene-2','n_clicks')],
    [State('input-gene-2','value')]
)

def add_trace_2(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-2':
        df_filtered = df_fetal_cornea[df_fetal_cornea['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr2.append(df_filtered)
        df_arr2.append(df_fetal_cornea_spe)
        df_final = pd.concat(df_arr2,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Fetal Cornea")
        return [fig]


@app.callback(
    [Output('col-3','style'),Output('btn-3','children'),Output('input-gene-3','style'),Output('btn-add-gene-3','style'),Output('graph-3','style')],
    [Input('btn-3','n_clicks')]
)

def update_col_3(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-3','figure')],
    [Input('btn-add-gene-3','n_clicks')],
    [State('input-gene-3','value')]
)

def add_trace_3(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-3':
        df_filtered = df_adult_ciliary_body[df_adult_ciliary_body['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr3.append(df_filtered)
        df_arr3.append(df_adult_ciliary_body_spe)
        df_final = pd.concat(df_arr3,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Adult Ciliary Body")
        return [fig]


@app.callback(
    [Output('col-4','style'),Output('btn-4','children'),Output('input-gene-4','style'),Output('btn-add-gene-4','style'),Output('graph-4','style')],
    [Input('btn-4','n_clicks')]
)

def update_col_4(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-4','figure')],
    [Input('btn-add-gene-4','n_clicks')],
    [State('input-gene-4','value')]
)

def add_trace_4(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-4':
        df_filtered = df_fetal_ciliary_body[df_fetal_ciliary_body['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr4.append(df_filtered)
        df_arr4.append(df_fetal_ciliary_body_spe)
        df_final = pd.concat(df_arr4,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Fetal Ciliary Body")
        return [fig]


@app.callback(
    [Output('col-5','style'),Output('btn-5','children'),Output('input-gene-5','style'),Output('btn-add-gene-5','style'),Output('graph-5','style')],
    [Input('btn-5','n_clicks')]
)

def update_col_5(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-5','figure')],
    [Input('btn-add-gene-5','n_clicks')],
    [State('input-gene-5','value')]
)

def add_trace_5(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-5':
        df_filtered = df_adult_trabecular_meshwork[df_adult_trabecular_meshwork['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr5.append(df_filtered)
        df_arr5.append(df_adult_trabecular_meshwork_spe)
        df_final = pd.concat(df_arr5,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Adult Trabecular Meshwork")
        return [fig]


@app.callback(
    [Output('col-6','style'),Output('btn-6','children'),Output('input-gene-6','style'),Output('btn-add-gene-6','style'),Output('graph-6','style')],
    [Input('btn-6','n_clicks')]
)

def update_col_6(btn):

    if (btn % 2 == 0):
        style1 = {'display':'none'}
        style2 = {'height':'450px'}
        return [{'padding':'10px'},"Expand",style1,style1,style2]
    else:
        style1 = {'visibility':'visible','margin':'5px'}
        style2 = {'height':'950px'}
        return [{'height':'100%','width':'100%','position':'absolute','z-index':'1','padding':'10px','top':'91px','left':'0px'},"Collapse",style1,style1,style2]

@app.callback(
    [Output('graph-6','figure')],
    [Input('btn-add-gene-6','n_clicks')],
    [State('input-gene-6','value')]
)

def add_trace_6(btn,gene_id):
    btn_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'btn-add-gene-6':
        df_filtered = df_fetal_trabecular_meshwork[df_fetal_trabecular_meshwork['Gene Id'] == gene_id]
        df_filtered.reset_index(drop=True,inplace=True)
        df_arr6.append(df_filtered)
        df_arr6.append(df_fetal_trabecular_meshwork_spe)
        df_final = pd.concat(df_arr6,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)
        fig = create_graph_1(df_final,"Fetal Trabecular Meshwork")
        return [fig]





@app.callback(
    [Output('graph','children')],
    [Input('btn','n_clicks')],
    [State('gene-search','value')]
)

def update_graph_7(btn7,id):
    button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'btn':
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

        df_arr7.append(df)
        df_final = pd.concat(df_arr7,ignore_index=True)
        df_final.drop_duplicates(inplace=True,ignore_index=True)


        fig = go.Figure()

        for type in df_final['Gene Id'].unique():
            df_filtered = df_final[df_final['Gene Id'] == type]
            fig.add_trace(go.Bar(x=df_filtered['dataset'],
                                 y=df_filtered['FPKM'],
                                 name=type,
                                 marker_color=random_color()
                                 )
                        )
        fig.update_layout(
            yaxis=dict(title='FPKM',showgrid=False, zeroline=False),
            xaxis=dict(tickangle=45),
            title="Overall Comparison",
            paper_bgcolor='rgba(255, 255, 255, 0)',
            plot_bgcolor='rgba(255, 255, 255, 0)',
            font=dict(color='#adafae')
        )

        content = [dcc.Graph(figure=fig)]

        return [content]
    else:
        return []


if __name__ == "__main__":
    app.run_server(debug=False)
