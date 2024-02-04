import sys
import datetime

class OutputLogger(object):
    def __init__(self, filename, stdout):
        self.stdout = stdout
        self.logfile = open(filename, 'w')

    def write(self, message):
        self.stdout.write(message)
        self.logfile.write(message)

    def flush(self):  # Needed if Python 3.x
        self.stdout.flush()
        self.logfile.flush()

def start_logging():
    # Skapar ett filnamn baserat på nuvarande datum och klockslag
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"log_{current_time}.txt"

    # Omdirigerar stdout till både skärmen och filen
    sys.stdout = OutputLogger(filename, sys.stdout)

# Kör funktionen för att starta loggningen
start_logging()

# Exempel på output som nu också loggas till fil
print("Detta är ett testmeddelande.")