'use strict';

const lentokone = new Airplane('kuvat/sus-plane-top.png', ctx, map);



const lentokentat = siirto('EFJY', 1, 'EFHK');
lentokentat.then((value) => {
  
  const layeri = lentokentta_layer(value.lahimmat);
  layeri.addTo(map);
})




lentokone.initairplane();
map.addEventListener('move',() => { lentokone.setcanvascoordinates(); });

window.requestAnimationFrame(() => {lentokone.draw()});


//sydämet screenillä
const lives = 2; //täs kuuluis olla se kun se hakee pelaajan elämät (numero) databasest?
for (let i=0; i<lives; i++) {
  const life = document.createElement("p");
  life.innerHTML = "<img src='/verkkosivu/kuvat/life.png' alt='nolife' >"
  document.querySelector("#hp").appendChild(life);
}
const noLives=3-lives
for (let i=0; i<noLives; i++) {
  const nolife = document.createElement("p");
  nolife.innerHTML = "<img src='/verkkosivu/kuvat/nolife.png' alt='nolife' >"
  document.querySelector("#hp").appendChild(nolife);
}


