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
  if (pos === 2180) {
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
  if (name.value==="" || name.value===null) {
    alert("Valitse itsellesi käyttäjänimi");
    event.preventDefault()
  }
  else {
    const dict_name = {'name': name.value};
    fetch('http://127.0.0.1:3000/name',
      {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify(dict_name),
      }).then(res => {
    if (res.ok) {
      return res.json();
    } else {
      alert('something is wrong');
    }
    }).then(jsonResponse => {
        console.log(jsonResponse);
      },
    ).catch((err) => console.error(err));
  }}) //noi sulut tossa on oudosti imo mut se valitti mulle niistä jos laitoin eri taval



