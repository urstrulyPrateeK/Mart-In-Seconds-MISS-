function formatDate(date) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    const formattedDate = new Date(date).toLocaleDateString('en-US', options);
    return formattedDate.replace(/(\d+)(st|nd|rd|th)/, '$1');
}

const today = new Date();
const formattedDate = formatDate(today);
console.log(formattedDate);

const date = document.getElementById("date");
date.innerHTML = "Date: " + formattedDate;

var href = "";

function generateInvoice(store) {
    const name = document.getElementById("nameInp").value;
    const mobile = document.getElementById("mobileInp").value;

    var tds = document.getElementsByTagName("td");

    var q = "";
    var d = "";
    var total = tds[tds.length - 1].innerText.slice(3);

    for (let i = 0; i < tds.length - 2; i += 4) {
        q += tds[i].innerText + ",";
        d += tds[i + 1].innerText + ",";
    }

    var notification = document.createElement('div');
    notification.id = 'notification';
    notification.innerText = "Invoice generated successfully";
    notification.style.position = 'fixed';
    notification.style.bottom = '0';
    notification.style.right = '0';
    notification.style.backgroundColor = 'rgba(144, 238, 144, 0.6)'; // lightgreen with 60% opacity
    notification.style.padding = '10px';
    notification.style.borderRadius = '25px'; // pill shape
    document.body.appendChild(notification);

    document.getElementById('printBtn').disabled = false;

    console.log(`generateInvoice called with: ${store}, ${name}, ${mobile}, ${q}, ${d}, ${total}`);

    q = q.slice(0, -1);
    d = d.slice(0, -1);
    href = "/genInvoice/" + store + "/" + name + "/" + mobile + "/" + q + "/" + d + "/" + total;
}

document.getElementById('printBtn').addEventListener('click', function() {
    var notification = document.getElementById('notification');
    var generateInvoiceButton = document.getElementById('generateInvoice');
    var printButton = document.getElementById('printInvoice');

    if (notification) {
        notification.classList.add('hide-for-print');
    }
    if (generateInvoiceButton) {
        generateInvoiceButton.classList.add('hide-for-print');
    }
    if (printButton) {
        printButton.classList.add('hide-for-print');
    }

    setTimeout(function() {
        html2canvas(document.body, {
            width: document.body.scrollWidth,
            height: document.body.scrollHeight
        }).then(function(canvas) {
            var link = document.createElement('a');
            link.href = canvas.toDataURL('image/png');

            window.location.href = href;
        });
    }, 2000);
});