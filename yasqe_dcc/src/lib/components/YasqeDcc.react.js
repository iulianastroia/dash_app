import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Yasqe from 'yasgui-yasqe';
import {omit} from 'ramda';

/**
 * YasqeDcc is a component which provides SPARQL syntax highlighting.
 * It takes a property, `query` which should be a SPARQl qeury, and
 * displays it.
 */
export default class YasqeDcc extends Component {
    constructor(props) {
        super(props);
        this.yasqe = 0;
    }

    componentDidMount() {
        const {id, value, setProps} = this.props;
        this.yasqe = Yasqe.fromTextArea(document.getElementById(id));
        if (value) {
            this.yasqe.setValue(value);
            this.yasqe.refresh();
        }

        this.yasqe.on('change', function (instance, changeObj) {
            if (this.props.setProps) {
                this.props.setProps({value: this.yasqe.getValue()});
            }
        }.bind(this));
    }

    componentWillReceiveProps(nextProps) {
        if (this.props.value !== nextProps.value && this.yasqe.getValue() !== nextProps.value){
            this.yasqe.setValue(nextProps.value);
            this.yasqe.refresh();
        }

        if (this.props.setProps && this.props.value !== nextProps.value) {
            this.props=nextProps;
            this.setState((prevState, curProps) => {
                return {id: curProps.id,
                setProps: curProps.setProps,
                value: curProps.value}
            });
        }

    }

    shouldComponentUpdate(nextProps){
        return (this.props.value !== nextProps.value);
    }

    render() {
        const {id, style} = this.props;

        return (
            <textarea
                id = {id}
                style = {style}
                {...omit(['setProps', 'value'], this.props)}
            />
        );
    }
}

YasqeDcc.defaultProps = {
    value: ""
};

YasqeDcc.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string.isRequired,

    /**
     * A query that will be displayed in the editor.
     */
    value: PropTypes.string,

    /**
    * Style for the component
    */
    style: PropTypes.object,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
     setProps: PropTypes.func,

     /**
     * Often used with CSS to style elements with common properties.
     */
     className: PropTypes.string,

};