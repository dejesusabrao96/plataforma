from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from .models import *


class ProjectImplementationForm(forms.ModelForm):
    class Meta:
        model = ProjectImplementation
        fields = ['years','date','activity','amount_of_funds','Funder','contact_person']
        exclude = ['hashed']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('years', css_class='form-group col-md-6 mb-0'),
                Column('date', css_class='form-group col-md-6 mb-0'),
                Column('activity', css_class='form-group col-md-12 mb-0'),

                Column('amount_of_funds', css_class='form-group col-md-6 mb-0'), 
                Column('Funder', css_class='form-group col-md-6 mb-0'), 
                Column('contact_person', css_class='form-group col-md-6 mb-0'), 
                # Column('author', css_class='form-group col-md-6 mb-0'), 
                # Column('tags', css_class='form-group col-md-6 mb-0'), 
                # Column('created', css_class='form-group col-md-6 mb-0'), 
                # Column('updated', css_class='form-group col-md-6 mb-0'), 
            ),

            HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )

# class ReportForm(forms.ModelForm):
#     class Meta:
#         model = Report
#         fields = ['report','years']
#         exclude = ['naran_folder']
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields['years'].widget = forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('report', css_class='form-group col-md-6 mb-0'),
#                 Column('date', css_class='form-group col-md-6 mb-0'),
#                 Column('naran_file', css_class='form-group col-md-12 mb-0'),
#             ),

#             HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
#             HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
#         )

