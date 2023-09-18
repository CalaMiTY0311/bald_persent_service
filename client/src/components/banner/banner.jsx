import React from 'react';
import { HashLink as Link } from 'react-router-hash-link';
import { Container, Row, Col } from 'reactstrap';

const HeaderBanner = () => {
    return (
        <div className="static-slider-head">
            <Container>
                <Row className="justify-content-center">
                    <Col lg="8" md="6" className="align-self-center text-center">
                        <h1 className="title">do you know your warning bald persent???</h1>
                        <h4 className="subtitle font-light">bald waring score<br /> i service for you</h4>
                        <Link to="/#coming" className="btn btn-md m-t-30 btn-info-gradiant font-14">go go bald waring test</Link>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default HeaderBanner;
