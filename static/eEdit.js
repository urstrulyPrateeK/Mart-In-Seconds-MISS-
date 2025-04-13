const inputs = document.getElementsByTagName("input");
var inputIds = "";
var inputVals = "";
var toggle = true;

for (let i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('input', (event) => restrictInput(event))
}

function restrictInput(event) {
    const inputValue = event.target.value;
    const numericValue = inputValue.replace(/[^0-9]/g, '');
    
    event.target.value = numericValue;
}

function addToDb(event) {
    inputIds += event.target.id + ",";
    inputVals += event.target.value === "" ? "0," : event.target.value + ",";

    console.log(inputIds, inputVals);
}

function submit() {
    inputIds = inputIds.slice(0, -1);
    inputVals = inputVals.slice(0, -1);

    console.log("/updateElectronics/" + inputIds + "/" + inputVals);
    window.location = "/updateElectronics/" + inputIds + "/" + inputVals;
}

function deleteToggle() {
    const tr = document.getElementById("tr");
    const trDel = document.getElementsByClassName("trDel");
    if (toggle) {
        tr.innerHTML = `<th class="del"></th>` + tr.innerHTML;

        for (let i of trDel) {
            i.innerHTML = `<td class="del"><span style="cursor:pointer;" class="material-symbols-outlined" onclick="deleteUser(event)">delete</span></td>` + i.innerHTML;
        }
        toggle = !toggle;
    } else {
        tr.removeChild(tr.firstChild);

        for (let i of trDel) {
            i.removeChild(i.firstChild);
        }
        toggle = !toggle;
    }
}

function deleteUser(event) {
    console.log(event.target.parentNode.nextElementSibling.innerText);
    window.location = "/deleteElectronics/" + event.target.parentNode.nextElementSibling.innerText;
}