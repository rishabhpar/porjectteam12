// src/components/Hardware.jsx
import React, { Component, useEffect, useState } from "react";
import {Button} from "reactstrap";
import './style.css';
import Alert from "./Alert";
import axios from "axios";
import auth from "../auth";
import { config } from './Constants';


class Hardware extends Component{

    constructor(props) {
        super(props);
        console.log("IN CONSTRUCTOR")
        this.initializeSearchid()
        console.log(this.props)
        if(this.state == undefined || this.state.searchid == undefined) {
            this.state = {
                used1: '234',
                used2:'123',
                cap1: '345',
                cap2:'456',
                hw: {},
                searchid: this.searchid
            }
        } else {
            this.state = {
                used1: '234',
                used2:'123',
                cap1: '345',
                cap2:'456',
                hw: {}
            }
        }
        
        

        this.handleHardwarePostRequest = this.handleHardwarePostRequest.bind(this);
    }
    setNum = 1
    url = 'http://127.0.0.1:5000/api/hardware?setNum=' + this.setNum

    initializeSearchid() {
        console.log(this.searchid)
        if(this.props.history.action == "PUSH"){
            this.searchid = this.props.location.state.searchid
        };
        
    }
    componentDidMount() {
        console.log("COMPONENT DID MOUNT")
        // this.hardwarePostRequest(0, 0, 0)
        axios.post(config.url.API_URL.concat("/api/hardware"), {
            // get the form data on submission and post to the server
            set1: 0,
            set2: 0,
            check: 0,
            id: this.state.searchid
        })
            .then(response => {
                const hw = response.data;
                this.setState({ hw }); 
                console.log(hw)
              //  console.log(JSON.stringify(this.id))
             //   console.log(JSON.stringify(response.data)) 
                       
            })
            .catch(() => {
                alert('error data not received')
            });
    }

    handleHardwarePostRequest(set1, set2, check) {
        axios.post(config.url.API_URL.concat("/api/hardware"), {
            // get the form data on submission and post to the server
            set1: set1,
            set2: set2,
            check: check,
            id: this.state.searchid
        })
            .then(response => {
                const hw = response.data;
                this.setState({ hw }); 
                
              //  console.log(JSON.stringify(this.id))
             //   console.log(JSON.stringify(response.data)) 
                       
            })
            .catch(() => {
                alert('error data not received')
            });
    }

    hardwarePostRequest = () => {
        this.hardwarePostRequest(
            document.getElementById("set1").value,
            document.getElementById("set2").value,
            document.getElementById("check").value
        );
    };

    searchid = '0';
    render(){
        console.log("RENDER")
        
        var divStyle = {
            color:'white'
        };
      
        // let checkin;
        // if ( < this.setNum) {
        //   alert = <Alert message={`Check in capacity reached, please try again`}></Alert>;
        // }
      //  let checkout;
       // checkout = <Alert message={`Check your form and try again! (${this.state.a})`}></Alert>;
        
        // {this.state.a.map((hi) => (
        //     <h1 style={divStyle}>{hi.setNum}</h1>
        //     ))}
        // {this.state.a.map((hi) => (
        //     <h1 style={divStyle}>{hi.setNum}</h1>
        //     ))}

      //  <div>{this.display(this.state.a)}</div>
    //  { this.state.hw.map(hws => <li>{hws.capacity}</li>)}

//     <a className='divStyle' href="/login">
//     <Button size="sm" id="set1" color="light">Set 1</Button>
// </a>
// <a className='divStyle' href="/register">
//     <Button  size="sm" id="set2" color="light">Set 2</Button>
// </a>


        return (
            <div className="container">
                <h1 class="center" style={divStyle}> <strong>Resource Management</strong></h1>
                <br></br><br></br>

                  <h1 style={divStyle}>For project ID: {this.state.searchid}</h1>
                    
                    <h1>Set 1 checked out: {this.state.hw.used1}     Set 1 capacity left: {this.state.hw.cap1}</h1>
                    <h1></h1>
                    <h1>Set 2 checked out: {this.state.hw.used2}     Set 2 capacity left: {this.state.hw.cap2}</h1>
                    <h1></h1>
                    <div class="right">
                    <form name="signup_form" onSubmit={this.hardwarePostRequest}>

                            <label for="set1" style={divStyle}>Set 1: </label>
                            <input type="set1" id="set1" class="field" required/>

                            <label for="set2" style={divStyle}>Set 2: </label>
                            <input type="set2" id="set2" class="field" required/>

                            <label for="check" style={divStyle}>Check In or Out</label>
                            <input type="check" id="check" class="field" required/>                            

                            <span>
                                <input type="submit" value="Submit" class="btn"/>
                                                 
                            </span>
                        </form>

                        </div>                        
                    
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

                    {/*LINK TO PHYSIONET PAGE*/}
                    <a className='divStyle' class = "btn-add" href="/dashboard">
                        <Button size="lg"  color="dark">ADD DATASET</Button>
                    </a>
                    <a className='divStyle' class = "btn-back" href="/dashboard">
                        <Button size="lg"  color="dark">Back</Button>
                    </a>
                

            </div>
        );
    }

}

export default Hardware;