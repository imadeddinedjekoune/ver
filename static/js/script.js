let counterValue = 0;
const counterElement = document.getElementById('counter');

function increaseCounter() {
    counterValue++;
    counterElement.textContent = counterValue;
}


setInterval(increaseCounter, 100);