import requests
import json
import sys
import argparse
import click
from lib.db import readInFile, saveInFile, deleteInFile
from services.weather import getWeather
from services.user import login, getAccountId, baseUrl, headers
from services.allocations import updateAllocations


@click.command()
@click.option("--email", "-e")
@click.password_option()
@click.option("--force", "-f", is_flag=True)
def main(email, password, force):
    newWeather = getWeather()
    if (newWeather != readInFile('weather')) or force:
        login(email, password)
        if updateAllocations(newWeather):
            saveInFile('weather', newWeather)


if __name__ == '__main__':
    main()
