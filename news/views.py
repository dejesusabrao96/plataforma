import os
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from .forms import NewsForm
from .models import News, Category
from django.utils import timezone
from core.utils import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
import hashlib



# Create your views here.
@login_required()
@allowed_users(allowed_roles=['Admin'])
def ListNews(request):
	group = request.user.groups.all()[0].name
	news = News.objects.all()
	context = {
		'group':group,
		'title':"Lista News",
		"page":"list",
		'news':news,		
	}
	return render(request,'news.html',context)
def aboutPost(request):
	today = date.today()

	today_news = News.objects.filter(created__year=today.year,created__month=today.month,created__day=today.day).count()
	tot_news = News.objects.all().count()
	this_month_news = News.objects.filter(created__year=today.year,created__month=today.month).count()
	this_year_news = News.objects.filter(created__year=today.year).count()
	context = {


	}
	return render(request, 'news.html', context)

def detailNews(request, hashid)
    cat = Category.objects.all()
    latest_news = News.objects.all().order_by('-created')[:3]
    news = get_object_or_404(News, hashed=hashid)  

    context = {
        'latest_news': latest_news,
        'news': news,
        'cat': cat,
    }

    return render(request, 'detailnews.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def addNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            raw_string = str(instance.pk)  
            instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
            # instance.hashed = hashlib.sha256(raw_string.encode('utf-8')).hexdigest()

            instance.save()

            messages.success(request, 'News is added successfully.')

            if 'save_and_add_another' in request.POST:
                return redirect('addnews')  
            return redirect('List-News') 
    else:
        form = NewsForm()

    context = {
        'form': form,
    }
    return render(request, 'newsForm.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def updateNews(request, hashid):
    group = request.user.groups.all()[0].name
    NewsData = get_object_or_404(News, hashed=hashid)  

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=NewsData)
        if form.is_valid():
            instance = form.save()
            messages.info(request, f'News is updated Successfully.')
            return redirect('List-News')
    else:
        form = NewsForm(instance=NewsData)

    context = {
        'sukuActive': "active",
        'page': "form",
        'group': group,
        'form': form,
        'hashed': NewsData.hashed  
    }

    return render(request, 'newsForm.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def DeleteNews(request, hashid):
	group = request.user.groups.all()[0].name
	news = get_object_or_404(News, hashed=hashid)
	# an = news.news
	news.delete()
	messages.warning(request, f'News is Deleted Successfully.')
	return redirect('List-News')

