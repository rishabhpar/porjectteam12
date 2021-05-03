// src/components/Hardware.jsx
import React, { Component, useEffect, useState } from "react";
import {Button} from "reactstrap";
import './style.css';
import Alert from "./Alert";
import axios from "axios";
import auth from "../auth";
import { config } from './Constants';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faDownload } from '@fortawesome/free-solid-svg-icons'


class Hardware extends Component{

    state = {
        hw: [],
        err: ""
        }

    componentDidMount() {
         axios.post("https://hardwareresources12.herokuapp.com/api/hardware", {
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
              
            }
            })
        .catch(() => {
            alert('error data not received')
        });
    };

    
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
              
            }
            document.getElementById('set1').value='';
            document.getElementById('check1').value='';
            document.getElementById('set2').value='';
            document.getElementById('check2').value='';
            })
        .catch(() => {
            alert('error data not received')
        });
    };

    //method to push external paths
    nextPath(path) {
        this.props.history.push(path);
      };

    
    render(){

        var divStyle = {
            color:'white'
        };
      
        let alert;
        if (this.state.err !== "") {
          alert = <Alert message={`Check your form and try again! (${this.state.err})`}></Alert>;
        } 

        return (
            <div>
                <span class="below"><button  onClick={() => this.nextPath('/dashboard')} class = "btn" variant = "outline-primary">Back</button> </span>
                <span class = "belowR"><button onClick={() => this.nextPath('/')} class = "btn" variant = "outline-primary">Logout</button></span>
                <h1 class = "center" style={divStyle}> <strong>Resource Management</strong></h1>
                                        
                    <span class="right">
                    <form name="form" onSubmit={this.hardware}>

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
                        <input type="submit"  value="Submit" class="btn"/>
                        </span>

                    </form>
                    </span> 

                    <span class="left">                
                    <span><h1 style={divStyle}><strong>Project ID: {this.state.hw.projectid}</strong></h1></span>
                                        
                    <h1 style = {divStyle} for="file">Hardware Set 1</h1>
                    <progress id="file" height = '10px' value={this.state.hw.used1} max="100"> </progress>
                    <h5 style = {divStyle}><span>Used: {this.state.hw.used1}</span><span class = "cappos">Available: {this.state.hw.cap1}</span></h5>
                                        
                    <h1 style = {divStyle} for="file">Hardware Set 2</h1>
                    <progress id="file" height = '10px' value={this.state.hw.used2} max="100"> {this.state.hw.used2} </progress>
                    <h5 style = {divStyle}><span>Used: {this.state.hw.used2}</span><span class = "cappos">Available: {this.state.hw.cap2}</span></h5>
                    </span>

                    <br></br><br></br>
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
                                <td><a href="https://physionet.org/static/published-projects/adfecgdb/abdominal-and-direct-fetal-ecg-database-1.0.0.zip"> <FontAwesomeIcon icon={faDownload} /> Abdominal and Direct Fetal ECG Database</a></td>
                                <td>Multichannel fetal electrocardiogram recordings obtained from 5 different women in labor, between 38 and 41 weeks of gestation.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/aftdb/af-termination-challenge-database-1.0.0.zip"> <FontAwesomeIcon icon={faDownload} /> AF Termination Challenge Database</a></td>
                                <td>ECG recordings created for the Computers in Cardiology Challenge 2004, which focused on predicting spontaneous termination of atrial fibrillation.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/ahadb/aha-database-sample-excluded-record-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />AHA Database Sample Excluded Record</a></td>
                                <td>Two ECG signals that were excluded from the 1980 American Heart Association database.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/aami-ec13/ansiaami-ec13-test-waveforms-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />ANSI/AAMI EC13 Test Waveforms</a></td>
                                <td>The files in this set can be used for testing a variety of devices that monitor the electrocardiogram. The recordings include both synthetic and real waveforms.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/apnea-ecg/apnea-ecg-database-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />Apnea-ECG Database</a></td>
                                <td>Seventy ECG signals with expert-labelled apnea annotations and machine-generated QRS annotations.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/pmd/a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />A Pressure Map Dataset for In-bed Posture Classification</a></td>
                                <td>Pressure sensor data captured from 13 participants in various sleeping postures.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/chfdb/bidmc-congestive-heart-failure-database-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />BIDMC Congestive Heart Failure Database</a></td>
                                <td>Long-term ECG recordings from 15 subjects with severe congestive heart failure.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/bidmc/bidmc-ppg-and-respiration-dataset-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />BIDMC PPG and Respiration Dataset</a></td>
                                <td>ECG signals extracted from the MIMIC-II Matched Waveform Database, with manual breath annotations added by annotators using impedance respiratory signal.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/bpssrat/blood-pressure-in-salt-sensitive-dahl-rats-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />Blood Pressure in Salt-Sensitive Dahl Rats</a></td>
                                <td>This database contains continuous blood pressure recordings for 9 Dahl SS rats and 6 Dahl SS.13BN rats, under high and low salt conditions.</td>
                            </tr>
                            <tr>
                                <td><a href="https://physionet.org/static/published-projects/body-sway-music-vr/body-sway-when-standing-and-listening-to-music-modified-to-reinforce-virtual-reality-environment-motion-1.0.0.zip"><FontAwesomeIcon icon={faDownload} />Body Sway When Standing and Listening to Music Modified to Reinforce Virtual Reality Environment Motion</a></td>
                                <td>This data were intended to show that music manipulated to match VR motion provided by an Oculus Rift head mounted display increased body sway when standing still.</td>
                            </tr>
                        </tbody>
                    </table>      

                    </div>
                    <br></br>  

            </div>
        );
    }

}

export default Hardware;