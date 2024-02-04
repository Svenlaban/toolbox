import requests

def get_country(ip_address):
    response = requests.get(f"http://ipinfo.io/{ip_address}/json")
    if response.status_code == 200:
        data = response.json()
        print(f"IP: {ip_address}, Land: {data.get('country')}")
    else:
        print(f"Kunde inte hämta data för IP: {ip_address}")