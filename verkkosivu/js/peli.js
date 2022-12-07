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
    console.log('loaded');
    ctx.drawImage(img, 0, 0);
});
img.addEventListener('error', (err) => {
    console.log(err);
});
img.setAttribute('src', 'js/lentsikka.png');

if (img.complete) {
    console.log('joo');
    ctx.drawImage(img, 0, 0)
};