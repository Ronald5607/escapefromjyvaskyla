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

  vihollisboxi(value.viholliset);

  tee_kentat(value.lahimmat);
  syd(3);

  for (let lahin of lahimmatlayer.getLayers()) {
    lahin.addEventListener('click', () => {
      for (let kentta of lahimmatlentokentat) {
        if (kentta.find(element => element === lahin.getLatLng().lat)){
          aa([kentta[2], kentta[3]], kentta[0]);
          map.panTo(lahin.getLatLng());
        };
      }
    })
  }
})



const aa = (sijainti, icao) => {
  const uusi_sijainti = sijainti;
  lentokone.lat = uusi_sijainti[0];
  lentokone.lon = uusi_sijainti[1];
  const uusi_icao = icao;
    const lentokentat = siirto(uusi_icao, ID, stringifykaydyt(kaydyt));
    lentokentat.then((value) => {
      pisteet = value.pisteet;
      polttoaine = value.polttoaine;
      hp = value.hp;
      if (hp <= 0 || polttoaine <= 0) {
        location.href = 'hävisit.html';
        return
      }
      syd(hp);

      polttis.innerText = `Polttoaine: ${polttoaine}%`;
      document.querySelector("#polttoaine").appendChild(polttis);

      points.innerText = `Pisteet: ${pisteet}`;
      document.querySelector("#pisteet").appendChild(points);



      kaydytlayer.remove();
      kaydyt = kaydyt_lentokentat_array(uusi_icao, kaydyt);
      kaydytlayer = kaydyt_lentokentat(vanha_sijainti, kaydytlayer);
      kaydytlayer.addTo(map);
      vanha_sijainti = uusi_sijainti;


    lahimmatlayer.remove();
    lahimmatlayer = lentokentta_layer(value.lahimmat);
    lahimmatlentokentat = value.lahimmat;
    lahimmatlayer.addTo(map);

    tee_kentat(value.lahimmat);
    vihollisboxi(value.viholliset);

    for (let lahin of lahimmatlayer.getLayers()) {
      lahin.addEventListener('click', () => {
        for (let kentta of lahimmatlentokentat) {
          if (kentta.find(element => element === lahin.getLatLng().lat)){
            aa([kentta[2], kentta[3]], kentta[0]);
            map.panTo(lahin.getLatLng());
          };
        }
      })
    }

})
}





lentokone.initairplane();
map.addEventListener('move',() => { lentokone.setcanvascoordinates(); });

window.requestAnimationFrame(() => {lentokone.draw()});




