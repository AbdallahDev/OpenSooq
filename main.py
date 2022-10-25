from pprint import pprint

from bs4 import BeautifulSoup
import requests
import pandas

URL = "https://bit.ly/3gsTv9O"
response = requests.get(url=URL).text

soup = BeautifulSoup(response, 'html.parser')

car_tags = soup.select(selector='div.rectLiDetails.tableCell.vMiddle.p8')
titles = [tag.select_one(selector='a').get('title') for tag in car_tags]
prices = [int("".join(tag.select_one(selector='span.inline.ltr').get_text().split(','))) for tag in car_tags]
brands = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[1].get('title') for tag in
          car_tags]
models = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[2].get('title') for tag in
          car_tags]
years = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[3].get('title') for tag in
         car_tags]

cities = [" ".join(tag.select_one(selector='div.clear.font-12').get_text().strip().split()).split("|")[0].strip() for
          tag in
          car_tags]
areas = [" ".join(tag.select_one(selector='div.clear.font-12').get_text().strip().split()).split("|")[1].replace(
    " Cars For Sale ", "").lstrip() for tag in
         car_tags]

cars = {"brands": brands[4:8], "models": models[4:8]}
data = pandas.DataFrame(cars)
data.to_excel("cars.xlsx")
