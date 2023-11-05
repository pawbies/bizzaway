let now = new Date();


let startTime = new Date();
startTime.setHours(10, 0, 0); //open from 10am to 9pm
let endTime = new Date();
endTime.setHours(22, 0, 0);

let orderlink = document.getElementById("orderlink");

if (now < startTime || now > endTime) {
    orderlink.addEventListener("click", (evt) => { evt.preventDefault(); });
    orderlink.classList.add("text-gray-600");
    orderlink.title = "Wir sind geschlossen!";
}
