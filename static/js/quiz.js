function processData(data)
{
    console.log(data);
}


document.getElementById("f").addEventListener("submit", (evt) => {
    console.log("Hello World");
    evt.preventDefault();

    let inputs = document.getElementsByTagName("input");
    let result = 3;
    
    for (let i = 0; i < inputs.length; i++)
    {
        switch (inputs[i].type) {
            case "radio":
                console.log("Radio", inputs[i].checked);
                if (inputs[i].checked)
                    result *= 1.5;
                break;



            case "checkbox":
                console.log("check", inputs[i].checked);
                if (inputs[i].checked)
                    result *= 2.2;
                break;



            case "text":
                console.log("text", inputs[i].value);
                if (inputs[i].value.length != 0)
                    result *= inputs[i].value.length;
                break;



            case "number":
                console.log("number", inputs[i].value);
                if (inputs[i].checked)
                    result *= inputs[i].value;
                break;

            default:
                break;
        }

    }
    
    console.log(result);
    result = result % parseInt(document.getElementById("pizza_amount").innerHTML);
    
    console.log(result);

    fetch(`/en/quiz/get_pizza/?id=${parseInt(result)}`)
    .then(response => response.json())
    .then(data => { processData(data); })
    .catch(error => { console.error("Error: ", error); });
    return 0;
});
