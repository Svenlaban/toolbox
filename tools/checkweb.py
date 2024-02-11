"""Kollar om det körs webbsida på en IP-adress"""
import requests

def check_website_status(ip_adress):
    """Kollar efter statuskod 200 på http och https"""
    # Definiera de två URL:erna för HTTP och HTTPS
    urls = [
        f'http://{ip_adress}',
        f'https://{ip_adress}'
    ]

    # Loopa igenom båda URL:erna och gör en GET-förfrågan för var och en
    for url in urls:
        try:
            response = requests.get(url, timeout=5)  # Timeout för att hantera långsamma svar
            print(f"URL: {url}, Statuskod: {response.status_code}")
        except requests.ConnectionError:
            print(f"Kunde inte ansluta till {url}. Ingen anslutning.")
        except requests.Timeout:
            print(f"Timeout när försökte ansluta till {url}.")
        except requests.RequestException as e:
            # För alla andra typer av fel
            print(f"Kunde inte ansluta till {url}. Fel: {e}")
