// Login.jsx
import React, { Component } from "react";
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";

class Login extends Component {
    state = { err: "" };

    login = (e) => {
        e.preventDefault();
        axios
            .post("http://127.0.0.1:5000/api/login", {
                email: document.getElementById("email").value,
                password: document.getElementById("password").value,
            })
            .then((res) => {
                if (res.data.error) {
                    this.setState({ err: res.data.error });
                    this.setState({ login: false });
                } else {
                    this.setState({ login: true });
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
        if (this.state.login) {
            positiveAlert = <PositiveAlert message={`You're Signed In!`}></PositiveAlert>;
        }
        return (
            <div className="main">
                <div className="card-wrapper">
                <div class="card">
                    <h1 class="center">Sign In</h1>
                    <h2 class="center">New Here? <a href="/register">Register</a></h2>
                    <form name="signin_form" onSubmit={this.login}>
                        <label for="email">Email</label>
                        <input type="email" id="email" class="field" required/>

                        <label for="password">Password</label>
                        <input type="password" id="password" class="field" required/>

                        {alert}

                        <span>
                            <input type="submit" value="Sign In" class="btn"/>
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

export default Login;