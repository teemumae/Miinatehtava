TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}
def sijainti_kentalla(x, y, leveys, korkeus):
    return sijainti

def tulosta_sijainti(sijainti):
    print(TULOSTUKSET[sijainti])

leveys = int(input("Anna kentän leveys: "))
korkeus = int(input("Anna kentän korkeus: "))

if leveys <= 0 or korkeus <= 0:
    print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua!")
else:
    x = int(input("Anna x-koordinaatti:  "))
    y = int(input("Anna y-koordinaatti:  "))
    sijainti = sijainti_kentalla(x, y, leveys, korkeus)
    tulosta_sijainti(sijainti)