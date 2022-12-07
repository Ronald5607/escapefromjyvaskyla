'use strict';

const btn = document.querySelector('.ei');
btn.addEventListener('click', function() {
  alert('nössö');
});

let id = null;
const elem = document.querySelector('.animation');
let pos = -300;
clearInterval(id);
id = setInterval(frame, 5);
function frame() {
  if (pos === 3000) {
    clearInterval(id);
  } else {
    pos++;
    elem.style.left = pos + 'px';
  }
}

// lähettää formiin laitetun nimen json pakettina pythonille
const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
  const name = document.querySelector('input[type=text]');
  const dict_name = {"name": name.value};
  alert(name.value);
  fetch("http://127.0.0.1:3000/name",
  {
  method: 'POST',
  headers: {
  'Content-type': 'application/json',
  'Accept': 'application/json'
  },
  body:JSON.stringify(dict_name)}).then(res=>{
  if(res.ok){
  return res.json()
  }else{
  alert("something is wrong")
  }
  }).then(jsonResponse=>{
  console.log(jsonResponse)
  }
  ).catch((err) => console.error(err));
})

