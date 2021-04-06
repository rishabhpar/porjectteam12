// src/components/Hardware.jsx
import React, { Component } from "react";
import {Button} from "reactstrap";
import './style.css';
import Alert from "./Alert";


var divStyle = {
    color:'white'
};


class Hardware extends Component {

    render(){
        // let checkin;
        // if ( < this.setNum) {
        //   alert = <Alert message={`Check in capacity reached, please try again`}></Alert>;
        // }
        // let checkout;
        // if (this.state.err !== "") {
        //   alert = <Alert message={`Checkout capacity reached, please try again`}></Alert>;
        // }

        return (
            <div className="container">
            
                    <h1 class="center" style={divStyle}> <strong>Resource Management</strong></h1>
                <br></br><br></br>
                    <div class = "right">
                        {/* create the form and set the onSubmit task to be check in and out */}
                        <form name="request" >
                            <h4 style = {divStyle} >Request: </h4>
                            <input type="text" id="request" class="field" />
                        </form>
                        {/*FIX BUTTON LINKS*/}
                        <a className='divStyle' href="/login">
                            <Button size="sm"  color="light">Check In</Button>
                        </a>
                        <a className='divStyle' href="/register">
                            <Button  size="sm"  color="light">Check Out</Button>
                        </a>
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
                    <div class = "right">
                        {/* create the form and set the onSubmit task to be check in and out */}
                        <form name="request" >
                            <h4 style = {divStyle} >Request: </h4>
                            <input type="text" id="request" class="field" />
                        </form>
                        {/*FIX BUTTON LINKS*/}
                        <a className='divStyle' href="/login">
                            <Button size="sm"  color="light">Check In</Button>
                            
                        </a>
                        <a className='divStyle' href="/register">
                            <Button  size="sm"  color="light">Check Out</Button>
                            
                        </a>
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