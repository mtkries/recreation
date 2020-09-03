import requests
import time

whitney = ""
non_whitney = "233262"
url = "https://www.recreation.gov/api/permitinyo/{}/availability".format(non_whitney)

#range of dates to poll for
start_date = "2020-10-01"
end_date = "2020-10-31"

#individual dates to check
entry_date = ['2020-10-04', '2020-10-05']
#location codes to check
location_code = ["460", "461"]
party_size = 4

#polling interval in seconds
interval = 60

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}

params = (
    ('start_date', start_date),
    ('end_date', end_date),
    ('commercial_acct', 'false'),
)

def parse_data(data):
    for date in entry_date:
        if date in data:
            for location in location_code:
                if location in data[date]:
                    if data[date][location]["remaining"] > party_size and not data[date][location]['is_walkup']:
                        print('ALERT: {} slots available for {} on {}!!'.format(data[date][location]["remaining"], location, date))

while True:
    try:
        response = requests.get('https://www.recreation.gov/api/permitinyo/233262/availability', headers=headers, params=params)
        if response.status_code == 200:
            parse_data(response.json()['payload'])
        else:
            raise Exception(str(response.status_code))
    except Exception as e:
        print(e)
    time.sleep(60)
