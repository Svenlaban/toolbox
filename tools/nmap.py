import nmap

def get_nmapscan(ip_address):
    nm = nmap.PortScanner()

    try:
        # Här lägger vi till '-v' för verbose output
        nm.scan(ip_address, arguments='-sV -sC -p- --open -v')
    except nmap.PortScannerError as e:
        print(f"Skanning misslyckades: {e}")
        return
    except Exception as e:
        print(f"Okänt fel: {e}")
        return

    hosts_up = nm.all_hosts()  # Hämta listan över upptäckta värdar

    if hosts_up:
        # Om minst en värd är uppe, skriv ut resultaten
        for host in hosts_up:
            print(f'Host: {host} ({nm[host].hostname()})')
            print(f'State: {nm[host].state()}')

            for proto in nm[host].all_protocols():
                print('----------')
                print(f'Protocol: {proto}')

                lport = sorted(nm[host][proto].keys())
                for port in lport:
                    if nm[host][proto][port]['state'] == 'open':
                        print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')
                        if 'version' in nm[host][proto][port]:
                            print(f'Version: {nm[host][proto][port]["version"]}')
    else:
        # Om ingen värd är uppe, skriv ut ett meddelande
        print("Inga värdar hittades.")

get_nmapscan('IP_ADRESS')  # Byt ut 'IP_ADRESS' mot den faktiska IP-adressen du vill skanna
