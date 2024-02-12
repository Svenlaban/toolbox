# toolbox-ctf

Välkommen till `toolbox-ctf`, ett repository skapat för att samla och dela verktyg, skript och resurser för Capture The Flag (CTF)-tävlingar. Här hittar du en mängd hjälpmedel som är utformade för att underlätta lösningen av CTF-utmaningar och penetrationstester inom olika kategorier.

## Innehåll

Toolboxen innehåller verktyg för

- Undersökning och scanning av IP-adresser
- Knäckning av lösenord
- Caesarchiffer
- Base64 decode/encode

## Externa beroenden

Verktyget nmapscan.py kräver att nmap finns installerat och med i path.

Verktyget hashcat.py kräver att hashcat finns installerat och med i path. Kräver även att man har ordlistan rockyou.txt i "/toolbox-ctf/tools/wordlist/"

Verktyget duckduckgosearch.py kräver att webbläsaren google chrome finns installerat på systemet.

Körs boxen på ett Kali-Linux system så finns samtliga program installerade. Ordlistan rockyou.txt finns på denna sökväg "/usr/share/wordlists/rockyou.txt.gz"

## Initiera projekt

git clone https://github.com/Svenlaban/toolbox-ctf
pip install -r requirements.txt
