'use strict';

const lentokone = new Airplane('kuvat/sus-plane-top.png', ctx, map);
let hp = 3;
let polttoaine = 100;
let pisteet = 0;
let kaydyt = ['EFJY'];
let kaydytlayer = [L.marker([62.4034, 25.6810])];
kaydytlayer = L.layerGroup(kaydytlayer);
let lahimmatlayer = 0;

function stringifykaydyt(kaydyt) {
  kaydyt.reduce((a, b) => {return a + ',' + b})
}

const alustus = alotus();
alustus.then((value) => {
  lahimmatlayer = lentokentta_layer(value.lahimmat);
  lahimmatlayer.addTo(map);
})

const aa = () => {
  const uusi_sijainti = 'EFHK';
    const lentokentat = siirto(uusi_sijainti, 1, stringifykaydyt(kaydyt));
    lentokentat.then((value) => {
    lahimmatlayer = lentokentta_layer(value.lahimmat);
    lahimmatlayer.addTo(map);

    kaydyt = kaydyt_lentokentat_array(uusi_sijainti, kaydyt);
    kaydytlayer = kaydyt_lentokentat(uusi_sijainti, kaydytlayer);
    kaydytlayer.addTo(map);
})
}

aa();




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


