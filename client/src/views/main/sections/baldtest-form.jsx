import React, { useState } from 'react';
import { Container, Row, Col, Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { useNavigate } from 'react-router-dom';


function Baldform ()  {
  	
  	const Navigate = useNavigate();
		
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
                  Navigate(`result?data=${JSON.stringify(data)}`)
                  
      }

    return (
        <div>
          <br/><br/><br/>
            <Container>
                <Row className="justify-content-center">
                    <Col md="8">
                        <Form className="row">
                        <FormGroup>
        <Label htmlFor="age">나이</Label>
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
        <Label htmlFor="gender">성별</Label>
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
        <Label htmlFor="is_married">결혼여부</Label>
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
        <Label htmlFor="is_hereditary">탈모유전유무</Label>
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
        <Label htmlFor="weight">몸무게</Label>
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
        <Label htmlFor="height">키</Label>
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
        <Label htmlFor="is_smoker">흡연여부</Label>
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
        <Label htmlFor="stress">자신이 현재 받고있는 스트레스의 수치를 1~10으로 나타내주세요</Label>
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
            <br/><br/><br/>
        </div>
    );
}

export default Baldform;
