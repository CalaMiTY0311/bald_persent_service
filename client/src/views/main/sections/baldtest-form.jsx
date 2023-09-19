import React, { useState } from 'react';
import axios from 'axios';
import { Container, Row, Col, Form, FormGroup, Label, Input, Button } from 'reactstrap';


function Baldform ()  {

    const [age, setAge] = useState(''); 
    const [gender, setGender] = useState(1); 
    const [isMarried, setIsMarried] = useState(1); 
    const [isHereditary, setIsHereditary] = useState(1); 
    const [weight, setWeight] = useState(''); 
    const [height, setHeight] = useState(''); 
    const [isSmoker, setIsSmoker] = useState(1); 
    const [stress, setStress] = useState(1);

    const Bald_datapost =  () => {
		const data = { 
            			age: age, 
            			gender: gender, 
                        is_married: isMarried, 
                        is_hereditary: isHereditary, 
                        weight: weight, 
                        height: height, 
                        is_smoker: isSmoker, 
                        stress: stress, 
                    };
        
        axios.post('http://localhost:8000/bald_persent_predict', data)
        .then(response =>{
            console.log(response)
        })
        .catch(error => {
            console.log('error:',error)
        })
    }

    return (
        <div>
            <div className="spacer" id="forms-component">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="7" className="text-center">
                            <h1 className="title font-bold">Form</h1>
                            <h6 className="subtitle">age = Age of people in datagender = Male or female (1 = Male and 0 = female)</h6>
							<h6 className="subtitle">is_married = Married status (1 = Yes and 0 = No)</h6>
							<h6 className="subtitle">is_hereditary = Is the bald based from hereditary? (1 = Yes and 0 = No)</h6>
							<h6 className="subtitle">weight = weight of people body in data</h6>
							<h6 className="subtitle">height = height of people body in data</h6>
							<h6 className="subtitle">is_smoker = Is the people a smoker? (1 = Yes and 0 = No)</h6>
							<h6 className="subtitle">stress = Stress level of people in range 1 (lower) to 10 (highest)</h6>
                        </Col>
                    </Row>
                </Container>
            </div>
            <Container>
                <Row>
                    <Col md="12">
                        <Form className="row">
                        <FormGroup>
        <Label htmlFor="age">Age</Label>
        <Input
          type="number"
          className="form-control"
          id="age"
          placeholder="Enter Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </FormGroup>
      <FormGroup>
        <Label htmlFor="gender">Gender</Label>
        <Input
          type="select"
          className="form-control"
          id="gender"
          value={gender}
          onChange={(e) => setGender(e.target.value)}
        >
          <option value={1}>Male</option>
          <option value={0}>Female</option>
        </Input>
      </FormGroup>
      <FormGroup>
        <Label htmlFor="is_married">Married</Label>
        <Input
          type="select"
          className="form-control"
          id="is_married"
          value={isMarried}
          onChange={(e) => setIsMarried(e.target.value)}
        >
          <option value={1}>Yes</option>
          <option value={0}>No</option>
        </Input>
      </FormGroup>
      <FormGroup>
        <Label htmlFor="is_hereditary">Hereditary</Label>
        <Input
          type="select"
          className="form-control"
          id="is_hereditary"
          value={isHereditary}
          onChange={(e) => setIsHereditary(e.target.value)}
        >
          <option value={1}>Yes</option>
          <option value={0}>No</option>
        </Input>
      </FormGroup>
      <FormGroup>
        <Label htmlFor="weight">Weight</Label>
        <Input
          type="number"
          className="form-control"
          id="weight"
          placeholder="Enter Weight"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
        />
      </FormGroup>
      <FormGroup>
        <Label htmlFor="height">Height</Label>
        <Input
          type="number"
          className="form-control"
          id="height"
          placeholder="Enter Height"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
        />
      </FormGroup>
      <FormGroup>
        <Label htmlFor="is_smoker">Smoker</Label>
        <Input
          type="select"
          className="form-control"
          id="is_smoker"
          value={isSmoker}
          onChange={(e) => setIsSmoker(e.target.value)}
        >
          <option value={1}>Yes</option>
          <option value={0}>No</option>
        </Input>
      </FormGroup>
      <FormGroup>
        <Label htmlFor="stress">Stress</Label>
        <Input
          type="number"
          className="form-control"
          id="stress"
          placeholder="Enter Stress Level (1-10)"
          value={stress}
          onChange={(e) => setStress(e.target.value)}
        />
      </FormGroup>
                            <Col md="12">
                                <Button onClick={Bald_datapost} type="button" className="btn btn-success waves-effect waves-light m-r-10">Submit</Button>
                                <Button type="submit" className="btn btn-inverse waves-effect waves-light">Cancel</Button>
                            </Col>
                        </Form>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default Baldform;
