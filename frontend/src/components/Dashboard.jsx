// src/components/Home.jsx
import React from "react";
import './style.css';
import axios from "axios";
import Alert from "./Alert";
import PositiveAlert from "./PositiveAlert";
import { Button } from 'react';
import auth from "../auth";
import { config } from './Constants'

var divStyle = {
    color:'white'
};

class Dashboard extends React.Component {
    state = { err: "" , arr: [], searcher:''};
     dashboard = (e) => {
        e.preventDefault();
         axios
             .post(config.url.API_URL.concat("/api/dashboard"), {
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
                     // and internally communicate that the project was found
                     this.setState({dashboard: true });
                     this.setState({ err: "" });
                     this.setState({searcher:document.getElementById('searchid').value})
                     // once the project is found reroute to the hardware page
                     setTimeout(() => {
                        this.props.history.push({
                            pathname: "/hardware",
                            state: {searchid: document.getElementById("searchid").value},
                        })
                    }, 3000);
                
                 }
             });};
            
    //potential method to display data from datbase
     displayProject = (arr) =>{
        return arr.map((na, index) => (
            <div key={index}>
                <h3>{arr.name}</h3>
            </div>
        ));
     };

    //method to push external paths
    nextPath(path) {
        this.props.history.push(path);
      };

    render () {

        
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        // variable to hold an PositiveAlert component that is updated based on the project state
        let positiveAlert;
        if (this.state.dashboard) {
            positiveAlert = <PositiveAlert message={`Success! Taking you to hardware checkout for the project`}></PositiveAlert>;
        }
        return (
            <div className="container">
                 <div className="card-wrapper">
                    <div class="card1">
                        <h3><strong>Welcome</strong> to your dashboard! {/*<strong>{this.props.location.state.email}!</strong>*/}</h3>
                        <form name="searchform" onSubmit={this.dashboard}>                       
                        <label className= "searchbar" for="searchid"><strong>Project ID</strong> </label>
                     
                        <input type="searchid" placeholder="Project ID" id="searchid"  class="field" required/>
                        <input type="password" placeholder="Password" id="searchpass"  class="field" required/>

                        {/* insert the alert initialized above */}
                        {alert}
                        <div class = "move">
                        <input type="submit" value="Submit" class="btn"/>
                        {/* if project was found, display ID and let them know it was found */}
                        <p style={{whiteSpace: "nowrap"}} ><strong>PROJECT ID: {this.state.searcher}</strong></p>
                         {positiveAlert}
                         </div>
                        </form>
                        {/* Routes to new project or back home after logging out */}
                        <button onClick={() => this.nextPath('/newproject')} class = "bigbtn" variant = "outline-primary">NEW PROJECT</button>
                        <button onClick={() => this.nextPath('/')} class = "btnLogout" variant = "outline-primary">Logout</button>
                    </div> 
                    
                </div>    
            </div>
        );
    };
    
    
}

export default Dashboard;