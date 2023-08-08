import json
import os
import urllib.request
from django.shortcuts import render

# Create your views here.
def api_service_search(request):
    if request.method == 'GET':
        with open('mymovie/config3.json') as json_file:
            config_data = json.load(json_file)
        client_serviceKey = config_data['serviceKeyDecoded']
        # q = request.GET.get('q')
        # encText = urllib.parse.quote("{}".format(q))
        url = "https://api.odcloud.kr/api/gov24/v3/serviceList?page=1&perPage=10"
        book_api_request = urllib.request.Request(url)
        book_api_request.add_header("Authorization", "Infuser "+client_serviceKey)
        # book_api_request.add_header("X-Naver-Client-Id",client_id)
        # book_api_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(book_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            # print(result)
            datas = result.get('data')
            # print(datas[0]['사용자구분'])
            context = {
                'datas': datas
            }
        else:
            print("error code: "+rescode)
        return render(request, 'service/service.html', {'datas': datas})
    else:
        return render(request, 'service/service.html')
