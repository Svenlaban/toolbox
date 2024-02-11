"""CTF Tool"""
import ipaddress

def klassificera_ip(ip):
    """Verifierar IP adressen och kollar ifall den är intern eller extern"""
    try:
        # Konvertera strängen till ett IP-adressobjekt
        ip_obj = ipaddress.ip_address(ip)
        # Kontrollera om IP-adressen är privat
        if ip_obj.is_private:
            return "Detta är en intern (privat) IP-adress. Vissa alternativ ger ej resultat."
        return "Detta är en extern (offentlig) IP-adress. Gör inget som kan vara olagligt."
    except ValueError:
        print("Ogiltig IP-adress angiven. Skriv in korrekt IP-adress.")
        ipval()


def ipval():
    """Går vidare till att visa olika IP verktyg"""
    print("Vilken IP adress vill du undersöka?")
    ip_adress = input("Ange en IP-adress: ")  # Notera att du använder 'ip_adress' här
    resultat = klassificera_ip(ip_adress)
    print(resultat)

    print(f"Det ip vi kommer att undersöka är {ip_adress} hur vill du gå vidare?")

    print("1: Portscanning med NMAP")
    print("2: IP-information(whois)")
    print("3: IP-adress ursprungsland")
    print("4: Kolla om det finns en webbsida uppe")
    print("5: Kolla Geodata")

    val = input("IP-adress:")
    if val == "1":
        print("Gör en portscanning")
        from tools.nmapscan import get_nmapscan
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
        print("Kolla geodata")
        from tools.ipapi import get_ipapi_info
        get_ipapi_info(ip_adress)
    elif val == "6":
        print("6")
    else:
        print("Ogiltigt val")



def main():
    """Första-sidan med val av verktyg"""
    while True:
        print("\nVälkommen till CTF assistenten")
        print("Vad vill du undersöka?")
        print("1: IP-adess")
        print("2: Knäcka en lösenordshash")
        print("3: Caesarchiffer")
        print("4: Base64 decode/encode")
        print("5: Avsluta")

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
            print("Base64 decode/encode")
            input_string = input ("Ange sträng:")
            from tools.base64encode import auto_encode_decode
            auto_encode_decode(input_string)
        elif val == "5":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    main()
