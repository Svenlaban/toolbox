import subprocess
import tempfile

def run_john_bruteforce(hash_string):
    """
    Kör John the Ripper i brute-force-läge på en given hash.

    :param hash_string: Hash-strängen som ska knäckas.
    :param hash_type: Typen av hash, standard är 'raw-md5'. Justera efter behov.
    """
    try:
        # Skapar en temporär fil för att lagra hash-strängen
        with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as tmpfile:
            tmpfile_name = tmpfile.name
            tmpfile.write(hash_string + "\n")

        # Bygger kommandot för att köra John the Ripper i brute-force-läge
        command = ['john', '--wordlist=None', '--rules=All', tmpfile_name]

        # Kör kommandot
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Skriver ut resultatet
        print("Standard Output:", result.stdout)
        print("Error Output:", result.stderr)

        # Tömmer och tar bort den temporära filen
        subprocess.run(['john', '--pot=NONE', '--format=' + hash_type, '--wordlist=None', '--rules=All', '--show', tmpfile_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(['rm', tmpfile_name])
    except Exception as e:
        print(f"Det gick inte att köra John the Ripper: {e}")

