function toggle() {


var div = document.getElementById('parent2');
  if(this.checked) {
    div.style.display = 'block';
  } else {
    div.style.display = 'none';
    }
}
document.getElementById('parent2b').onchange = toggle;

function getKidForm() {
  var elem = document.getElementById('kid');
  elem.style.display = 'block';
}

document.getElementById('btn').onclick = getKidForm;