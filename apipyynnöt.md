## verkkosivulta -> taustapalvelin:

pelaajan nimi ja id (
    pelaaja_nimi: string;
    id: string;
)

siirto (
    ICAO: string;
    teleport: boolean;
)

kauppa tapahtuma (
    teleportin_osto: boolean;
    poltto_aineen_oston_määrä: int;
)

## taustapalvelin -> verkkosivulle:

elämäpisteet (
    määrä: int;
)

polttoaine (
    määrä: int;
)

pistemäärä (
    määrä: int;
)

viholliset (
    siirtojen_määrä: int;
    tyyppi: string;
)

ostotapahtuma ok (
    teleport: boolean;
    polttoaine: int;
)

viisi lähintä lentokenttää (
    nimi: string;
    latitude: float;
    longitude: float;
    korkeus_metri: int;
    tyyppi: string;
    pilvisyys: float; (prosentti)
)