import requests
import json
import sys
import argparse
import click
from library.db import readInFile, saveInFile, deleteInFile
from services.weather import getWeather
from services.user import login, getAccountId, baseUrl, headers
from services.allocations import updateAllocations


@click.command()
@click.option("--email", "-e")
@click.option('--password', "-p")
@click.option("--force", "-f", is_flag=True)
def main(email, password, force):
    newWeather = getWeather()
    if (newWeather != readInFile('weather')) or force:
        login(email if email else readInFile('email'),
              password if password else readInFile('password'))
        if updateAllocations(newWeather):
            saveInFile('weather', newWeather)


if __name__ == '__main__':
    main()
