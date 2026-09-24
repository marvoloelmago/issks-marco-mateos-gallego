import collections
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    ciphertext = input("\nSartu deszifratu nahi duzun testua:\n> ").strip()
    
    if not ciphertext:
        print("Ez da testurik sartu. Irteten...")
        return

    letters = [c for c in ciphertext if c.isalpha()]
    counter = collections.Counter(letters)
    cipher_freqs = counter.most_common()

    mapping = {}

    while True:
        clear_screen()
        
        decrypted_text = ""
        for char in ciphertext:
            if char in mapping:
                decrypted_text += f"\033[92m{mapping[char]}\033[0m"
            else:
                decrypted_text += char
                
        print("UNEKO TESTUA:")
        print("-" * 60)
        print(decrypted_text)
        print("-" * 60 + "\n")

        print("TESTUAREN FREKUENTZIAK")
        
        freq_display = []
        for c_char, c_count in cipher_freqs:
            mapped_to = f" -> {mapping[c_char]}" if c_char in mapping else ""
            freq_display.append(f"{c_char}({c_count}){mapped_to:<6}")
            
        for i in range(0, len(freq_display), 5):
            print("    ".join(freq_display[i:i+5]))

        print("\nKomandoak:")
        print(" - 'X=y' X letra y-rekin aldatzeko")
        print(" - 'del X' X-n egindako ordezkapena ezabatzeko")
        print(" - 'atera' programa amaitzeko")
        
        cmd = input("\nKomando bat sartu: ").strip()

        if cmd.lower() == 'atera':
            break
        elif cmd.startswith("del "):
            char_to_del = cmd[4:].strip()
            if char_to_del in mapping:
                del mapping[char_to_del]
        elif "=" in cmd:
            parts = cmd.split("=")
            if len(parts) == 2 and len(parts[0].strip()) == 1 and len(parts[1].strip()) == 1:
                cipher_char = parts[0].strip()
                plain_char = parts[1].strip().lower()
                mapping[cipher_char] = plain_char

if __name__ == "__main__":
    main()