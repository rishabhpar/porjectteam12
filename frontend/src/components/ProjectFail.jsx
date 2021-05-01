import React from "react";

// This is a component that will communicate with users that 
// there is a successful processing of submitted data
// Prop: The message to communicate to user
function ProjectFail(props) {
    return (
        <div
            className="w3-pale-red w3-text-red w3-border w3-border-red w3-round-large"
            style={{ padding: "1rem", marginTop: "1rem", position:"absolute",right:"700px",top:"450px", whiteSpace: "nowrap", float: "left"}}>
            <span>{props.message}</span>
        </div>
    );
}

export default ProjectFail;