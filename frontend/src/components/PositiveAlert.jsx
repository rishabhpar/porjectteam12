import React from "react";

function PositiveAlert(props) {
    return (
        <div
            className="w3-pale-green w3-text-green w3-border w3-border-green w3-round-large"
            style={{ padding: "1rem", marginTop: "1rem" }}>
            {props.message}
        </div>
    );
}

export default PositiveAlert;