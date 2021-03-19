// src/components/Register.jsx
import React, { Component } from "react";
import axios from "axios";
import Alert from "./Alert";
import "./style.css";
import PositiveAlert from "./PositiveAlert";

class Register extends Component {
    state = { err: "" };

    register = (e) => {
        e.preventDefault();
        axios
            .post("http://127.0.0.1:5000/api/register", {
                email: document.getElementById("email").value,
                name: document.getElementById("name").value,
                password: document.getElementById("password").value,
            })
            .then((res) => {
                if (res.data.error) {
                    this.setState({ err: res.data.error });
                    this.setState({ register: false });
                } else {
                    this.setState({ register: true });
                    this.setState({ err: "" });
                }
            });
    };

    render() {
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        }
        let positiveAlert;
        if (this.state.register) {
            positiveAlert = <PositiveAlert message={`You're registered!`}></PositiveAlert>;
        }
        return (
            <div className="main">
                <div className="card-wrapper">
                    <div class="card">
                        <h1 class="center">Create an Account</h1>
                        <h2 class="center">Already Registered? <a href="/login">Sign In</a></h2>
                        <form name="signup_form" onSubmit={this.register}>
                            <label for="name">Name</label>
                            <input type="text" id="name" class="field" required/>

                            <label for="email">Email</label>
                            <input type="email" id="email" class="field" required/>

                            <label for="password">Password</label>
                            <input type="password" id="password" class="field" required/>

                            {alert}

                            <span>
                                <input type="submit" value="Sign Up" class="btn"/>
                                {positiveAlert}
                            </span>
                        </form>

                        <h2 class="center">Cancel? <a href="/">Go Back</a></h2>
                    </div>
                </div>       
            </div>
                     
        );
    }
}

export default Register;