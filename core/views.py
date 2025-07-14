from django.shortcuts import render
from news.views import *
from Activity.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import requests

# Create your views here.

def get_weather():
    city = 'Dili'
    api_key = '03815455da08763e32a045ba6450d92c'  
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Dili&appid=03815455da08763e32a045ba6450d92c&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        weather_data = response.json()

        if 'main' in weather_data:
            temperature = weather_data['main']['temp']
            return temperature
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def Index(request):
    activities = Activities.objects.all()
    temperature = get_weather()
    current_datetime = datetime.now()
    news = News.objects.all()
    latest_news = News.objects.order_by('-created')[0:3]

    page = request.GET.get('page')

    paginator = Paginator(news, 9)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # page = 1
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {
        'news':news,
        'activities':activities,
        'latest_news':latest_news,
        'current_datetime': current_datetime,
        'temperature': temperature,
        'page':page,
	
    }
    return render(request, 'home/index.html', context)

def aboutUs(request):
	latest_news = News.objects.order_by('-created')[0:3]
	context = {
		'latest_news':latest_news,
	}
	return render(request, 'home/vizaun_misaun.html', context)

def Member(request):
	# latestMember = News.objects.order_by('-created')[0:3]
	# context = {
	# 	'latest_news':latest_news,
	# }
	return render(request, 'home/team.html')

def Contact(request):
	# latestMember = News.objects.order_by('-created')[0:3]
	# context = {
	# 	'latest_news':latest_news,
	# }
	return render(request, 'home/contact.html')





