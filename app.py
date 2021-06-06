from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# url = "https://www.amazon.in/HP-Pavilion-Processor-15-6-inch-15-dk0264TX/dp/B08CHWP814?ref_=Oct_DLandingS_D_a090a9e5_62&smid=A14CZOWI0VEHLG"
# url = 'https://www.google.com/search?q=tv&tbm=shop&sxsrf=ALeKk00IiOx40LalEJmnfuwSjuddYrrf1Q%3A1622867395276&source=hp&ei=w_26YLm8DY6ImAX47q7ICA&oq=tv&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIAFDwMFjhMWCVNGgBcAB4AIABnwGIAZYCkgEDMC4ymAEAoAEBsAEA&sclient=products-cc&ved=0ahUKEwj5qfCU1P_wAhUOBKYKHXi3C4kQ4dUDCAc&uact=5'
url = 'https://www.google.com/search?q=card+man+hinh&tbm=shop'
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
# name = soup.select('a8Pemb')[0].getText()
# print(name)

# print( soup.find(id="a8Pemb"))
spansPrices = soup.find_all('span', {'class' : 'a8Pemb'})
print(spansPrices)
for Prices  in spansPrices:
    # print(tag)
    print(Prices .contents[0])

Prices = [Prices.contents[0] for Prices  in spansPrices]


divStores = soup.find_all('div', {'class' : 'mqQL1e'})
print('==========Stores=========')
print(divStores)
Stores = []
for Store in divStores:
    # print(tag)
    # print(Store.contents[0])
    span = Store.find_next('span')
    print(span.string)


Stores = [Store.find_next('span').string for Store  in divStores]

for mPrices, mStores in zip(Prices, Stores):
    print(mPrices, mStores)

# mFile = open('web.txt', mode='w',encoding='utf-8' )
# mFile.write(soup.prettify())
# mFile.close()

