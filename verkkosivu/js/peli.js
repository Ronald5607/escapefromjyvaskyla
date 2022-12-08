'use strict';

const lentokone = new Airplane('kuvat/lentsikka.png', ctx, map);

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
kaydyt.addTo(map);

lentokone.initairplane();

map.addEventListener('move',() => { lentokone.setcanvascoordinates(); });
lentokone.rotation = 0.5;
window.requestAnimationFrame(() => {lentokone.draw()});



