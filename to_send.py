import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output, State
import yasqe_dcc

import dash_bootstrap_components as dbc
import dash

# style to vertically split the screen in two parts
SPARQL_INPUT_STYLE = {'position': 'relative', 'width': '50%', 'float': 'left', 'height': '10%'}
PROPERTIES_STYLE = {'width': '49%', 'display': 'inline-block', 'height': '259px', 'overflow': 'scroll'}

app = dash.Dash(
    external_stylesheets=['//cdn.jsdelivr.net/npm/yasgui-yasqe@2.11.22/dist/yasqe.min.css',
                          dbc.themes.BOOTSTRAP])

# path changes, based on click on "classes", 'prefixes' and 'properties'
PATH_TO_PREFIXES_FILE = r"prefixes_tab.txt"

# needs to change based on file length
prefixes_count = len(open(PATH_TO_PREFIXES_FILE, "r").readlines())


def read_file(tab_name):
    prefixes_file = open(str(tab_name) + ".txt", "r")

    # holds prefixes read from file
    output = []
    for row_number, row_value in enumerate(prefixes_file):
        # append prefixes from file to list
        # get value without \n
        # output.append(dbc.ListGroupItem(row_value.splitlines(), id=str(row_number), n_clicks=0, action=True))
        if row_number == 0:
            output.append(
                dbc.ListGroupItem(row_value, id={"item": str(row_number)}, n_clicks=0, action=True, disabled=True))       
        else:
            output.append(dbc.ListGroupItem(row_value, id={"item": str(row_number)}, n_clicks=0, action=True))
    return output


"""
set layout 
"""
app.layout = html.Div(
    style={'fontFamily': 'Bahnschrift'},
    children=[
        html.H3(children='Select text from list to view into textInput',
                style={'color': 'rgba(0,102,102,1)',
                       'textAlign': 'center'}),
        # SPARQL interpreter (left side of screen)
        html.Div(
            children=[
                yasqe_dcc.YasqeDcc

                    (
                    id='sparql_query',
                    value=" "
                ),

            ],
            style=SPARQL_INPUT_STYLE

        ),
        # WIKI tabs (right side of screen)
        html.Div(children=[
            dbc.Tabs
            (id="wiki_tabs", active_tab='prefixes_tab',
             children=[
                 dbc.Tab(label='Classes', tab_id='classes_tab'),
                 dbc.Tab(label='Prefixes', tab_id='prefixes_tab'),
                 dbc.Tab(label='Properties', tab_id='properties_tab'),
             ], ),
            html.Div(id='wiki_tabs_content')
        ],
        ),
        dbc.Button('Submit Query', id='submit', n_clicks=0, color="info",
                   className="mr-1", style={'margin': '0 auto', 'width': '150px',
                                            'textAlign': 'center',
                                            }),

        html.Div(id='view_query',
                 style={'whiteSpace': 'pre-line', 'textAlign': 'center',
                        'color': 'rgba(0,102,102,1)'}),
        html.Div(id='length_children_tab'

                 )
        , html.Div(id='helper'),
        dbc.ListGroup(id='list_group')

    ])

@app.callback(
    [Output('wiki_tabs_content', 'children'), Output('length_children_tab', 'value')],
    [Input('wiki_tabs', 'active_tab')])
def render_content(tab):
    output = read_file(tab)
    prefix_list = [dbc.ListGroup(id="list_group",
                                 children=
                                 output, style=PROPERTIES_STYLE
                                 ),
                   ]
    return prefix_list, len(output)


@app.callback(
    [Output("helper", "children"), Output("sparql_query", "value")],
    [Input({"item": ALL}, "n_clicks")],
    [Input({"item": ALL}, "children")],
    [Input('length_children_tab', 'value')],
    State('sparql_query', 'value'), prevent_initial_call=True
)
def func(*args):
    print('len', len(args))
    print("args[1]",args[1])
    length_children_tab = args[-2]
    print("args", args)
    print("callback context ", callback_context.triggered[0])
    trigger = callback_context.triggered[0]
    selected_value = trigger["prop_id"].split(".")[0]
    selected_from_value = selected_value.split(":")[1]
    SELECTED_ID = selected_from_value.split('"')[1]
    print("SELECTED ID IS ", SELECTED_ID)
    # SELECTED_VALUE=args[1][int(SELECTED_ID)]


    #
    if int(SELECTED_ID) == 0:
        raise dash.exceptions.PreventUpdate()
    try:
        print("selected option is ", SELECTED_ID)
        # get selected item from prefixes list based on the selected id
        # args is a list of all the ids, followed by the prefixes value
        SELECTED_VALUE = args[1][int(SELECTED_ID)]
        # sparql_query = args[len(args) - 1] + "\n" + selected_value
        # sparql query holds the query from yasqe, followed by the chosen prefix from the list
        sparql_query = args[len(args) - 1] + SELECTED_VALUE
        print("sparql query is ", sparql_query)
        print("selected option is ", )
    except ValueError:
        pass
    return SELECTED_ID, sparql_query


if __name__ == '__main__':
    app.run_server(debug=True, port=8019)
