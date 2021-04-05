// src/components/Home.jsx
import React from "react";
import './style.css';


var divStyle = {
    color:'white'
};

class Dashboard extends React.Component {
    nextPath(path) {
        this.props.history.push(path);
      }

    render () {
        return (
            <div className="container">
                 <div className="card-wrapper">
                    <div class="card1">
                        <h3><strong>Welcome</strong> to your dashboard{/*{this.props.location.state.name}*/}</h3>
                        <table striped bordered hover></table>
                        <thead>
                            <tr>
                            <th>Project Name</th>
                            <th>Description</th>
                            <th>Date Created</th>
                            </tr>
                        </thead>
                        <button onClick={() => this.nextPath('/newproject')} class = "bigbtn" variant = "outline-primary">NEW PROJECT</button>
                    </div>
                </div>    
            </div>
        );
    };
    
    
}

export default Dashboard;