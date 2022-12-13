'use strict';

const btn = document.querySelector('.ei');
btn.addEventListener('click', function() {
  alert('nössö');
});

let id = null;
const elem = document.querySelector('.animation');
let pos = -200;
clearInterval(id);
id = setInterval(frame, 1);

function frame() {
  if (pos === window.innerWidth) {
    pos = -200;
  } else {
    pos++;
    elem.style.left = pos + 'px';
  }
}

// lähettää formiin laitetun nimen json pakettina pythonille
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  const name = document.querySelector('input[type=text]');
  if (name.value === '' || name.value === null) {
    alert('Valitse itsellesi käyttäjänimi');
    event.preventDefault();
  }
  else if (name.value.length>20) {
    alert(`Käyttäjänimi on ${name.value.length-20} merkkiä liian pitkä (20 on maksimi)`);
    event.preventDefault();
  }
  else {
    let result = confirm(`Oletko valmis, ${name.value}?`);
    if (result === false) {
      alert('nössö');
      event.preventDefault();
    } else {
      
    }
  }
});



