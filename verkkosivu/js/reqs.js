'use strict';


async function siirto(ICAO, id, kaydyt) {


    const vastaus = await fetch('http://127.0.0.1:8888/siirto?ICAO=' + ICAO + '&ID=' + id + '&kaydyt=' + kaydyt);

    return await vastaus.json();
        
}


async function alotus() {
    const querystr = window.location.search;
    const params = new URLSearchParams(querystr);
    const name = params.get('screen_name');
    const vastaus = await fetch('http://127.0.0.1:8888/name?name=' + name)

    return await vastaus.json();
}




