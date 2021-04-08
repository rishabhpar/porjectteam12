// src/components/Hardware.jsx
import React, { Component, useEffect, useState } from "react";
import {Button} from "reactstrap";
import './style.css';
import Alert from "./Alert";
import axios from "axios";
import auth from "../auth";


class Hardware extends Component{

    state = {
        hw: []
    }
    setNum = 1
    url = 'http://127.0.0.1:5000/api/hardware?setNum=' + this.setNum

    componentDidMount(){
        //this.getHardware(1)
        axios.post(this.url, {
                setNum: '1',
                capacity: '2',
                totalUsed: '2',
        })
            .then(response => {
                const hw = response.data;
                this.setState({ hw });  
              
            })
            .catch(() => {
                alert('error data not received')
            });
    };

    getHardware = (setNum) => {
        axios.post('http://127.0.0.1:5000/api/hardware?', { params: { setNum: this.setNum}})
            .then(response => {
                const hw = response.data;
                this.setState({ hw });  
             //   this.setState({ a: response.data });
               // console.log(this.state.a) 
                                 
            })
            .catch(() => {
                alert('error data not received')
            });
    }

    // display = (a) => {
    //     return a.map((hw) => 
    //     <div>
    //         <h3>{hw.capacity}</h3>
    //     </div>)
    // }


    render(){
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

        let set1;
        this.setNum = 1
        
        let set2;
        this.setNum = 2

        return (
            <div className="container">
                <h1 class="center" style={divStyle}> <strong>Resource Management</strong></h1>
                <br></br><br></br>
                  <h1>{this.state.hw.setNum}</h1>
                    <div class = "right">
                        
                        {/* create the form and set the onSubmit task to be check in and out */}

                        <form name="request1" >
                            <h4 style = {divStyle} >Request: </h4>
                            <input type="text" id="request" class="field" />
                        </form>
                        {/*FIX BUTTON LINKS*/}
                        <a className='divStyle' href="/login">
                            <Button size="sm" id="in" color="light">Check In</Button>
                        </a>
                        <a className='divStyle' href="/register">
                            <Button  size="sm" id="out" color="light">Check Out</Button>
                        </a>
                    </div>
                    <div class="right">
                    <form name="signup_form" onSubmit={this.componentDidMount}>

                            <label for="set">Set</label>
                            <input type="set" id="set" class="field" required/>

                            <label for="val">Request</label>
                            <input type="val" id="val" class="field" required/>

                            <label for="check">Checkin/out</label>
                            <input type="check" id="check" class="field" required/>                            

                            <span>
                                <input type="submit" value="Submit" class="btn"/>
                                                 
                            </span>
                        </form>

                        </div>

                        <h1>{this.state.hw.setNum}</h1>
                        <h1>{this.state.hw.capacity}</h1>
                        <h1>{this.state.hw.totalUsed}</h1>
                        
                    
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
                

            </div>
        );
    }

}

export default Hardware;