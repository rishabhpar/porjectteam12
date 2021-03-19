// src/components/Home.jsx
import React from "react";
import {Button} from "reactstrap";
import './style.css';

var divStyle = {
    color:'white'
};

function Home() {
    return (

        <div className="container">
            <div className="main">
                <h1 style={divStyle}> <strong>Landing Page</strong> - Project Team 12 </h1>
                <br/>
                    <h5 style={divStyle}>Currently only has the login system <span role="img" aria-label="lock">🔒</span>
                        <br></br>
                        Built with React, Flask, and MongoDB (so far)</h5>
                <br/>
                <div>

                    <a className='divStyle' href="/login">
                        <Button size="lg"  color="light">Sign In</Button>
                    </a>

                    <a className='divStyle' href="/register">
                        <Button  size="lg"  color="light">Register</Button>
                    </a>

                </div>
            </div>
        </div>
    );
}

export default Home;