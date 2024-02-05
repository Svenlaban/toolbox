import logging
import datetime

def setup_logging():
    # Skapar ett filnamn baserat på nuvarande datum och klockslag
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"log_{current_time}.txt"

    # Konfigurerar loggningsmodulen
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(filename, 'w'),
                                  logging.StreamHandler()])

# Kör funktionen för att starta loggningen
setup_logging()

# Exempel på output som nu också loggas till fil och konsol
logging.info("Detta är ett testmeddelande.")