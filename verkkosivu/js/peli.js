'use strict';

const lentokone = new Airplane('kuvat/sus-plane-top.png', ctx, map);
let ID = 0;
let hp = 3;
let polttoaine = 100;
let pisteet = 0;
let kaydyt = ['EFJY'];
let kaydytlayer = [];
kaydytlayer = L.layerGroup(kaydytlayer);
let lahimmatlayer = 0;
let lahimmatlentokentat = [];
let vanha_sijainti = [62.4034, 25.6810];

function stringifykaydyt(kaydyt) {
  return kaydyt.reduce((a, b) => {return a + ',' + b})
}

const alustus = alotus();
alustus.then((value) => {
  ID = value.ID;
  lahimmatlentokentat = value.lahimmat;
  lahimmatlayer = lentokentta_layer(value.lahimmat);
  lahimmatlayer.addTo(map);
})



const aa = () => {
  const uusi_sijainti = [61.856, 24.7867];
  lentokone.lat = uusi_sijainti[0];
  lentokone.lon = uusi_sijainti[1];
  const uusi_icao = 'EFHA';
    const lentokentat = siirto(uusi_icao, ID, stringifykaydyt(kaydyt));
    lentokentat.then((value) => {
      pisteet = value.pisteet;
      polttoaine = value.polttoaine;
      hp = value.hp;

      polttis.innerText = `Polttoaine: ${polttoaine}%`;
      document.querySelector("#polttoaine").appendChild(polttis);

      kaydyt = kaydyt_lentokentat_array(uusi_icao, kaydyt);
      kaydytlayer = kaydyt_lentokentat(vanha_sijainti, kaydytlayer);
      kaydytlayer.addTo(map);
      vanha_sijainti = uusi_sijainti;

    lahimmatlayer.remove();
    lahimmatlayer = lentokentta_layer(value.lahimmat);
    lahimmatlayer.addTo(map);
    console.log(lahimmatlayer.getLayers())

})
}

aa()




lentokone.initairplane();
map.addEventListener('move',() => { lentokone.setcanvascoordinates(); });

window.requestAnimationFrame(() => {lentokone.draw()});




