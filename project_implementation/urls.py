from django.urls import path	
from .views import *

urlpatterns = [
	path('project-implementation', ProjectImplamentationList, name="projectimplementation"),
	path(' addprojectimplementation/', addProjectImplementation, name="addprojectimplementation"),
	# path(' addreport/', addReport, name="addreport"),
	path('reports/', report_list, name='report_list'),
]