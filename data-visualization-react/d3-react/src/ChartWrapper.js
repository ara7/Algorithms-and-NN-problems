import React, { Component } from 'react';
import D3Chart from './D3Chart';

/* 
Wrapper Component using lifecycle method to render the d3 code
*/

export default class ChartWrapper extends Component {
    componentDidMount() {
        //new D3Chart(this.refs.chart)
        this.setState({
            chart: new D3Chart(this.refs.chart)
        })
    }

    shouldComponentUpdate() {
        //allows we want to renrenser react compnent or not if something changes
        return false 
    }

    componentWillReceiveProps(nextProps) {
        this.state.chart.update(nextProps.gender)//update chart
    }

    render() {
        return <div ref="chart"></div>
    }
}