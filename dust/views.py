from django.shortcuts import render
from urllib.parse import urlencode, unquote, quote_plus
import json

# Create your views here.
# def dust_check(request):
#     if request.method=="GET":
#         with open('mymovie/config2.json') as json_file:
#             config_data = json.load(json_file)
#         serviceKey = config_data['serviceKey']
#         serviceKeyDecoded = config_data['serviceKeyDecoded']
#         station = []
#         pm10 = []
#         url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"
#         returnType = "json"
#         numOfRows = "100"
#         pageNo = "1"
#         sidoName = "경기"
#         ver = "1.0"

#         queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
#         res = request.get(url + queryParams)
#         xml = res.text
#         soup = BeautifulSoup(xml, 'html.parser')
#         for tag in soup.find_all('stationname'):
#             station.append(tag.text)
#         for tag in soup.find_all('pm10value'):
#             pm10.append(tag.text)
#         res = dict(zip(station, pm10))
#         return res