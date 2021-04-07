// Login.jsx
import React, { Component } from "react";
// axios is used to communicate with the flask server from react
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";
import auth from "../auth";
import { config } from './Constants'

class Login extends Component {
    // state of the Login component
    // err is the error message flask server returned
    state = { err: "" };

    // login is an onSubmit function that will post 
    // form submission data to the server
    login = (e) => {
        e.preventDefault();
        axios
            .post(config.url.API_URL.concat("/api/login"), {
                // get the form data on submission and post to the server
                email: document.getElementById("email").value,
                password: document.getElementById("password").value,
            })
            .then((res) => {
                if (res.data.error) {
                    // if there is an error, update err with message
                    // and internally communicate that the login failed
                    this.setState({ err: res.data.error });
                    this.setState({ login: false });
                } else {
                    // else, clear err message
                    // and internally communicate that the login succeeded
                    this.setState({ login: true });
                    this.setState({ err: "" });

                    // login so the protected routes become viewable
                    auth.login(() => {
                        // once logged in reroute to the dashboard and pass email
                        // to show you are logged in with a specific user.
                        this.props.history.push({
                            pathname: "/dashboard",
                            state: {email: document.getElementById("email").value}
                        });
                    })
                }
            });
    };

    render() {
        // variable to hold an Alert component that is updated based on the err state
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        // variable to hold an PositiveAlert component that is updated based on the login state
        let positiveAlert;
        if (this.state.login) {
            positiveAlert = <PositiveAlert message={`You're Signed In!`}></PositiveAlert>;
        }

        return (
            <div className="main">
                <div className="card-wrapper">
                <div class="card">
                    <h1 class="center">Sign In</h1>
                    {/* link to the register form for new users */}
                    <h2 class="center">New Here? <a href="/register">Register</a></h2>
                    {/* create the form and set the onSubmit task to be the login function above */}
                    <form name="signin_form" onSubmit={this.login}>
                        <label for="email">Email</label>
                        <input type="email" id="email" class="field" required/>

                        <label for="password">Password</label>
                        <input type="password" id="password" class="field" required/>

                        {/* insert the alert initialized above */}
                        {alert}

                        <span>
                            <input type="submit" value="Sign In" class="btn"/>
                            {/* if the login is successful, communicate with user that it is done */}
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

export default Login;