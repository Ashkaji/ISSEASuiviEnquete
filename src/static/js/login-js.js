document.addEventListener('DOMContentLoaded', function() {
    // Define a function to check if the input fields are not null
    function checkInputs() {
       // Get the input elements
        let username = document.getElementById("username");
        let password = document.getElementById("password");
        // Get the values of the input fields
        let usernameValue = username.value.trim();
        let passwordValue = password.value.trim();

        // Return true if both values are not empty, false otherwise
        return usernameValue !== "" && passwordValue !== "";
    }

    // Get the button element
    let button = document.getElementById("login-button");

    // Define a function to move the button randomly
    function moveButton() {
        if (button.style.left === "50%") {
            button.style.left = "-50%";
        }
        else {
            button.style.left = "50%";
        }
    }

    // Add an event listener to the button mouseover event
    button.addEventListener("mouseover", function() {
        // Check if the input fields are not null
        if (!checkInputs()) {
            // If yes, move the button
            moveButton();
        }
    });
    // button.addEventListener('mouseout', function() {
    //     // Reset button position
    //     button.style.left= '0%';
    // });
});
