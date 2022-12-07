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
