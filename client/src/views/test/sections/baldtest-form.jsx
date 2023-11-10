import React, { useState } from 'react';
import { Container, Row, Col, Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { useNavigate } from 'react-router-dom';

function Baldform() {
  const Navigate = useNavigate();

  const [formData, setFormData] = useState({
    age: '',
    gender: 1,
    is_married: 1,
    is_hereditary: 1,
    weight: '',
    height: '',
    is_smoker: 1,
    stress: 1,
  });

  const questions = [
    { label: '나이', key: 'age', type: 'number', options: [] },
    { label: '성별', key: 'gender', type: 'select', options: ['Male', 'Female'] },
    { label: '결혼여부', key: 'isMarried', type: 'select', options: ['Yes', 'No'] },
    { label: '탈모유전유무', key: 'isHereditary', type: 'select', options: ['Yes', 'No'] },
    { label: '몸무게', key: 'weight', type: 'number', options: [] },
    { label: '키', key: 'height', type: 'number', options: [] },
    { label: '흡연여부', key: 'isSmoker', type: 'select', options: ['Yes', 'No'] },
    { label: '자신이 현재 받고있는 스트레스의 수치를 1~10으로 나타내주세요', key: 'stress', type: 'number', options: [] },
  ];

  const [questionIndex, setQuestionIndex] = useState(0);

  const handleInputChange = (key, value) => {
    setFormData({ ...formData, [key]: value });
  };
  
  const Bald_datapost = () => {
    // You can access the user's responses in the formData object
    // Now, you can use formData to navigate or process the data as needed
    // Navigate(`result?data=${JSON.stringify(formData)}`);
    console.log(formData)
    Navigate(`/result?data=${JSON.stringify(formData)}`)
  };




  const renderQuestion = (question, index) => {
    return (
      <FormGroup key={index}>
        <Label htmlFor={question.key}>{question.label}</Label>
        {question.type === 'select' ? (
          <Input
            type="select"
            className="form-control"
            id={question.key}
            value={formData[question.key]}
            onChange={(e) => handleInputChange(question.key, e.target.value)}
          >
            {question.options.map((option, optionIndex) => (
              <option key={optionIndex} value={option}>
                {option}
              </option>
            ))}
          </Input>
        ) : (
          <Input
            type={question.type}
            className="form-control"
            id={question.key}
            placeholder={`Enter ${question.label}`}
            value={formData[question.key]}
            onChange={(e) => handleInputChange(question.key, e.target.value)}
          />
        )}
      </FormGroup>
    );
  };

  const goToNextQuestion = () => {
    if (questionIndex < questions.length - 1) {
      setQuestionIndex(questionIndex + 1);
    } else {
      Bald_datapost();
    }
  };

  return (
    <div>
      <br />
      <br />
      <br />
      <Container>
        <Row className="justify-content-center">
          <Col md="8">
            <Form className="row">
              {renderQuestion(questions[questionIndex], questionIndex)}
              <Col md="12">
                {questionIndex > 0 && (
                  <Button
                    type="button"
                    onClick={() => setQuestionIndex(questionIndex - 1)}
                    className="btn btn-success waves-effect waves-light m-r-10"
                  >
                    Previous
                  </Button>
                )}
                <Button
                  type="button"
                  onClick={goToNextQuestion}
                  className="btn btn-success waves-effect waves-light m-r-10"
                >
                  {questionIndex < questions.length - 1 ? 'Next' : 'Submit'}
                </Button>
                <Button
                  type="submit"
                  className="btn btn-inverse waves-effect waves-light"
                >
                  Cancel
                </Button>
              </Col>
            </Form>
          </Col>
        </Row>
      </Container>
      <br />
      <br />
      <br />
    </div>
  );
}

export default Baldform;

// import React, { useState } from 'react';
// import { Container, Row, Col, Form, FormGroup, Label, Input, Button } from 'reactstrap';
// import { useNavigate } from 'react-router-dom';


// function Baldform ()  {
  	
//   	const Navigate = useNavigate();
		
//     const [age, setAge] = useState(''); 
//     const [gender, setGender] = useState(1); 
//     const [isMarried, setIsMarried] = useState(1); 
//     const [isHereditary, setIsHereditary] = useState(1); 
//     const [weight, setWeight] = useState(''); 
//     const [height, setHeight] = useState(''); 
//     const [isSmoker, setIsSmoker] = useState(1); 
//     const [stress, setStress] = useState(1);

//     const [questionIndex, setQuestionIndex] = useState(0);
//     const [answers, setAnswers] = useState([]);

//     const questions = [
//       {
//         question: '나이를 입력해주세요',
//         options: [],
//         type: 'number',
//       },
//       {
//         question: '성별을 선택해주세요',
//         options: ['Male', 'Female'],
//         type: 'select',
//       },
//       {
//         question: '결혼 여부를 선택해주세요',
//         options: ['Yes', 'No'],
//         type: 'select',
//       },
//       {
//         question: '탈모 유전을 가지고 계신가요?',
//         options: ['Yes', 'No'],
//         type: 'select',
//       },
//       {
//         question: '몸무게를 알려주세요',
//         options: [],
//         type: 'number',
//         step:'0.1'
//       },
//       {
//         question: '키도 알려주세요',
//         options: [],
//         type: 'number',
//         step:'0.1',
//       },
//       {
//         question: '거의다 오셨어요 흡연은 하시나요?',
//         options: ['Yes', 'No'],
//         type: 'select',
//       },
//       {
//         question: '마지막으로 현재 자신의 스트레스를 1~10으로 표현해주세요',
//         options: [],
//         type: 'number',
//       },
//     ]
//     const handleAnswer = (answer) => {
//       const newAnswers = [...answers];
//       newAnswers[questionIndex] = answer;
//       setAnswers(newAnswers);
//     };
  
//     const handleSubmit = () => {
//       // Calculate the result using answers array and any desired logic
//       // Example: You can use the answers to calculate the MBTI type
//       // const mbtiType = calculateMBTI(answers);
//       // Then you can navigate to the result page with the calculated result
//       Navigate(`/result?data=${JSON.stringify(answers)}`);
//     };


//     const Bald_datapost =  () => {
// 		const data = { 
//             			age: age, 
//             			gender: gender, 
//                         is_married: isMarried, 
//                         is_hereditary: isHereditary, 
//                         weight: weight, 
//                         height: height, 
//                         is_smoker: isSmoker, 
//                         stress: stress, 
//                     };
//                   Navigate(`result?data=${JSON.stringify(data)}`)
                  
//       }
//       const renderQuestion = (question, index) =>{
//     return (
//       <div>
//       <br />
//       <br />
//       <br />
//       <Container>
//         <Row className="justify-content-center">
//           <Col md="8">
//             <Form className="row">
//               {renderQuestion(questions[questionIndex], questionIndex)}
//               <Col md="12">
//                 {questionIndex > 0 && (
//                   <Button
//                     type="button"
//                     onClick={() => setQuestionIndex(questionIndex - 1)}
//                     className="btn btn-success waves-effect waves-light m-r-10"
//                   >
//                     Previous
//                   </Button>
//                 )}
//                 {questionIndex < questions.length - 1 ? (
//                   <Button
//                     type="button"
//                     onClick={() => setQuestionIndex(questionIndex + 1)}
//                     className="btn btn-success waves-effect waves-light m-r-10"
//                   >
//                     Next
//                   </Button>
//                 ) : (
//                   <Button
//                     type="button"
//                     onClick={handleSubmit}
//                     className="btn btn-success waves-effect waves-light m-r-10"
//                   >
//                     Submit
//                   </Button>
//                 )}
//                 <Button
//                   type="submit"
//                   className="btn btn-inverse waves-effect waves-light"
//                 >
//                   Cancel
//                 </Button>
//               </Col>
//             </Form>
//           </Col>
//         </Row>
//       </Container>
//       <br />
//       <br />
//       <br />
//     </div>
//   );
// }
// }

// export default Baldform;
