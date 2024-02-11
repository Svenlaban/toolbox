""""IP-geodata checkup Tool"""
import requests

def get_ipapi_info(ip_adress):
    """Hämtar Ip-information från ett öppet API på ip-api.com"""
    url = f"http://ip-api.com/json/{ip_adress}"
    try:
        response = requests.get(url, timeout=5)  # 5 sekunders timeout
        data = response.json()

        if data['status'] == 'success':
            print(f"IP: {data['query']}")
            print(f"Land: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"Stad: {data['city']}")
            print(f"ISP: {data['isp']}")
        else:
            print("Information inte tillgänglig.")
    except requests.exceptions.Timeout:
        print("Timeout nådd vid anrop till API")
    except requests.exceptions.RequestException as e:
        # Hanterar andra requests-relaterade fel
        print(f"Ett fel uppstod vid anrop till API: {e}")
