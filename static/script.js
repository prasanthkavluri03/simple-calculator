// Welcome Message
console.log("Simple Calculator Loaded Successfully");

// Button Animation
const button = document.querySelector("button");

button.addEventListener("click", function(){

    button.innerHTML="Calculating...";

    setTimeout(function(){

        button.innerHTML="Calculate";

    },800);

});