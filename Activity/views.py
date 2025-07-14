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

from rest_framework import viewsets
from .serializers import ActivitiesSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

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

           
            instance.save()

            raw_string = str(instance.pk) 
            instance.hashed = hashlib.md5(raw_string.encode('utf-8')).hexdigest()
           

            instance.save()

            messages.success(request, 'Activity is added successfully.')

            if 'save_and_add_another' in request.POST:
                return redirect('addactividade') 
            return redirect('actividade')  
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
