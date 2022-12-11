'use strict';


async function siirto(ICAO, id, kaydyt) {


    const vastaus = await fetch('http://127.0.0.1:8888/siirto?ICAO=' + ICAO + '&ID=' + id + '&kaydyt=' + kaydyt);

    return await vastaus.json();
        
}




