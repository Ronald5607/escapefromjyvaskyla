//sydämet screenillä
function syd(hp) {
  const lives = hp; //täs kuuluis olla se kun se hakee pelaajan elämät (numero) databasest?
  document.getElementById('hp').innerHTML = '';
  for (let i=0; i<lives; i++) {
    const life = document.createElement("p");
    life.innerHTML = "<img src='kuvat/life.png' alt='nolife' >"
    document.querySelector("#hp").appendChild(life);
  }
  const noLives=3-lives
  for (let i=0; i<noLives; i++) {
    const nolife = document.createElement("p");
    nolife.innerHTML = "<img src='kuvat/nolife.png' alt='nolife' >"
    document.querySelector("#hp").appendChild(nolife);
  }
}

//vihut
//for vihollinen in viholliset diibadaaba
function vihollisboxi(viholliset) {
  document.getElementById('viholliset').innerHTML = '';
  for (let vihulainen of viholliset) {
    let vihollinen = document.createElement("div");
    let nimi = document.createElement("h2");
    nimi.innerText = vihulainen[0]; //vihun nimi
    let kuva = document.createElement("img");
    kuva.src = "kuvat/life.png";
    //kuva.alt = vihun nimi;
    let siirrot = document.createElement("p");
    siirrot.innerText = vihulainen[1]; //siirrot
    vihollinen.appendChild(nimi);
    vihollinen.appendChild(kuva);
    vihollinen.appendChild(siirrot);
    const tyyppi = "iceman"; //hakee tyypin
    vihollinen.classList.add(tyyppi);
    document.querySelector("#viholliset").appendChild(vihollinen);
  }
}
//pisteet
const pistemaara = 0; //hae pisteet
const points = document.createElement("p");
points.innerText = `Pisteet: ${pistemaara}`;
document.querySelector("#pisteet").appendChild(points);

//polttoaine
const prosentti = 100;//tähän polttoaineen hakeminen (muuttuja prosentti)
const polttis = document.createElement("p");
polttis.innerText = `Polttoaine: ${prosentti}%`;
document.querySelector("#polttoaine").appendChild(polttis);

//vaihetaa noi myöhemmin ne on taas placeholders
function tee_kentat(kentat) {
  document.getElementById('airports').innerHTML = '';
  let i = 0;
  kentat.forEach(function(kentta) {
    const airport = document.createElement('div');
    airport.setAttribute('id', i);
    const nimi = document.createElement('p');
    const latitude = document.createElement('p');
    latitude.setAttribute('id', i+10);
    const longitude = document.createElement('p');
    const elevation = document.createElement('p');
    const pilvisyys = document.createElement('p');
    nimi.innerText = `Nimi: ${kentta[1]}`;
    latitude.innerText = `Latitude: ${kentta[2]}`;
    longitude.innerText = `Longitude: ${kentta[3]}`;
    elevation.innerText = `Elevation: ${kentta[7]}`;
    pilvisyys.innerText = `Pilvisyys: ${kentta[6]}`;
    airport.appendChild(nimi);
    airport.appendChild(latitude);
    airport.appendChild(longitude);
    airport.appendChild(elevation);
    airport.appendChild(pilvisyys);
    document.querySelector("#airports").appendChild(airport);
    i++;
  })
}