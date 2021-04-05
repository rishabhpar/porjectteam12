// src/components/Home.jsx
import React from "react";
import { Table } from 'reactstrap';
import './style.css';
import auth from "../auth";
import {Button} from "reactstrap";

var divStyle = {
    color:'white'
};

class Dashboard extends React.Component {
    render () {
        return (

            <div className="container">
                 <div className="card-wrapper">
                    <div class="card1">
                        <h3>Welcome to your dashboard!</h3>
                        <table striped bordered hover></table>
                        <thead>
                            <tr>
                            <th>Project Name</th>
                            <th>Description</th>
                            <th>Date Created</th>
                            </tr>
                        </thead>
                        <button class = "bigbtn" variant = "outline-primary">NEW PROJECT</button>
                    </div>
                </div>    
            </div>
        );
    };
    
    
}

export default Dashboard;