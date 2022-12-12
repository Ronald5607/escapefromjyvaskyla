//sydämet screenillä
const lives = 3; //täs kuuluis olla se kun se hakee pelaajan elämät (numero) databasest?
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

//vihut
//for vihollinen in viholliset diibadaaba
vihollinen = document.createElement("div");
let nimi = document.createElement("h2");
nimi.innerText = "jäämies"; //vihun nimi
let kuva = document.createElement("img");
kuva.src = "kuvat/life.png";
//kuva.alt = vihun nimi;
let siirrot = document.createElement("p");
siirrot.innerText = "4"; //siirrot
vihollinen.appendChild(nimi);
vihollinen.appendChild(kuva);
vihollinen.appendChild(siirrot);
const tyyppi = "iceman"; //hakee tyypin
vihollinen.classList.add(tyyppi);
document.querySelector("#viholliset").appendChild(vihollinen);

//pisteet
/*const pistemaara = 200; //hae pisteet
const points = document.createElement("p");
points.innerText = `Polttoaine: ${pistemaara}%`;
document.querySelector("#pisteet").appendChild(points);*/

//polttoaine
const prosentti = 100;//tähän polttoaineen hakeminen (muuttuja prosentti)
const polttis = document.createElement("p");
polttis.innerText = `Polttoaine: ${prosentti}%`;
document.querySelector("#polttoaine").appendChild(polttis);

//vaihetaa noi myöhemmin ne on taas placeholders
const kentat = [["nimisdfsdfsfd", "icao", "pilvisyys"], ["nimi2", "icao2", "pilvisyys2"],["skdjfskjfksjdkkfjksdfksjksjdfkjsk djfskjfksdjfj dfjdkfjdk", "icaosdfsdfsd3", "pilvisyys3"],["nimi4", "icao4", "pilvisyys4"],["nisdfsdfsfsdfd dsdf ddkskfjdsjfkjskfjmi5", "icao5", "pilvisyys5"]]
kentat.forEach(function(kentta) {
  const airport = document.createElement('div');
  const nimi = document.createElement('p');
  const latitude = document.createElement('p');
  const longitude = document.createElement('p');
  const elevation = document.createElement('p');
  const pilvisyys = document.createElement('p');
  nimi.innerText = `Nimi: ${kentta[0]}`;
  latitude.innerText = `Latitude: ${kentta[1]}`;
  longitude.innerText = `Longitude: ${kentta[1]}`;
  elevation.innerText = `Elevation: ${kentta[2]}`;
  pilvisyys.innerText = `Pilvisyys: ${kentta[2]}`;
  airport.appendChild(nimi);
  airport.appendChild(latitude);
  airport.appendChild(longitude);
  airport.appendChild(elevation);
  airport.appendChild(pilvisyys);
  document.querySelector("#airports").appendChild(airport);
})