from random import randint
import logging
import requests


logging.basicConfig(
    level=logging.DEBUG,
    filename='analytics.log',
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
class Research:
    def __init__(self, path):
        self.path = path
        logging.debug("Research class initialized with path: %s", path)

    def file_reader(self, has_header=True):
        logging.debug("Reading file: %s", self.path)
        with open (self.path, 'r') as f:
            lines = f.readlines().strip().split(',')

        if has_header:
            lines = lines[1:]

        return [[int(x) for x in line.split(',')] for line in lines]
    
    def send_telegram(self, message):
        logging.debug("Sending Telegram message: %s", message)
        token = "8286917069:AAGlGISWADbvNyjCPjpKqk3OM5iNSWrnmGw"
        chat_id = "1265113315"
        url = f"https://api.telegram.org/bot{token}/sendMessage"

        try:
            response = requests.post(url, json={
                "chat_id": chat_id,
                "text": message
            })
            logging.debug("Telegram message sent succesfully")
        except Exception as e:
            logging.debug("Telegram error: %s", e)
        
    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.debug("Calculations class initialized")

        def counts(self):
            logging.debug("Calculating the counts of heads and tails")
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails
        
        def fractions(self, heads, tails):
            logging.debug("Calculating the fractions")
            total = heads + tails
            head_frac = int(heads / total * 10000) / 10000
            tail_frac = int(tails / total * 10000) / 10000
            return head_frac, tail_frac
        
class Analytics(Research.Calculations):
    def predict_random(self, num):
        logging.debug("Predicting random observations")
        predictions = []
        for _ in range(num):
            rand = randint(0, 1)
            predictions.append([rand, 1 - rand])
        return predictions

    def predict_last(self):
        logging.debug("Getting last observation")
        return self.data[-1]

    def save_file(self, data, filename, extension):
        logging.debug("Saving file: %s.%s", filename, extension)
        with open(f"{filename}.{extension}", 'w') as f:
            f.write(data)