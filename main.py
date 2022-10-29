from bs4 import BeautifulSoup
import requests
import pandas
import openpyxl

page_no = 1
result = True
car_tags = []
prices = []
while result:
    URL = f"https://jo.opensooq.com/ar/find?have_images=&allposts=&onlyPremiumAds=&onlyDonation=&onlyPrice=true&onlyUrgent=&onlyShops=&onlyMemberships=&onlyBuynow=&memberId=&sort=cp_Kilometers_Cars_value_ss.asc&PostDynamicFieldModel%5BDeliveryService%5D=&hoodId=&cityId=&term=&cat_id=1777&scid=&city=&cat_id=1777&PostDynamicFieldModel%5BBrand%5D%5B%5D=Ford&PostDynamicFieldModel%5BBrand_child%5D%5B%5D=Focus&PostDynamicFieldModel%5BCar_Year%5D%5Bfrom%5D=2013&PostDynamicFieldModel%5BCar_Year%5D%5Bto%5D=2013&price_from=10000&price_to=13000&price_currency=10&PostDynamicFieldModel%5BFuel_Cars%5D%5B%5D=Electric&page="
    URL = URL + f"{page_no}"
    response = requests.get(url=URL).text
    soup = BeautifulSoup(response, 'html.parser')
    try:
        no_result = soup.select_one(selector="#gridPostListing div.empty").get_text()
    except AttributeError:
        print(page_no)
        page_no += 1
    else:
        result = False

    car_tags += soup.select(selector='div.rectLiDetails.tableCell.vMiddle.p8')

titles = [tag.select_one(selector='a').get('title') for tag in car_tags]
for tag in car_tags:
    try:
        price = int("".join(tag.select_one(selector='span.inline.ltr').get_text().split(',')))
    except AttributeError:
        price = 0

    prices.append(price)

brands = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[1].get('title') for tag in
          car_tags]
models = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[2].get('title') for tag in
          car_tags]
years = [tag.select(selector='div.rectCatesLinks.mb15.mt15.clear span.font-12.inline')[3].get('title') for tag in
         car_tags]
cities = [" ".join(tag.select_one(selector='div.clear.font-12').get_text().strip().split()).split("|")[0].strip()
          for
          tag in
          car_tags]
areas = [" ".join(tag.select_one(selector='div.clear.font-12').get_text().strip().split()).split("|")[1].replace(
    " Cars For Sale ", "").lstrip() for tag in
         car_tags]
car_links = [
    "https://jo.opensooq.com" + tag.select_one(selector="a.block.postLink.notEg.postSpanTitle.noEmojiText").get(
        "href")
    for tag in car_tags]

# print()
# print(len(titles))
# print(len(prices))
# print(len(brands))
# print(len(models))
# print(len(years))
# print(len(cities))
# print(len(areas))
# print(len(car_links))
# print(len(page_links))

cars = {
    "titles": titles,
    "prices": prices,
    "brands": brands,
    "models": models,
    "years": years,
    "cities": cities,
    "areas": areas,
    "car_links": car_links,
}

data = pandas.DataFrame(cars)
data.to_excel("cars.xlsx")
