// src/components/Hardware.jsx
import React, { Component, useEffect, useState } from "react";
import {Button} from "reactstrap";
import './style.css';
import Alert from "./Alert";
import axios from "axios";
import auth from "../auth";
import { config } from './Constants';


class Hardware extends Component{

    state = {
        hw: [],
        err: ""
        }
    
    hardware = (e) => {
        e.preventDefault();
         axios.post(config.url.API_URL.concat("/api/hardware"), {
            // get the form data on submission and post to the server
            set1: document.getElementById("set1").value,
            set2: document.getElementById("set2").value,
            check1: document.getElementById("check1").value,
            check2: document.getElementById("check2").value,
            id: this.props.location.state.searchid
        })
        .then((res) => {
            if (res.data.error) {
                // if there is an error, update err with message
                // and internally communicate that the registration failed
                this.setState({ err: res.data.error });
                this.setState({ hardware: false });
            } else {
                // else, clear err message
                // and internally communicate that the registration succeeded
                this.setState({ hardware: true });
                this.setState({ err: "" });
                const hw = res.data;
                this.setState({ hw });  
              
            }})
            // .then(response => {
            //     const hw = response.data;
            //     this.setState({ hw }); 
            //   //  console.log(JSON.stringify(this.id))
            //  //   console.log(JSON.stringify(response.data)) 
            //     console.log(hw)             
            // })
        .catch(() => {
            alert('error data not received')
        });
    };

    nextPath() {
        auth.login(() => {
            this.props.history.push({
                pathname: "/dashboard",
            });
        })
        }
    
    render(){
        console.log("RENDER")
        
        var divStyle = {
            color:'white'
        };
      
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        return (
            <div>
                <h1 class = "center" style={divStyle}> <strong>Resource Management</strong></h1>
                <br></br>
                   
                    <div class="right">
                    <p style={divStyle}>To view hardware availability in current state, press "submit"</p>
                    <form name="signup_form" onSubmit={this.hardware}>

                        <label for="set1" style={divStyle}>Set 1 Request #: </label>
                        <input type="set1" id="set1" class="field" />

                        <label for="check1" style={divStyle}>Check "In"/"Out" </label>
                        <input type="check1" id="check1" class="field" />

                        <label for="set2" style={divStyle}>Set 2 Request #: </label>
                        <input type="set2" id="set2" class="field" />

                        <label for="check2" style={divStyle}>Check "In"/"Out" </label>
                        <input type="check2" id="check2" class="field" />                            
                        {alert}
                        <span>
                            <input type="submit" value="Submit" class="btn"/>
                                                
                        </span>
                    </form>

                    </div>                 
                    <h1 style={divStyle}>For project ID: {this.state.hw.projectid}</h1>
                    
                    <h1 style={divStyle}>Set 1 checked out: {this.state.hw.used1} | Set 1 capacity left: {this.state.hw.cap1}</h1>
                   
                    <h1 style={divStyle}>Set 2 checked out: {this.state.hw.used2} | Set 2 capacity left: {this.state.hw.cap2}</h1>       
                    
                    <p style = {divStyle}>----------------------------------------------------------------------------------------------------------------</p>
                    <p>*Area below to be completed for checkpoint 3</p>
                    <h1 style = {divStyle}>Hardware Set 1</h1>
                    <div class="bar">
                        <section id="occupied" style={{width: '20%'}}>20</section>
                        <section id="personal" style={{width: '50%'}}>50</section>
                        <section id="available" style={{width: '30%'}}>30</section>
                    </div>
                    <br></br><br></br>
                    <h1 style = {divStyle}>Hardware Set 2</h1>
                    <div class="bar">
                        <section id="occupied" style={{width: '20%'}}>20</section>
                        <section id="personal" style={{width: '50%'}}>50</section>
                        <section id="available" style={{width: '30%'}}>30</section>
                    </div>          
                    <br></br><br></br>

                    <div>
                    <h1 style = {divStyle} class = "center"><strong>Download Dataset from PhysioNet</strong></h1>

                    <table class="hoverTable">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Link</td>
                                <td>words</td>
                            </tr>
                            <tr>
                                <td>Link</td>
                                <td>words</td>
                            </tr>
                            <tr>
                                <td>Link</td>
                                <td>words</td>
                            </tr>
                        </tbody>
                    </table>      

                    </div>
                    <br></br>
                    <button onClick={() => this.nextPath()} class = "btn" variant = "outline-primary">Back</button>                             

            </div>
        );
    }

}

export default Hardware;