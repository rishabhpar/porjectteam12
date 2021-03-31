import React from "react";
import {Route, Redirect } from "react-router-dom";
import auth from "./auth";

// this component will take in a component like Dashboard
// it will show the Dashboard if the user is authenticated,
// else it reroutes to landing page.
const ProtectedRoute = ({component: Component, ...rest}) => {
    return (
        <Route {...rest} render={
            (props) => {
                if (auth.isAuthenticated()){
                    return <Component {...props} />;
                } else {
                    return <Redirect to={
                        {
                            pathname: '/',
                            state: {
                                from: props.location
                            }
                        }
                    } />
                }
                
            }
        }
        />
    );
};

export default ProtectedRoute;