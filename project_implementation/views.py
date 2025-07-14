from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date
from core.utils import hash_md5, getlastid
from django.contrib import messages

# Create your views here.

def ProjectImplamentationList(request):
	project_implementation = ProjectImplementation.objects.all()
	context = {
		'project_implementation':project_implementation,
	}
	return render(request, 'project_implementation_list.html', context)

def addProjectImplementation(request):
	if request.method == 'POST':
		form = ProjectImplementationForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hash_md5(str(getlastid(ProjectImplementation)[1]))
			instance.save() 
			messages.success(request, 'Project is added successfully.')
			if 'save_and_add_another' in request.POST:
				return redirect('addprojectimplementation') 
			return redirect('projectimplementation') 
	else:
		form = ProjectImplementationForm()
	context = {
		'form':form,
	} 
	return render(request, 'projectimplementationform.html', context)

def report_list(request):
    year_id = request.GET.get('year', None)
    if year_id:
        reports = Report.objects.filter(years__id=year_id)
    else:
        reports = Report.objects.all()

    years = Year.objects.all()

    return render(request, 'report_list.html', {'reports': reports, 'years': years})
