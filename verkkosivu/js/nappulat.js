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
siirrot.innerText = 4 //siirrot
vihollinen.appendChild(nimi);
vihollinen.appendChild(kuva);
vihollinen.appendChild(siirrot);
const tyyppi = "iceman"; //hakee tyypin
vihollinen.classList.add(tyyppi);
document.querySelector("#viholliset").appendChild(vihollinen);

