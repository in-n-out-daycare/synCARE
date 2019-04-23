
function validateBottleForm () {
  const radios = document.getElementsByName('bottle_choice')
  let formValid = false

  let i = 0
  while (!formValid && i < radios.length) {
    if (radios[i].checked) formValid = true
    i++
  }
  if (!formValid) alert('Must choose a bottle option!')
  return formValid
}

function submitBottleForm () {
  if (validateBottleForm()) document.getElementById('bottle_form').submit()
}

function validateNurseForm () {
  const radios = document.getElementsByName('nurse_choice')
  let formValid = false

  let i = 0
  while (!formValid && i < radios.length) {
    if (radios[i].checked) formValid = true
    i++
  }
  if (!formValid) alert('Must choose a nurse option!')
  return formValid
}

function submitNurseForm () {
  if (validateNurseForm()) document.getElementById('nurse_form').submit()
}

function validateFoodForm () {
  const radios = document.getElementsByName('food_choice')
  let formValid = false

  let i = 0
  while (!formValid && i < radios.length) {
    if (radios[i].checked) formValid = true
    i++
  }
  if (!formValid) alert('Must choose a food option!')
  return formValid
}

function submitFoodForm () {
  if (validateFoodForm()) document.getElementById('food_form').submit()
}

function myBottleFunction () {
  document.getElementById('bottleChoices').classList.toggle('show')
}

function myNurseFunction () {
  document.getElementById('nurseChoices').classList.toggle('show')
}

function myLunchFunction () {
  document.getElementById('lunchChoices').classList.toggle('show')
}

function myDiaperFunction() {
    document.getElementById("diaperChoices").classList.toggle("show");
}

window.onclick = function(event) {
    
    if (!event.target.matches('.dropButton')) {
        
        var dropdowns = document.getElementsByClassName("dropdownContent");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
  }
}
