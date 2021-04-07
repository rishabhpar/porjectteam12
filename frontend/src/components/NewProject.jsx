// NewProject.jsx
import React, { Component } from "react";
// axios is used to communicate with the flask server from react
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";
import auth from "../auth";
import { config } from './Constants'

class NewProject extends Component {
    // state of the NewProject component
    // err is the error message flask server returned
    state = { err: "" };

    // newproject is an onSubmit function that will post 
    // form submission data to the server
    newproject = (e) => {
       e.preventDefault();
        axios
            .post(config.url.API_URL.concat("/api/newproject"), {
                // get the form data on submission and post to the server
                projName: document.getElementById("projName").value,
                description: document.getElementById("description").value,
                projectid: document.getElementById("projectid").value,
                password: document.getElementById("password").value,
            })
            .then((res) => {
                if (res.data.error) {
                    // if there is an error, update err with message
                    // and internally communicate that the project creation failed
                    this.setState({ err: res.data.error });
                    this.setState({ newproject: false });
                } else {
                    // else, clear err message
                    // and internally communicate that the project creation succeeded
                    this.setState({newproject: true });
                    this.setState({ err: "" });
                    // once logged in reroute to the dashboard and pass email
                    // to show you are logged in with a specific user.
                    this.props.history.push({
                        pathname: "/dashboard"
                    });
                }
            });
  
    };
    //finds next authorized path
    nextPath() {
        auth.login(() => {
            this.props.history.push({
                pathname: "/dashboard",
            });
        })
        }

    render() {
        // variable to hold an Alert component that is updated based on the err state
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        // variable to hold an PositiveAlert component that is updated based on the login state
        let positiveAlert;
        if (this.state.newproject) {
            positiveAlert = <PositiveAlert message={`Success!`}></PositiveAlert>;
        }

        return (
            <div className="main">
                <div className="card-wrapper">
                <div class="card">
                    <h1 class="center">New Project</h1>
                    {/* create the form and set the onSubmit task to be the login function above */}
                    <form name="signin_form" onSubmit={this.newproject}>
                        <label for="projName">Project Name</label>
                        <input type="projName" id="projName" class="field" required/>

                        <label for="password">Project Password</label>
                        <input type="password" id="password" class="field" required/>

                        <label for="description">Description</label>
                        <input type="description" id="description" class="field" required/>

                        <label for="projectid">Project ID</label>
                        <input type="projectid" id="projectid" class="field" required/>

                        {/* insert the alert initialized above */}
                        {alert}

                        <span>
                            <input type="submit" value="Submit" class="btn"/>
                            {/* if the project creation is successful, communicate with user that it is done */}
                            {positiveAlert}
                        </span>
                    </form>

                    {/* go back to the landing page */}
                    <button onClick={() => this.nextPath()} class = "btnSub" variant = "outline-primary">Go Back</button>
                </div>
            </div>
            </div>
            
        );
    }
}

export default NewProject;