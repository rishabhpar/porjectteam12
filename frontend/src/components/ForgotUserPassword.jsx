// Login.jsx
import React, { Component } from "react";
// axios is used to communicate with the flask server from react
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";
import auth from "../auth";
import { config } from './Constants'

class UpdateUserPassword extends Component {
    // state of the Login component
    // err is the error message flask server returned
    state = { err: "" };

    // update is an onSubmit function that will post 
    // form submission data to the server to update the user password
    updatePassword = (e) => {
        e.preventDefault();
        axios
            .post("https://backendteam12.herokuapp.com/api/updatepassword", {
                // get the form data on submission and post to the server
                email: document.getElementById("email").value,
                currentPassword: document.getElementById("current_password").value,
                newPassword: document.getElementById("new_password").value,
                accountType: "user",
            })
            .then((res) => {
                if (res.data.error) {
                    // if there is an error, update err with message
                    // and internally communicate that the login failed
                    this.setState({ err: res.data.error });
                    this.setState({ updated: false });
                } else {
                    // else, clear err message
                    // and internally communicate that the login succeeded
                    this.setState({ updated: true });
                    this.setState({ err: "" });

                    // this will reroute to the sign in page directly after 1 seconds
                    setTimeout(() => {
                        this.props.history.push("/login");
                    }, 1000);
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
        if (this.state.updated) {
            positiveAlert = <PositiveAlert message={`Your Password is Updated! Taking you to sign in page...`}></PositiveAlert>;
        }

        return (
            <div className="main">
                <div className="card-wrapper">
                <div class="card">
                    <h1 class="center">Update Password</h1>
                    {/* link to the register form for new users */}
                    <h2 class="center">New Here? <a href="/register">Register</a></h2>
                    {/* create the form and set the onSubmit task to be the login function above */}
                    <form name="forgot_password_form" onSubmit={this.updatePassword}>
                        <label for="email">Email</label>
                        <input type="email" id="email" class="field" required/>

                        <label for="password">Current Password</label>
                        <input type="password" id="current_password" class="field" required/>

                        <label for="password">New Password</label>
                        <input type="password" id="new_password" class="field" required/>

                        {/* insert the alert initialized above */}
                        {alert}

                        <span>
                            <input type="submit" value="Update" class="btn"/>
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

export default UpdateUserPassword;