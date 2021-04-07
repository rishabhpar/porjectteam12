import React from "react";

// This is a component that will communicate with users that 
// there is a successful processing of submitted data
// Prop: The message to communicate to user
function PositiveAlert(props) {
    return (
        <div
            className="w3-pale-green w3-text-green w3-border w3-border-green w3-round-large"
            style={{ padding: "1rem", marginTop: "1rem", whiteSpace: "nowrap", float: "left"}}>
            <span>{props.message}</span>
        </div>
    );
}

export default PositiveAlert;