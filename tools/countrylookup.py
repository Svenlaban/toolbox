"""IP origin country lookup Tool"""
import requests

def get_country(ip_address):
    """Kollar ursprungsland för ip adresser"""
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"IP: {ip_address}, Land: {data.get('country')}")
        else:
            print(f"Kunde inte hämta data för IP: {ip_address}")
    except requests.exceptions.Timeout:
        print("Timeout uppnådd vid anrop till API")
    except requests.exceptions.RequestException as e:
        # Hantera andra requests-relaterade fel (t.ex. anslutningsfel)
        print(f"Ett fel uppstod: {e}")
