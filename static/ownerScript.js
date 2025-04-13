const logo = document.querySelector('.logo');
const container = document.querySelector('.container');

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function move() {
    await sleep(500);
    logo.classList.add('logoMove');
    container.classList.add('show');
}

move();