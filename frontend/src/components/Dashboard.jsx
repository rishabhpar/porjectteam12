// src/components/Home.jsx
import React from "react";
import './style.css';
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";
import { Button } from 'react';
import auth from "../auth";
import { BiSearchAlt } from "react-icons/bi";

var divStyle = {
    color:'white'
};

class Dashboard extends React.Component {
    state = { err: "" };
    dashboard = (e) => {
        e.preventDefault();
         axios
             .post("http://127.0.0.1:5000/api/dashboard", {
                 // get the form data on submission and post to the server
                 password: document.getElementById("searchpass").value,
                 searchid: document.getElementById("searchid").value
             })
             .then((res) => {
                 if (res.data.error) {
                     // if there is an error, update err with message
                     // and internally communicate that the login failed
                     this.setState({ err: res.data.error });
                     this.setState({ dashboard: false });
                 } else {
                     // else, clear err message
                     // and internally communicate that the login succeeded
                     this.setState({dashboard: true });
                     this.setState({ err: "" });
                     // once logged in reroute to the dashboard and pass email
                     // to show you are logged in with a specific user.
                     this.props.history.push({
                         pathname: "/dashboard",
                         // state: {email: document.getElementById("email").value}
                     });
                 }
             });
     };
    nextPath(path) {
        this.props.history.push(path);
      }

    render () {

        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        // variable to hold an PositiveAlert component that is updated based on the login state
        let positiveAlert;
        if (this.state.dashboard) {
            positiveAlert = <PositiveAlert message={`Found`}></PositiveAlert>;
        }
        return (
            <div className="container">
                 <div className="card-wrapper">
                    <div class="card1">
                        <h3><strong>Welcome</strong> to your dashboard{/*{this.props.location.state.name}*/}</h3>
                        <form name="searchform" onSubmit={this.dashboard}>                       
                        <label className= "searchbar" for="searchid"><strong>Project ID</strong> </label>
                     
                        <input type="searchid" placeholder="Project ID" id="searchid"  class="field" required/>
                        <input type="password" placeholder="Password" id="searchpass"  class="field" required/>
                        <input type="submit" value="Submit" class="btnSearch"/>
                        </form>
                        <button onClick={() => this.nextPath('/newproject')} class = "bigbtn" variant = "outline-primary">NEW PROJECT</button>
                        <button onClick={() => this.nextPath('/')} class = "btnLogout" variant = "outline-primary">Logout</button>
                    </div> 
                    
                </div>    
            </div>
        );
    };
    
    
}

export default Dashboard;