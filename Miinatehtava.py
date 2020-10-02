TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}
def sijainti_kentalla(x, y, leveys, korkeus):
    leveys-=1
    korkeus-=1
    if x == 0 and y == 0:
        sijainti = "nurkassa"
    elif x == leveys and y == korkeus:
        sijainti = "nurkassa"
    elif x == 0 and y == korkeus:
        sijainti = "nurkassa"
    elif x == leveys and y == 0:
        sijainti = "nurkassa"
    elif x < 0 or y < 0:
        sijainti = "ulkona"
    elif x > leveys or y > korkeus:
        sijainti = "ulkona"
    elif x == 0 and y < korkeus and y >0:
        sijainti = "laidalla"
    elif y == 0 and x > 0 and x < leveys:
        sijainti = "laidalla"
    elif x == leveys and y > 0 and y < k:
        sijainti = "laidalla"
    elif y == korkeus and x > 0 and x < leveys:
        sijainti = "laidalla"
    else:
        sijainti = "keskellä"
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