from ipwhois import IPWhois
import ipaddress

def get_whois(ip_address):
    try:
        # Kontrollera först om det är en privat IP-adress
        ip_obj = ipaddress.ip_address(ip_address)
        if ip_obj.is_private:
            print("Detta är en intern (privat) IP-adress. Denna metod fungerar enbart på externa adresser.")
            return

        obj = IPWhois(ip_address)
        results = obj.lookup_rdap(depth=1)

        # Extrahera och skriv ut den information du är intresserad av
        asn_description = results.get('asn_description', 'Ingen beskrivning tillgänglig')
        network = results.get('network', {})
        name = network.get('name', 'Okänt nätverk')
        cidr = network.get('cidr', 'Ingen CIDR tillgänglig')
        country = network.get('country', 'Inget land angivet')

        print(f"AS-beskrivning: {asn_description}")
        print(f"Nätverksnamn: {name}")
        print(f"CIDR: {cidr}")
        print(f"Land: {country}")

        # Om du vill inkludera adressinformation, kan det kräva ytterligare parsing beroende på datans struktur

    except ValueError as e:
        print(f"Ogiltig IP-adress angiven: {e}")
    except Exception as e:
        print(f"Det gick inte att hämta WHOIS-information: {e}")