import ipaddress

def klassificera_ip(ip):
    try:
        # Konvertera strängen till ett IP-adressobjekt
        ip_obj = ipaddress.ip_address(ip)

        # Kontrollera om IP-adressen är privat
        if ip_obj.is_private:
            return "Detta är en intern (privat) IP-adress. Vissa alternativ kommer ej att ge resultat."
        else:
            return "Detta är en extern (offentlig) IP-adress. Gör inget som kan anses vara olagligt."
    except ValueError:
        print("Ogiltig IP-adress angiven. Skriv in korrekt IP-adress.")
        ipval()

def ipval():
    print("Vilken IP adress vill du undersöka?")
    ip_adress = input("Ange en IP-adress: ")  # Notera att du använder 'ip_adress' här
    resultat = klassificera_ip(ip_adress)
    print(resultat)

    print(f"Det ip vi kommer att undersöka är {ip_adress} hur vill du gå vidare?")

    print("1: Portscanning med NMAP")
    print("2: Gobuster enkla directory scanning")
    print("3: Gobuster .php filer")
    print("4: Nikto directory scanning")
    print("5: IP-information(whois)")

    val = input("IP-adress:")
    if val == "1":
        print("Gör en portscanning")
        from tools.nmap import get_nmapscan
        get_nmapscan(ip_adress)
    elif val == "2":
        print("2")
    elif val == "3":
        print("3")
    elif val == "4":
        print("4")
    elif val == "5":
        print("Hämtar whois-data")
        from tools.whois import get_whois
        get_whois(ip_adress)
    elif val == "6":
        print("6")
    else:
        print("Ogiltigt val")

def hashval():
    print("hash")

def cryptoval():
    print("crypto")


print("Välkommen till CTF assistenten")
print("Vad vill du undersöka?")
print("1: IP-adess")
print("2: hash-sträng")
print("3: crypto")

val = input("Ange ditt val: ")

if val == "1":
    ipval()
elif val == "2":
    hashval()
elif val == "3":
    cryptoval()


else:
    print("ogiltigt val.")