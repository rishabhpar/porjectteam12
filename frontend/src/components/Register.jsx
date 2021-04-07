// src/components/Register.jsx
import React, { Component } from "react";
// axios is used to communicate with the flask server from react
import axios from "axios";
import Alert from "./Alert";
import "./style.css";
import PositiveAlert from "./PositiveAlert";
import { config } from './Constants'

class Register extends Component {
    // state of the Register component
    // err is the error message flask server returned
    state = { err: "" };

    // register is an onSubmit function that will post 
    // form submission data to the server
    register = (e) => {
        e.preventDefault();
        axios
            .post(config.url.API_URL.concat("/api/register"), {
                // get the form data on submission and post to the server
                email: document.getElementById("email").value,
                name: document.getElementById("name").value,
                password: document.getElementById("password").value,
                confirm_password: document.getElementById("confirm_password").value
            })
            .then((res) => {
                if (res.data.error) {
                    // if there is an error, update err with message
                    // and internally communicate that the registration failed
                    this.setState({ err: res.data.error });
                    this.setState({ register: false });
                } else {
                    // else, clear err message
                    // and internally communicate that the registration succeeded
                    this.setState({ register: true });
                    this.setState({ err: "" });

                    // this will reroute to the sign in page directly after 3 seconds
                    setTimeout(() => {
                        this.props.history.push("/login");
                    }, 3000);
                }
            });
    };


    render() {
        // variable to hold an Alert component that is updated based on the err state
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        }

        // variable to hold an PositiveAlert component that is updated based on the register state
        let positiveAlert;
        if (this.state.register) {
            positiveAlert = <PositiveAlert message={`You're registered! Taking you to the sign in page...`}></PositiveAlert>;
        }
        return (
            <div className="main">
                <div className="card-wrapper">
                    <div class="card">
                        <h1 class="center">Create an Account</h1>
                        {/* link to the sign in form for new users */}
                        <h2 class="center">Already Registered? <a href="/login">Sign In</a></h2>
                        {/* create the form and set the onSubmit task to be the register function above */}
                        <form name="signup_form" onSubmit={this.register}>
                            <label for="name">Name</label>
                            <input type="text" id="name" class="field" required/>

                            <label for="email">Email</label>
                            <input type="email" id="email" class="field" required/>

                            <label for="password">Password</label>
                            <input type="password" id="password" class="field" required/>

                            <label for="password">Reenter Password</label>
                            <input type="password" id="confirm_password" class="field" required/>

                            {/* insert the alert initialized above */}
                            {alert}

                            <span>
                                <input type="submit" value="Sign Up" class="btn"/>
                                {/* if the registration is successful, communicate with user that it is done */}
                                {positiveAlert}
                            </span>
                        </form>
                        
                        {/* go back to the landing page */}
                        <h2 class="center">Cancel? <a href="/">Go Back</a></h2>
                    </div>
                </div>       
            </div>
                     
        );
    }
}

export default Register;