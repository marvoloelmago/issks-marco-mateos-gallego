def xor_stream_cipher(data_bytes: bytes, key_bytes: bytes) -> bytes:

    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes)])

def main():
    # Frogatzeko mezua eta gakoa
    mezua_str = "GURE MEZUA HAU DA"
    gakoa_str = "GAKO1234567890"

    # Mezua eta gakoa byte formatuan lortu
    mezua_bytes = mezua_str.encode('utf-8')
    gakoa_bytes = gakoa_str.encode('utf-8')

    # Kriptograma sortu XOR fluxu zifraketa aplikatuz
    kriptograma_bytes = xor_stream_cipher(mezua_bytes, gakoa_bytes)

    # Deskodetua lortu XOR fluxu zifraketa aplikatuz
    deskodetua_bytes = xor_stream_cipher(kriptograma_bytes, gakoa_bytes)
    deskodetua_str = deskodetua_bytes.decode('utf-8')

    # Inprimatu emaitzak
    print("------------------- EMAITZAK -------------------\n")
    print(f"Mezua (testu lauan):            {mezua_str}")
    print(f"Mezua (hexadezimalean):         {mezua_bytes.hex(' ')}")
    print(f"Gakoa (testu lauan):            {gakoa_str}")
    print(f"Gakoa (hexadezimalean):         {gakoa_bytes.hex(' ')}")
    print(f"Kriptograma (hexadezimalean):   {kriptograma_bytes.hex(' ')}")
    print(f"Deskodetua (testu lauan):       {deskodetua_str}\n")

    # Egiaztapena
    if deskodetua_bytes == mezua_bytes:
        print("Dena ondo!")
    else:
        print("Zerbait gaizki joan da!")

if __name__ == "__main__":
    main()