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

let top5elementti = document.querySelector('.stoori ol');

top5().then((value) => {
    for (let highscore of value) {
        let jee = document.createElement('li');
        jee.innerText = highscore[0] + ': ' + highscore[1];
        top5elementti.appendChild(jee);   
}
})