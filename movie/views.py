import json
import os
import urllib.request
from django.shortcuts import render

def menu(request):
    return render(request, 'movie/menu.html')

def api_book_search(request):

    if request.method == 'GET':
        with open('mymovie/config.json') as json_file:
            config_data = json.load(json_file)
        client_id = config_data['NAVER']['CLIENT_ID']
        client_secret = config_data['NAVER']['CLIENT_SECRET']
        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/book?query=" + encText  # json 결과
        book_api_request = urllib.request.Request(url)
        book_api_request.add_header("X-Naver-Client-Id",client_id)
        book_api_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(book_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')

            context = {
                'items': items
            }
            return render(request, 'movie/search_book.html', context=context)
    else:
        return render(request, 'movie/search_book.html')

def api_movie_search(request):
    if request.method == "GET":
        with open('mymovie/config.json') as json_file:
            config_data = json.load(json_file)
        client_id = config_data['NAVER']['CLIENT_ID']
        client_secret = config_data['NAVER']['CLIENT_SECRET']
        q=request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/shop?query=" + encText
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id",client_id)
        movie_api_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()
        if (rescode ==200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            context = {
                'items':items
            }
            return render(request, 'movie/search_movie.html', context=context)
    else:
        return render(request,'movie/search_movie.html')