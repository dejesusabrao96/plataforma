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

# def hash_md5(value):
#     # Fungsi untuk menghasilkan hash MD5
#     return hashlib.md5(value.encode()).hexdigest()


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

def detailNews(request, hashid):
    # Ambil semua kategori
    cat = Category.objects.all()

    # Ambil berita terbaru (3 berita terbaru)
    latest_news = News.objects.all().order_by('-created')[:3]

    # Cari objek News berdasarkan hashed ID (bukan id)
    news = get_object_or_404(News, hashed=hashid)  # Menggunakan hashed untuk pencarian

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

            # Simpan entri terlebih dahulu untuk mendapatkan ID (PK)
            instance.save()

            # Setelah ID (PK) disimpan, kita dapat menggunakan ID tersebut untuk membuat hash yang konsisten
            raw_string = str(instance.pk)  # Menggunakan primary key ID entri untuk hashing
            instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
            # instance.hashed = hashlib.sha256(raw_string.encode('utf-8')).hexdigest()



            # Simpan kembali dengan hash yang telah dihitung
            instance.save()

            messages.success(request, 'News is added successfully.')

            # Redirect sesuai dengan tombol yang dipilih (save_and_add_another atau not)
            if 'save_and_add_another' in request.POST:
                return redirect('addnews')  # Misalnya ke halaman index
            return redirect('List-News')  # Kembali ke form tambah berita
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
    # Ambil data News berdasarkan hashed ID
    NewsData = get_object_or_404(News, hashed=hashid)  # Pastikan kamu mencari berdasarkan hashed ID

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
        'hashed': NewsData.hashed  # Menambahkan hashed ID ke context untuk ditampilkan
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

