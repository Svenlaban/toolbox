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
    print("2: IP-information(whois)")
    print("3: IP-adress ursprungsland")
    print("4: Kolla om det finns en webbsida uppe")
    print("5: IP-information(whois)")

    val = input("IP-adress:")
    if val == "1":
        print("Gör en portscanning")
        from tools.nmap import get_nmapscan
        get_nmapscan(ip_adress)
    elif val == "2":
        print("Hämtar whois-data")
        from tools.whois import get_whois
        get_whois(ip_adress)
    elif val == "3":
        print("Hämtar ursprungsland")
        from tools.countrylookup import get_country
        get_country(ip_adress)
    elif val == "4":
        print("Kollar om det finns en websida uppe")
        from tools.checkweb import check_website_status
        check_website_status(ip_adress)
    elif val == "5":
        print("5")
    elif val == "6":
        print("6")
    else:
        print("Ogiltigt val")

def hashval():
    print("hash")

def cryptoval():
    print("crypto")


def main():
    while True:
        print("\nVälkommen till CTF assistenten")
        print("Vad vill du undersöka?")
        print("1: IP-adess")
        print("2: Knäcka en lösenordshash")
        print("3: crypto")
        print("4: Avsluta")

        val = input("Ange ditt val: ")
        if val == "1":
            ipval()
        elif val == "2":
            from tools.hashcat import run_hashcat
            run_hashcat()
        elif val == "3":
            crot13 = input ("Ange text som ska krypteras/dekrypteras:")
            from tools.caesar import rot13
            rot13(crot13)

        elif val == "4":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    main()