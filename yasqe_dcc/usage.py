import yasqe_dcc
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__,
                external_stylesheets=['//cdn.jsdelivr.net/npm/yasgui-yasqe@2.11.22/dist/yasqe.min.css']
                )

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    html.Div(id='output'),
    html.Br(),
    html.Button('Display', id='display-query'),
    yasqe_dcc.YasqeDcc(
        id='yasqe-example', value="select * where {?s ?p ?o}", style={'height':'100','width': '80%'}
    ),
])

@app.callback(Output('output', 'children'),
              [Input('display-query', 'n_clicks')],
              [State('yasqe-example', 'value')])
def display_output(n_clicks, value):
    if n_clicks and n_clicks>0:
        return 'You have entered {}'.format(value)
    return ""


if __name__ == '__main__':
    app.run_server()