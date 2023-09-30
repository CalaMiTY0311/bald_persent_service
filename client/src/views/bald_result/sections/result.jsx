import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

//import { Container, Row, Col } from 'reactstrap';

//predict persent when image
import img1 from '../../../assets/images/ui/img6.jpg';
import img2 from '../../../assets/images/ui/5.jpg';
import img3 from '../../../assets/images/ui/1.jpg'

//notbad Bald persent

const Result = () => {
	
	const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
	const dataParam = searchParams.get('data');

    const [resultPredict, setresultPredict] = useState(null);
    
    let imgPath = '';

	const data = JSON.parse(dataParam);

    useEffect(() => {
	axios.post('http://localhost:8000/bald_persent_predict', data)
        .then(response =>{
            const resultPredict = Math.floor(response.data.predict*100);
            setresultPredict(resultPredict);
	
            if (resultPredict >= 1 && resultPredict <= 30) {
        		imgPath = img1;
        		console.log('good')
    		} else if (resultPredict > 30 && resultPredict <= 60) {
        		imgPath = img2;
        		console.log('bad')
    		} // 여기에 필요한 다른 조건을 추가할 수 있습니다. 

            console.log(resultPredict)
        })
        .catch(error => {
            console.log('error:',error)
        })
    }, [])
	
	
    if (resultPredict >= 1 && resultPredict <= 30) {
        imgPath = img1;
        console.log('good')
    } else if (resultPredict > 30 && resultPredict <= 60) {
        imgPath = img2;
        console.log('bad')
    } // 여기에 필요한 다른 조건을 추가할 수 있습니다. 

    return (
        <div>
            { resultPredict !==null && (
                <div>
                {resultPredict}
                { imgPath }
            	</div>
            ) }
        </div>
        // <div>
        //     <div className="spacer" id="imgs-component">
        //         <Container>
        //             <Row className="justify-content-center">
        //                 <Col md="7" className="text-center">
        //                     <h1 className="title font-bold">Result</h1>
        //                     <h6 className="subtitle">Here you can check Demos we created based on WrapKit. Its quite easy to Create your own dream website &amp; dashboard in No-time.</h6>
        //                     {/* <div><h1>Baldness Result</h1> {imgPath && <img src={imgPath} alt={`Baldness ${responseData}%`} />} </div> */}
        //                 	<p>Percentage: {responseData.predict}%</p>
        //                 </Col>
        //             </Row>
        //         </Container>
        //     </div>
        //     <Container>
        //         <Row>
        //             <Col lg="12" className="text-center m-b-30">
        //                 <h4 className="card-title">Image with circle</h4>
        //                 <h6 className="card-subtitle"><code>.img-circle</code> Make sure the image is square not ractangle</h6>
        //                 <img src={img2} alt="img" className="img-circle" width="290" />
        //                 <p className="m-t-15 m-b-0"></p>
        //             </Col>
        //         </Row>
        //     </Container>
        // </div>
    );
}

export default Result;

