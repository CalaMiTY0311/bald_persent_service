import React from "react";
import PropTypes from "prop-types";

// core components
// import Header from "../../components/header/header.jsx";
import MainPage from "../../components/main-page/main-page.jsx";
import HeaderBanner from "../../components/banner/banner.jsx";
import Footer from "../../components/footer/footer.jsx";

const Main = () => {
    return (
        <MainPage /> 
    );
}

Main.propTypes = {
    classes: PropTypes.object
};

export default Main;
