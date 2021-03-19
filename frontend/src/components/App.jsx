// src/components/App.jsx
import React from "react";
import Home from "./Home";
import Login from "./Login";
import Register from "./Register";
import { BrowserRouter as Router, Route } from "react-router-dom";

function App() {
    return (
        <React.Fragment>
            <Router>
                <Route path="/" exact component={Home} />
                <Route path="/login" exact component={Login} />
                <Route path="/register" exact component={Register} />
            </Router>
        </React.Fragment>
    );
}

export default App;