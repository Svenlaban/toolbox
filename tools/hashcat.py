import subprocess
import sys

def run_hashcat():
    """
    Kör Hashcat på en given hash-sträng.

    :param hash_string: Hash-strängen som ska knäckas.
    :param hash_type: Hash-typen som Hashcat ska använda (t.ex. '0' för MD5).
    """
    try:
        # Konverterar hash_type och attack mode (3) till strängar
        hash_type = input("Ange hashtyp: ")
        hash_string = input("Ange hashsträng: ")
        # Bygger Hashcat-kommandot med alla argument som strängar
        command = ['hashcat', '-m', hash_type, '-a', '0', hash_string, './tools/wordlist/rockyou.txt']

        # Kör Hashcat-kommandot
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Skriver ut resultatet
        print("Standard Output:", result.stdout)
        print("Error Output:", result.stderr)
    except Exception as e:
        print(f"Det gick inte att köra Hashcat: {e}")
