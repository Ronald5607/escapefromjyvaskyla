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
        iconSize: [30, 30],
        iconAnchor: [15, 15]
    });
    for (let lentokentta of lentokentat) {
        const markkeri = L.marker([lentokentta[2], lentokentta[3]], {
            icon:punainen
        });
        lentokenttalayer.push(markkeri);
    }
    for (let kayty of lentokenttalayer) {
        kayty.addEventListener('mouseout', () => {
            for (let i = 0; i < 5; i++) {
                const element = document.getElementById(i);
                element.style.backgroundColor = 'rgb(24, 37, 41)';
                element.style.color = 'aliceblue';
            }
        })

        kayty.addEventListener('mouseover', () => {
            const latlon = kayty.getLatLng();
            const markercoords = map.latLngToContainerPoint(latlon);
            const airplanecoords = map.latLngToContainerPoint([lentokone.lat, lentokone.lon]);
            const direction = Math.atan2(airplanecoords.y - markercoords.y, airplanecoords.x - markercoords.x) + 3.14;
            lentokone.rotation = direction;

            for (let i = 0; i < 5; i++) {
                let latitude = document.getElementById(i+10).innerText;
                latitude = parseFloat(latitude.split(' ')[1]);
                if (kayty.getLatLng().lat === latitude) {
                    const element = document.getElementById(i);
                    element.style.backgroundColor = 'aliceblue';
                    element.style.color = 'rgb(24, 37, 41)';

                }

                
            }
        });
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
    if (kentat.length > 9) kentat.shift();
    const markkeri = L.marker([sijainti[0], sijainti[1]], {
        icon: sininen
    });
    kentat.push(markkeri);
    return L.layerGroup(kentat);
};

function kaydyt_lentokentat_array(sijainti, kaydyt) {
    if (kaydyt.length > 9) kaydyt.shift();
    kaydyt.push(sijainti);
    return kaydyt
}
