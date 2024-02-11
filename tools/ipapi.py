import requests

def get_ipapi_info(ip_adress):
    url = f"http://ip-api.com/json/{ip_adress}"
    response = requests.get(url)
    data = response.json()

    # Skriv ut några av de data som returneras av API:t
    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Land: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"Stad: {data['city']}")
        print(f"ISP: {data['isp']}")
    else:
        print("Information inte tillgänglig.")
