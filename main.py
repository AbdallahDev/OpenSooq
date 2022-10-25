from bs4 import BeautifulSoup
import requests

URL = "https://jo.opensooq.com/en/find?have_images=&allposts=&onlyPremiumAds=&onlyDonation=&onlyPrice=&onlyUrgent=&onlyShops=&onlyMemberships=&onlyBuynow=&memberId=&sort=price.asc&PostDynamicFieldModel[DeliveryService]=&hoodId=&cityId=&term=&cat_id=1777&scid=&city=&cat_id=1777&PostDynamicFieldModel[Car_Year][from]=&PostDynamicFieldModel[Car_Year][to]=&price_from=10000&price_to=17000&price_currency=10&PostDynamicFieldModel[Fuel_Cars][]=Electric&PostDynamicFieldModel[Kilometers_Cars][]=0&PostDynamicFieldModel[Kilometers_Cars][]=1%20-%20999&PostDynamicFieldModel[Kilometers_Cars][]=1000%20-%209999&PostDynamicFieldModel[Kilometers_Cars][]=010000%20-%2019999&PostDynamicFieldModel[Kilometers_Cars][]=020000%20-%2029999&PostDynamicFieldModel[Kilometers_Cars][]=030000%20-%2039999&PostDynamicFieldModel[Kilometers_Cars][]=040000%20-%2049999&PostDynamicFieldModel[Kilometers_Cars][]=050000%20-%2059999"
response = requests.get(url=URL).text

soup = BeautifulSoup(response, 'html.parser')

car_tags = soup.select(selector='div.rectLiDetails.tableCell.vMiddle.p8')
titles = [tag.select_one(selector='a').get('title') for tag in car_tags]
prices = [int("".join(tag.select_one(selector='span.inline.ltr').get_text().split(','))) for tag in car_tags]
brands = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[1].get('title') for tag in
          car_tags]
types = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[2].get('title') for tag in
         car_tags]
years = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[3].get('title') for tag in
         car_tags]
cities = [tag.select_one(selector='div.clear.font-12') for tag in
          car_tags]
