import React, { Component } from 'react';
import  Navbar  from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import ChartWrapper from './ChartWrapper';
import DropDownD3 from './DropDownD3';

class App extends Component {
  state = {
    gender: "men"
  }

  genderSelected = (gender) => this.setState({ gender }) //ES6, beacause key value have same, and because single line get rid of {}

  render(){
    return (
      <div className="App">
        <Navbar bg="light">
          <Navbar.Brand>Beautiful BarCharts using React D3 and LifeCycle </Navbar.Brand>
        </Navbar>
        <Container>
          <Row>
            <Col xs={12}><DropDownD3 genderSelected={this.genderSelected} /></Col>
          </Row>
          <Row>
            <Col xs={12}><ChartWrapper gender={this.state.gender} /></Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
