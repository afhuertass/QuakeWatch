import uuid

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from views import uploadapp
from components import sidebar


def get_layout():
    """Create session ID and return page content."""
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        sidebar.get_component(),
        html.Div(id='page-content')
    ])


app.layout = get_layout()


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
               Input('session-id', 'children')])
def display_page(pathname, session_id):
    """Display correct view based on the URL.

    Keyword arguments:
    pathname -- The current URL ending
    session_id -- ID of the current session
    """
    if pathname in ['/', '/upload']:
        return uploadapp.get_layout(session_id)

    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)