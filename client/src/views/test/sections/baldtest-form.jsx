import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const BaldForm = () => {
  const navigate = useNavigate();

  const [step, setStep] = useState(1);

  const [age, setAge] = useState('');
  const [gender, setGender] = useState(null);
  const [is_married, setIs_married] = useState(null);
  const [is_hereditary, setIs_hereditary] = useState(null);
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [is_smoker, setIs_smoker] = useState(null);
  const [stress, setStress] = useState('');

  const formData = {
    age,
    gender,
    is_married,
    is_hereditary,
    weight,
    height,
    is_smoker,
    stress,
  };

  const nextStep = () => {
    setStep((prevStep) => prevStep + 1);
  };

  const handleSelection = (field, value) => {
    switch (field) {
      case 'gender':
        setGender(value);
        break;
      case 'maritalStatus':
        setIs_married(value);
        break;
      case 'hairLossGenetics':
        setIs_hereditary(value);
        break;
      case 'smoking':
        setIs_smoker(value);
        break;
      default:
        break;
    }
    nextStep();
  };

  const submitForm = () => {
    console.log(formData);
    navigate(`/result?data=${JSON.stringify(formData)}`);
  };

  return (
    <Container>
      <Row className="justify-content-center">
        <Col md="7" className="text-center">
          {step === 1 && (
            <>
              <h1 className="title font-bold">Step 1 Title</h1>
              <h6 className="subtitle">Step 1 Subtitle</h6>
              <input type="number" placeholder="나이" value={age} onChange={(e) => setAge(e.target.value)} />
              <Button variant="outline-primary" className="btn btn-block" onClick={nextStep}>
                다음
              </Button>
            </>
          )}

          {step === 2 && (
            <>
              <h1 className="title font-bold">Step 2 Title</h1>
              <h6 className="subtitle">Step 2 Subtitle</h6>
              <Button variant="outline-primary" className="btn btn-block" onClick={() => handleSelection('gender', 1)}>
                남성
              </Button>
              <Button variant="outline-primary" className="btn btn-block" onClick={() => handleSelection('gender', 0)}>
                여성
              </Button>
            </>
          )}

          {step === 3 && (
            <>
              <h1 className="title font-bold">Step 3 Title</h1>
              <h6 className="subtitle">Step 3 Subtitle</h6>
              <Button
                variant="outline-primary"
                className="btn btn-block"
                onClick={() => handleSelection('maritalStatus', 1)}
              >
                결혼
              </Button>
              <Button
                variant="outline-primary"
                className="btn btn-block"
                onClick={() => handleSelection('maritalStatus', 0)}
              >
                미혼
              </Button>
            </>
          )}

          {step === 4 && (
            <>
              <h1 className="title font-bold">Step 4 Title</h1>
              <h6 className="subtitle">Step 4 Subtitle</h6>
              <Button
                variant="outline-primary"
                className="btn btn-block"
                onClick={() => handleSelection('hairLossGenetics', 1)}
              >
                유전 있음
              </Button>
              <Button
                variant="outline-primary"
                className="btn btn-block"
                onClick={() => handleSelection('hairLossGenetics', 0)}
              >
                유전 없음
              </Button>
            </>
          )}

          {step === 5 && (
            <>
              <h1 className="title font-bold">Step 5 Title</h1>
              <h6 className="subtitle">Step 5 Subtitle</h6>
              <input type="number" placeholder="몸무게" value={weight} onChange={(e) => setWeight(e.target.value)} />
              <Button variant="outline-primary" className="btn btn-block" onClick={nextStep}>
                다음
              </Button>
            </>
          )}

          {step === 6 && (
            <>
              <h1 className="title font-bold">Step 6 Title</h1>
              <h6 className="subtitle">Step 6 Subtitle</h6>
              <input type="number" placeholder="키" value={height} onChange={(e) => setHeight(e.target.value)} />
              <Button variant="outline-primary" className="btn btn-block" onClick={nextStep}>
                다음
              </Button>
            </>
          )}

          {step === 7 && (
            <>
              <h1 className="title font-bold">Step 7 Title</h1>
              <h6 className="subtitle">Step 7 Subtitle</h6>
              <Button variant="outline-primary" className="btn btn-block" onClick={() => handleSelection('smoking', 1)}>
                흡연
              </Button>
              <Button variant="outline-primary" className="btn btn-block" onClick={() => handleSelection('smoking', 0)}>
                비흡연
              </Button>
            </>
          )}

          {step === 8 && (
            <>
              <h1 className="title font-bold">Step 8 Title</h1>
              <h6 className="subtitle">Step 8 Subtitle</h6>
              <input
                type="number"
                placeholder="스트레스 수치"
                value={stress}
                onChange={(e) => setStress(e.target.value)}
              />
              <Button variant="outline-primary" className="btn btn-block" onClick={submitForm}>
                제출
              </Button>
            </>
          )}
        </Col>
      </Row>
    </Container>
  );
};

export default BaldForm;
