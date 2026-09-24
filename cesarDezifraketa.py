from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def cesar_deszifratu(testua, desplazamendua):
    emaitza = ""
    for karaketere in testua:
        if karaketere.isalpha():
            # Letra maiuskulak eta minuskulak kudeatu
            oinarria = ord('A') if karaketere.isupper() else ord('a')
            # Desplazamendua aplikatu (atzera, deszifratzeko)
            berria = (ord(karaketere) - oinarria - desplazamendua) % 26 + oinarria
            emaitza += chr(berria)
        else:
            # Espazioak eta puntuazio-markak berdin mantendu
            emaitza += karaketere
    return emaitza

def indar_eraso_cesar(zifratutako_testua):
    print("Indar-erasoa hasi da gakoa bilatzeko...\n")
    
    # Letra-aldaketaren 26 aukerak probatu (Fuerza bruta)
    for gakoa in range(26):
        proba_testua = cesar_deszifratu(zifratutako_testua, gakoa)
        
        # Hizkuntza autodetektatzen saiatu
        try:
            hizkuntza = detect(proba_testua)
            if hizkuntza == 'es':
                print(f"¡Gakoa aurkitu da! -> Desplazamendua: {gakoa}")
                print(f"Mezu deszifratua: {proba_testua}")
                return
        except:
            # Testu laburregiek edo erroreek jarraitzea ahalbidetu
            continue
            
    print("Ezin izan da gako zuzena automatikoki inferitu.")

# Emandako mezua
mezua = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"
indar_eraso_cesar(mezua)
