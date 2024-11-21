from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from news.models import *
from datetime import date
from core.utils import hash_md5, getlastid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
import hashlib

# Create your views here.
@login_required()
@allowed_users(allowed_roles=['Admin'])
def Actividade(request):
	group = request.user.groups.all()[0].name
	actividade = Activities.objects.all()
	context = {
		'actividades':actividade,

	}
	return render(request, 'actividade.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def addActivity(request):
    if request.method == 'POST':
        form = activityForm(request.POST, request.FILES)
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

            messages.success(request, 'Activity is added successfully.')

            # Redirect sesuai dengan tombol yang dipilih (save_and_add_another atau not)
            if 'save_and_add_another' in request.POST:
                return redirect('addactividade')  # Misalnya ke halaman index
            return redirect('actividade')  # Kembali ke form tambah berita
    else:
        form = activityForm()

    context = {
        'form': form,
    }
    return render(request, 'activityform.html', context)

def detailActivity(request, hashid):
	cat = Category.objects.all()
	latest_news = News.objects.all().order_by('-created')[:3]
	activity = get_object_or_404(Activities, hashed=hashid)
	
	context = {
		'latest_news': latest_news,
		'activity': activity,
		'cat' : cat,
		}
		
	return render(request, 'detailActivity.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def updateActivity(request, hashid):
    group = request.user.groups.all()[0].name
    # Ambil data News berdasarkan hashed ID
    ActivityData = get_object_or_404(Activities, hashed=hashid)  # Pastikan kamu mencari berdasarkan hashed ID

    if request.method == 'POST':
        form = activityForm(request.POST, instance=ActivityData)
        if form.is_valid():
            instance = form.save()
            messages.info(request, f'Activity is updated Successfully.')
            return redirect('actividade')
    else:
        form = activityForm(instance=ActivityData)

    context = {
        'sukuActive': "active",
        'page': "form",
        'group': group,
        'form': form,
        'hashed': ActivityData.hashed  # Menambahkan hashed ID ke context untuk ditampilkan
    }

    return render(request, 'activityform.html', context)

@login_required()
@allowed_users(allowed_roles=['Admin'])
def DeleteActivity(request, hashid):
	group = request.user.groups.all()[0].name
	activity = get_object_or_404(Activities, id=hashid)
	# an = news.news
	activity.delete()
	messages.warning(request, f'Activity is Deleted Successfully.')
	return redirect('actividade')

def Report(request):
	context = {

	}
	return render(request, 'report.html', context)