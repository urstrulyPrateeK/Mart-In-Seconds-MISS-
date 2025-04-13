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

const menuIcon = document.getElementById('menuIcon');
const sidebar = document.getElementById('sidebar');

menuIcon.addEventListener('click', function() {
    sidebar.classList.toggle('active');
});

document.addEventListener('click', function(event) {
    if (event.target.id !== 'menuIcon' && event.target.id !== 'sidebar') {
        sidebar.classList.remove('active');
    }
});

window.onload = function() {
    setTimeout(function() {
        document.querySelector('.logo').classList.add('logoMove');
    }, 2000); // Adjust this delay as needed

    setTimeout(function() {
        document.querySelector('.main-content').classList.add('show');
        document.querySelector('#sidebar a').classList.add('show');
    }, 2005); // Adjust this delay as needed
}