// src/components/App.jsx
import React from "react";
import Home from "./Home";
import Login from "./Login";
import Register from "./Register";
import Dashboard from "./Dashboard";
// use the ProtectedRoute component as a wrapper for components
// that need to be password protected
import ProtectedRoute from "../protected_route";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
    return (
        <React.Fragment>
            {/* route the components to a link that can be referenced with href */}
            <Router>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/login" exact component={Login} />
                    <Route path="/register" exact component={Register} />
                    {/*<Route path="/dashboard" exact component={Dashboard} />*}
                    {/* the dashboard should not be viewable if user is not logged in */}
                    <ProtectedRoute path="/dashboard" exact component={Dashboard} />
                </Switch> 
            </Router>
        </React.Fragment>
    );
}

export default App;