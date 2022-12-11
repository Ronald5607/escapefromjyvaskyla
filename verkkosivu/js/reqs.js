'use strict';


async function siirto(ICAO) {

    const siirto_dict = {'ICAO': ICAO};

    const vastaus = await fetch('http://127.0.0.1:3000/siirto?siirto=' + ICAO);

    const vastaus_json = await vastaus.json();
        
}
