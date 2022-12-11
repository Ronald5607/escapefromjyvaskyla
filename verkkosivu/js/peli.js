'use strict';

const lentokone = new Airplane('kuvat/sus-plane-top.png', ctx, map);

const lentokentat = [
    {
        latitude: 62.2426,
        longitude: 25.7473
    }
]

const layeri = lentokentta_layer(lentokentat);
let kaydyt = layeri;
layeri.addTo(map);

kaydyt = kaydyt_lentokentat({latitude: 55, longitude: 43}, kaydyt);
for (let kayty of kaydyt.getLayers()) {
    kayty.addEventListener('mouseover', () => {
        const latlon = kayty.getLatLng();
        const direction = -Math.atan2(lentokone.lon - latlon.lng, lentokone.lat - latlon.lat);
        lentokone.rotation = direction;
    });
}
kaydyt.addTo(map);

lentokone.initairplane();

map.addEventListener('move',() => { lentokone.setcanvascoordinates(); });
lentokone.rotation = 2;
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


