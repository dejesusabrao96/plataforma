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
			# Automatically populate the hashed field
			instance.hashed = hash_md5(str(getlastid(ProjectImplementation)[1]))
			instance.save()  # Save the instance to the database
			messages.success(request, 'Project is added successfully.')
			if 'save_and_add_another' in request.POST:
				return redirect('addprojectimplementation')  # Redirect to add another news item
			return redirect('projectimplementation')  # Redirect to another view after saving
	else:
		form = ProjectImplementationForm()
	context = {
		'form':form,
	} 
	return render(request, 'projectimplementationform.html', context)

# def addReport(request):
# 	# Retrieve all years for the dropdown in the template
# 	year = Year.objects.all()

# 	if request.method == "POST" and 'upload_file' in request.FILES:
# 		# Get the last report ID and generate the hashed ID for the new report
# 		_, newid = getlastid(Report)
# 		hashid = hash_md5(str(newid))

# 		# Get the data from the form
# 		report = request.POST.get('report')
# 		year_report = request.POST.get('year')
# 		year_id = Year.objects.get(id=year_report)

# 		# Handle the uploaded file
# 		naran_file = request.FILES.get('upload_file')
# 		uploaded_filename = naran_file.name

# 		# Ensure the file is in PDF format
# 		if not uploaded_filename.endswith('.pdf'):
# 			messages.warning(request, 'The uploaded file should be in PDF format.')
# 			return redirect('add_report')  # Redirect to the same page to allow re-upload
        
# 		# Define the folder for storing reports based on the year
# 		year_folder = str(year_id)
# 		year_path = os.path.join('doc_files', year_folder)

# 		# Check if the folder exists, if not create it
# 		if not os.path.exists(year_path):
# 			os.makedirs(year_path)

# 		# Use Django's default file storage to save the uploaded file
# 		# The `upload_to` parameter of FileField is not needed here since the path is dynamic
# 		naran_file.name = os.path.join(year_folder, uploaded_filename)

# 		try:
# 			# Save the file with Django's file storage system
# 			report_instance = Report(
# 				report=report,
# 				years=year_id,
				
# 			)
# 			report_instance.save()

# 		except Exception as e:
# 			# Handle file save errors gracefully
# 			messages.error(request, f"An error occurred while saving the report: {e}")
# 			return redirect('add_report')

# 		# Send success messages and redirect based on form action
# 		if 'save' in request.POST:
# 			messages.success(request, 'Report added successfully.')
# 			return redirect('projectimplementation')
# 		elif 'save_and_add_another' in request.POST:
# 			messages.success(request, 'Report added successfully. You can add another.')
# 			return redirect('add_report')  # Assuming you want to keep the form open for adding another report

# 	context = {
# 		'year': year,
# 	}
# 	return render(request, 'reportForm.html', context)

def report_list(request):
    # Mengambil 'Year' yang dipilih dari request
    year_id = request.GET.get('year', None)
    
    # Jika ada 'year_id' dalam GET request, filter berdasarkan 'Year' yang dipilih
    if year_id:
        reports = Report.objects.filter(years__id=year_id)
    else:
        # Jika tidak ada filter tahun, tampilkan semua data
        reports = Report.objects.all()
    
    # Mengambil semua data tahun untuk dropdown atau filter
    years = Year.objects.all()

    return render(request, 'report_list.html', {'reports': reports, 'years': years})