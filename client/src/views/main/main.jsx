import React from "react";
import PropTypes from "prop-types";

// core components
import Header from "../../components/header/header.jsx";
import HeaderBanner from "../../components/banner/banner.jsx";
import Footer from "../../components/footer/footer.jsx";

// bald components
import Baldform from "./sections/baldtest-form.jsx";


const Main = () => {
    return (
        <div id="main-wrapper">
            <Header />
            <div className="page-wrapper">
                <div className="container-fluid">
                    <HeaderBanner />
                    <Baldform />
                </div>
            </div>
            {/* <Footer /> */}
        </div>
    );
}

Main.propTypes = {
    classes: PropTypes.object
};

export default Main;
