# :sunny::cloud: Napbot Weather Bot :cloud::sunny:

> a bot who track the Napbot weather and change allocation in consequence

## :memo: Installation

- `git clone https://github.com/vodkhard/weather-napbot`
- `pip install -r requirements.txt`

#### If you use Docker

- `docker build -t weather-napbots .`

## :beer: Usage

- `python main.py --email [napbots email] --password [napbots password]`

- you can also edit the `user.json` file and add your informations in:
```json
{"email": "[napbots email]", "password": "[napbots password]"}
```
- so now you can run `python main.py`

#### If you use Docker

- `docker run -t --rm weather-napbots`

## :book: Configuration

- Change allocations and leverage in `allocations.json`
- Change email and password in `user.json`
- if you want to launch the command periodically you can edit your `cron`
  - `crontab -e`
  - `0 * * * * docker run -t --rm weather-napbots >> /var/log/weather-napbots/weather.log` for launching bot every hour at 0