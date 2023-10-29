import React, { useState, useEffect, useRef } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

//social container css
import styled from "styled-components";
import { CopyToClipboard } from "react-copy-to-clipboard";
import {
    FacebookShareButton,
    FacebookIcon,
    TwitterShareButton,
    TwitterIcon,
} from "react-share";
import kakaoLogo from '../../../assets/images/logos/kakao-button.jpg';

import { Container, Row, Col } from 'reactstrap';

//predict persent when image
import img1 from '../../../assets/images/bald_result_img/1.jpg';
import img2 from '../../../assets/images/bald_result_img/2.jpg';
// import img3 from '../../../assets/images/ui/1.jpg'

//notbad Bald persent

const Result = () => {
   
   const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
   const dataParam = searchParams.get('data');

    const [resultPredict, setresultPredict] = useState(null);
    const [resultMessage , setresultMessage] = useState(null); 
    
    let imgPath = useRef('');

   const data = JSON.parse(dataParam);

    // get resultPredict
    useEffect(() => {
   axios.post('http://localhost:8000/bald_persent_predict', data)
        .then(response =>{
            const resultPredict = Math.floor(parseInt(response.data.predict*100));
            setresultPredict(resultPredict);
         
         if (resultPredict > 50){
                console.log(resultPredict)
                console.log(true)

                imgPath.current = img1;
                var resultMessage = 'you really really dangerous now'
                setresultMessage(resultMessage)
                console.log('bad')

            } 
            else {
                console.log(false)

                imgPath.current = img2;
              var resultMessage = 'happy happy cat you safe'
              setresultMessage(resultMessage)
                console.log('good')
            }
        })
        .catch(error => {
            console.log('error:',error)
        })
        
    }, [data])

	const FlexContainer = styled.div`
    	display: flex;
        flex-direction: column;
        align-items: center;
    `;
    
    const GridContainer = styled.div`
    	display: grid;
        grid-template-columns: repeat(4, 48px);
        grid-column-gap: 8px;
        justify-content: center;
        align-items: center;
        margin-bottom: 16px;
    `;

    const URLShareButton = styled.button`
    	width: 48px;
        height: 48px;
        color: white;
        border-radius: 24px;
        border: 0px;
        font-weight: 800;
        font-size: 18px;
        cursor: pointer;
        background-color: #7362ff;
        &:hover {
            background-color: #a99fee;
        }
    `;


    const KakaoShareButton = styled.a`
	    cursor: pointer;
        `;

    const KakaoIcon = styled.img`
    	width: 48px;
    	height: 48px;
    	border-radius: 24px;
    `;
    
    const currentUrl = window.location.href;

    useEffect(()=>{
        const kakaoScript = document.createElement('script');
      kakaoScript.src = 'https://developers.kakao.com/sdk/js/kakao.js';
        kakaoScript.onload = () => {
            window.Kakao.init('KEY')
        };
      document.head.appendChild(kakaoScript);
    },[]);

   useEffect(()=>{
        const { Kakao } = window;
        if (Kakao){
            Kakao.Link.createDefaultButton({
               container: '#kakao-share-button',
               objectType: 'feed',
               content: {
                   title:'Baldness Result',
                   description: `Result: ${resultPredict}% - ${resultMessage}`,
               imageUrl: imgPath.current,
                   link:{
                       mobileWebUrl:window.location.href,
                   },
               },
            });
        }
    }, [resultPredict, resultMessage])
	
    return (
        <div>
            <div className="spacer" id="imgs-component">
                <Container>
                    <Row className="justify-content-center">
                        <Col md="7" className="text-center">
                            <h1 className="title font-bold">Result</h1>
                            <h6 className="subtitle">{ resultMessage }</h6>
                            {/* <div><h1>Baldness Result</h1> {imgPath && <img src={imgPath} alt={`Baldness ${responseData}%`} />} </div> */}
                           <p className="font-bold">Percentage: { resultPredict }%</p>
                        </Col>
                    </Row>
                <Row>
                    <Col lg="12" className="text-center m-b-30">
                       <img src={imgPath.current} alt="img" className="img-circle" width="290" />
                        <br/><br/><br/><br/>
                        <h4 className="card-title">Image with circle</h4>
                        <h6 className="card-subtitle"><code>.img-circle</code> Make sure the image is square not ractangle</h6>
                        <p className="m-t-15 m-b-0"></p>
                    </Col>
                </Row>
                {/* <script src="https://t1.kakaocdn.net/kakao_js_sdk/2.4.0/kakao.min.js" 
                      integrity="sha384-mXVrIX2T/Kszp6Z0aEWaA8Nm7J6/ZeWXbL8UpGRjKwWe56Srd/iyNmWMBhcItAjH" 
                        crossorigin="anonymous">
                </script> */}
            </Container>
			
            <FlexContainer>
                <h1>친구들과 공유하기</h1>
                <br/>
                <GridContainer>
                    <FacebookShareButton url={currentUrl}>
                        <FacebookIcon size={48} round={true} borderRadius={24}></FacebookIcon>
                    </FacebookShareButton>
                	<TwitterShareButton url={currentUrl}>
                        <TwitterIcon size={48} round={true} borderRadius={24}></TwitterIcon>
                    </TwitterShareButton>
                    <CopyToClipboard text={currentUrl}>
                        <URLShareButton>URL</URLShareButton>
                    </CopyToClipboard>
                    <KakaoShareButton>
					<KakaoIcon  id="kakao-share-button" src={kakaoLogo}></KakaoIcon>
				</KakaoShareButton>
                </GridContainer>
            </FlexContainer>

        </div>
        </div>
    );
}

export default Result;

