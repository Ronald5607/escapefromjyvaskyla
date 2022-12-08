const map = L.map('map');
map.setView([62.2426, 25.7473], 7);

const tiles = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
}).addTo(map);


function lentokentta_layer(lentokentat) {
    const lentokenttalayer = [];
    const punainen = new L.Icon({
        iconUrl: 'kuvat/punainenmarker.png',
        iconSize: [20, 20],
        iconAnchor: [10, 10]
    });
    for (let lentokentta of lentokentat) {
        const markkeri = L.marker([lentokentta.latitude, lentokentta.longitude], {
            icon:punainen
        });
        lentokenttalayer.push(markkeri);
    }
    return L.layerGroup(lentokenttalayer);
};

function kaydyt_lentokentat(sijainti, kaydyt) {
    const sininen = new L.Icon({
        iconUrl: 'kuvat/sininenmarker.png',
        iconSize: [20, 20],
        iconAnchor: [10, 10]
    });
    const kentat = kaydyt.getLayers();
    if (kentat.length > 0 && kentat.length > 9) kentat.shift();
    kentat.push(L.marker([sijainti.latitude, sijainti.longitude], {
        icon: sininen
    }));
    return L.layerGroup(kentat);
};

function piirra_lentokentat(lentokenttalayer, kaydyt) {

}