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



