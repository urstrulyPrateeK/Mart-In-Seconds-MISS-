const total = document.getElementById("total");

const plus = document.getElementsByClassName("plus");
const minus = document.getElementsByClassName("minus");

let cart = {};

for (let i = 0; i < plus.length; i++) {
    plus[i].addEventListener('click', (event) => plusFun(event));
}

for (let i = 0; i < minus.length; i++) {
    minus[i].addEventListener('click', (event) => minusFun(event));
}

function plusFun(event) {
    let q = parseInt(event.target.previousElementSibling.innerHTML);
    event.target.previousElementSibling.innerHTML = q + 1;
    total.innerHTML = parseInt(total.innerHTML) + 1;

    let v = event.target.parentElement.previousElementSibling.previousElementSibling.innerHTML.toLowerCase();
    if (v in cart) {
        cart[v] += 1;
    } else {
        cart[v] = 1;
    }

    console.log(cart);
}

function minusFun(event) {
    let q = parseInt(event.target.nextElementSibling.innerHTML);
    if (q != 0) {
        event.target.nextElementSibling.innerHTML = q - 1;
        total.innerHTML = parseInt(total.innerHTML) - 1;

        let v = event.target.parentElement.previousElementSibling.previousElementSibling.innerHTML.toLowerCase();
        if (v in cart) {
            cart[v] -= 1;
        }

        if (cart[v] === 0) {
            delete cart[v];
        }

        console.log(cart);
    }
}

function goToCart() {
    let items = "";
    let quants = "";
    for (var key in cart) {
        items += key.replace(" ", "_") + ",";
        quants += cart[key] + ",";
    }

    items = items.slice(0, -1);
    quants = quants.slice(0, -1);
    window.location = "/cart/v/" + items + "/" + quants;
}