import React from "react";

// This is a component that will communicate with users that 
// there is an error with the processing of submitted data
// Prop: The message to communicate to user
function Alert(props) {
    return (
        <div
            className="w3-pale-red w3-text-red w3-border w3-border-red w3-round-large"
            style={{ padding: "1rem", marginTop: "1rem", whiteSpace: "nowrap", float: "left"}}>
            {props.message}
        </div>
    );
}

export default Alert;