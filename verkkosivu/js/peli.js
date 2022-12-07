'use strict';

const map = L.map('map');
map.setView([62.2426, 25.7473], 7);

const tiles = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
}).addTo(map);

const gamecanvas = document.getElementById('canvas');
const ctx = gamecanvas.getContext('2d');

const img = document.createElement('img');


img.addEventListener("load", () => {
    ctx.drawImage(img, 0, 0);
});
img.addEventListener('error', (err) => {
    console.log(err);
});
img.setAttribute('src', 'js/lentsikka.png');


let center = map.getCenter();
let pixelorigin = map.getPixelOrigin();

let pxcenter = map.project(center);

console.log(center);
console.log(pixelorigin);
const x = pxcenter.x - pixelorigin.x
console.log(x);
ctx.clearRect(0, 0, 1000, 1000);
ctx.translate(x, 0);


function lentokentta_layer(lentokentat) {
    const lentokenttalayer = [];
    const punainen = new L.Icon({
        iconUrl: 'punainenmarker.png',
        iconSize: [20, 20],
        iconAnchor: [10, 10]
    });
    for (let lentokentta of lentokentat) {
        const markkeri = L.marker([parseFloat(lentokentta.latitude), parseFloat(lentokentta.longitude)], {
            icon:punainen
        });
        lentokenttalayer.push(markkeri);
    }
    return L.layerGroup(lentokenttalayer);
};

function kaydyt_lentokentat(sijainti, kaydyt) {
    const kentat = kaydyt.getLayers();
    if (kentat.length > 0 && kentat.length > 9) kentat.shift();
    kentat.push(L.marker([sijainti.latitude, sijainti.longitude]));
    return L.layerGroup(kentat);

}

function piirra_lentokentat(lentokenttalayer, kaydyt) {

}

const lentokentat = [
    {
        latitude: 62.2426,
        longitude: 25.7473
    }
]
let a = [
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    },
    {
        latitude: 62.2426,
        longitude: 25.7473
    }
]
const layeri = lentokentta_layer(a);
let kaydyt = layeri;
layeri.addTo(map);

kaydyt = kaydyt_lentokentat({latitude: 55, longitude: 43}, kaydyt);
console.log(kaydyt.getLayers());
