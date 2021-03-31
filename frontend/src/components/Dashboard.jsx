// src/components/Home.jsx
import React from "react";
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
                <div className="main">
                    <h1 style={divStyle}> <strong>Welcome</strong> {this.props.location.state.email} 👋</h1>
                    <br/>
                    <br/>
                    <div>
                        <Button size="lg"  color="light" onClick={() => {
                            auth.logout(() => {
                                this.props.history.push("/");
                            })
                        }}>Log Out</Button>     
                    </div>
    
                </div>
            </div>
        );
    };
    
    
}

export default Dashboard;