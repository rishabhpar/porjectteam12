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
                <h1 style={divStyle}> <strong>Welcome</strong> to Hardware Set Rental System 👋</h1>
                <br/>
                <h5 style={divStyle}>Safely borrow our hardware sets to leverage for your projects
                    <br></br>
                    Sign in or register 🔒 to visit/create a project
                </h5>
                <br/>
                <div>
                    {/* Two buttons, one to sign in with and another to register 
                        clicking a button will take you to another component */}
                    <a className='divStyle' href="/login">
                        <Button size="lg"  color="light">Sign In</Button>
                    </a>

                    <a className='divStyle' href="/register">
                        <Button  size="lg"  color="light">Register</Button>
                    </a>

                </div>

                <h5 style={divStyle}>
                    Courtesy of Team 12 😊
                </h5>
            </div>
        </div>
    );
}

export default Home;