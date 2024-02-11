import nmap

def get_nmapscan(ip_address, output_file='nmap_scan_results.txt'):
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

    with open(output_file, 'w') as file:  # Öppna filen för skrivning
        if hosts_up:
            # Om minst en värd är uppe, skriv ut resultaten och skriv till filen
            for host in hosts_up:
                host_info = f'Host: {host} ({nm[host].hostname()})\n'
                print(host_info)
                file.write(host_info)

                state_info = f'State: {nm[host].state()}\n'
                print(state_info)
                file.write(state_info)

                for proto in nm[host].all_protocols():
                    proto_info = '----------\n' + f'Protocol: {proto}\n'
                    print(proto_info)
                    file.write(proto_info)

                    lport = sorted(nm[host][proto].keys())
                    for port in lport:
                        if nm[host][proto][port]['state'] == 'open':
                            port_info = f'Port: {port}\tState: {nm[host][proto][port]["state"]}\n'
                            print(port_info)
                            file.write(port_info)
                            if 'version' in nm[host][proto][port]:
                                version_info = f'Version: {nm[host][proto][port]["version"]}\n'
                                print(version_info)
                                file.write(version_info)
        else:
            # Om ingen värd är uppe, skriv ut ett meddelande och skriv till filen
            no_hosts = "Inga värdar hittades.\n"
            print(no_hosts)
            file.write(no_hosts)

get_nmapscan('IP_ADRESS')  # Byt ut 'IP_ADRESS' mot den faktiska IP-adressen du vill skanna
