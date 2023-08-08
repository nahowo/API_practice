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
        page = '1'
        perPage = '100'
        url = "https://api.odcloud.kr/api/gov24/v3/serviceList?page="+page+"&perPage="+perPage
        service_api_request = urllib.request.Request(url)
        service_api_request.add_header("Authorization", "Infuser "+client_serviceKey)
        response = urllib.request.urlopen(service_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            datas = result.get('data')
        else:
            print("error code: "+rescode)
        return render(request, 'service/service.html', {'datas': datas})
    else:
        return render(request, 'service/service.html')
