# Toolbox-CTF

Välkommen till `toolbox-ctf`, ett repository skapat för att samla och dela verktyg, skript och resurser för Capture The Flag (CTF)-utmaningar. Här hittar du en mängd hjälpmedel som är utformade för att underlätta lösningen av CTF-utmaningar och IT-säkerhetstester inom olika kategorier.

## Innehåll

Toolboxen innehåller verktyg för:

- **Undersökning och scanning av IP-adresser**: Utforska och analysera nätverk.
- **Knäckning av lösenord**: Dekryptering av lösenordshashar genom olika tekniker.
- **Caesarchiffer**: Hjälp med kryptering och dekryptering baserat på Caesars chiffer.
- **Base64 decode/encode**: Konvertera data till och från Base64-kodning.
- **PHP Reverse Shell**: Skapar ett PHP Reverse Shell som går förbi Signature-based detection hos antivirusprogram.

## Externa beroenden

För att använda vissa verktyg i denna toolbox, behöver följande programvara vara installerad och korrekt konfigurerad på ditt system:

- **nmapscan.py**: Kräver att `nmap` är installerat och tillgängligt i systemets sökväg (`PATH`).
- **hashcat.py**: Kräver att `hashcat` är installerat och tillgängligt i systemets sökväg (`PATH`), samt tillgång till ordlistan `rockyou.txt`. Ordlistan ska placeras i `/toolbox-ctf/tools/wordlist/`.
- **duckduckgosearch.py**: Kräver att webbläsaren Google Chrome är installerad.
- **webshell.py**: Kräver att `netcat(nc)` är installerat och tillgängligt i systemets sökväg (`PATH`).

Om verktygslådan körs på ett Kali Linux-system, bör samtliga beroenden redan vara uppfyllda. Ordlistan `rockyou.txt` kan hittas på sökvägen `/usr/share/wordlists/rockyou.txt.gz`.

## Initiera projekt

För att komma igång med `toolbox-ctf`, följ dessa steg:

```bash
git clone https://github.com/Svenlaban/toolbox-ctf
cd toolbox-ctf
pip install -r requirements.txt
```

## Använda toolboxen

Alla steg är självförklarande efter start av main.py.

```bash
Välkommen till CTF assistenten
Vad vill du undersöka?
1: IP-adess
2: Knäcka en lösenordshash
3: Caesarchiffer
4: Base64 decode/encode
5: Skapa ett PHP Reverse Shell
6: Avsluta
Ange ditt val:
```