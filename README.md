
### Installation

1. Clone the repo
```sh
git clone https://github.com/danielchowofficiall/recreation.GIT
```
2. Make local .venv folder
```sh
mkdir .venv
```
3. Create Virtual Enviroment
```sh
pipenv install
```
4. Edit parameters
```sh
#range of dates to poll for
start_date = "2020-10-01"
end_date = "2020-10-31"

#individual dates to check
entry_date = ['2020-10-04', '2020-10-05']
#location codes to check
location_code = ["460", "461"]
party_size = 4

#polling interval in seconds
interval = 60```
5. Start Polling
```sh
python poll.py
```
