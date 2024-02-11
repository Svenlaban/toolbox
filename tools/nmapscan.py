"""Nmap port scanning tool"""
import nmap

def print_and_write(file, message):
    """Skriv ut och skriv meddelande till fil."""
    print(message)
    file.write(message + "\n")

def scan_host(nm, host, file):
    """Skanna en specifik värd och skriv resultaten till fil."""
    host_info = f'Host: {host} ({nm[host].hostname()})'
    print_and_write(file, host_info)

    state_info = f'State: {nm[host].state()}'
    print_and_write(file, state_info)

    for proto in nm[host].all_protocols():
        proto_info = '----------\n' + f'Protocol: {proto}'
        print_and_write(file, proto_info)

        lport = sorted(nm[host][proto].keys())
        for port in lport:
            if nm[host][proto][port]['state'] == 'open':
                port_info = f'Port: {port}\tState: {nm[host][proto][port]["state"]}'
                print_and_write(file, port_info)
                if 'version' in nm[host][proto][port]:
                    version_info = f'Version: {nm[host][proto][port]["version"]}'
                    print_and_write(file, version_info)

def get_nmapscan(ip_address, output_file='nmap_scan_results.txt'):
    """Kör en portscanning via nmap."""
    nm = nmap.PortScanner()

    try:
        nm.scan(ip_address, arguments='-sV -sC -p- --open -v')
    except nmap.PortScannerError as e:
        print(f"Skanning misslyckades: {e}")
        return
    except Exception as e:  # Behåller generell exceptionhantering som en sista utväg
        print(f"Okänt fel: {e}")
        return

    hosts_up = nm.all_hosts()  # Hämta listan över upptäckta värdar

    with open(output_file, 'w', encoding='utf-8') as file:  # Specifierar encoding
        if hosts_up:
            for host in hosts_up:
                scan_host(nm, host, file)
        else:
            print_and_write(file, "Inga värdar hittades.")

# Ersätt 'IP_ADDRESS' med den faktiska IP-adressen du vill skanna
# get_nmapscan('IP_ADDRESS')
