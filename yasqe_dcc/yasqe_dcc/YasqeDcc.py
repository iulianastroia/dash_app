# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class YasqeDcc(Component):
    """A YasqeDcc component.
YasqeDcc is a component which provides SPARQL syntax highlighting.
It takes a property, `query` which should be a SPARQl qeury, and
displays it.

Keyword arguments:
- id (string; required): The ID used to identify this component in Dash callbacks
- value (string; optional): A query that will be displayed in the editor.
- style (dict; optional): Style for the component
- className (string; optional): Often used with CSS to style elements with common properties."""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, value=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'style', 'className']
        self._type = 'YasqeDcc'
        self._namespace = 'yasqe_dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'style', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(YasqeDcc, self).__init__(**args)
