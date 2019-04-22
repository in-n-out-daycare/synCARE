

function validateBottleForm() {
    const radios = document.getElementsByName("bottle_choice");
    let formValid = false;

    let i = 0;
    while (!formValid && i <radios.length) {
        if (radios[i].checked) formValid = true;
        i++;
    }
    if (!formValid) alert("Must choose a bottle option!");
    return formValid;
}

function submitBottleForm() {
    if (validateBottleForm()) document.getElementById("bottle_form").submit();
}
