
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
  if (validatenurseForm()) document.getElementById('nurse_form').submit()
}

function validateLunchForm () {
  const radios = document.getElementsByName('lunch_choice')
  let formValid = false

  let i = 0
  while (!formValid && i < radios.length) {
    if (radios[i].checked) formValid = true
    i++
  }
  if (!formValid) alert('Must choose a lunch option!')
  return formValid
}

function submitLunchForm () {
  if (validatelunchForm()) document.getElementById('lunch_form').submit()
}
