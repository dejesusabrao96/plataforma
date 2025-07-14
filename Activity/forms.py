from django import forms
from froala_editor.widgets import FroalaEditor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from .models import *


class activityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['years','date','title','activity_content','category','image']
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('years', css_class='form-group col-md-6 mb-0'),
                Column('date', css_class='form-group col-md-6 mb-0'),
                Column('title', css_class='form-group col-md-12 mb-0'),

                Column('activity_content', css_class='form-group col-md-6 mb-0'), 
                Column('category', css_class='form-group col-md-6 mb-0'), 
                Column('image', css_class='form-group col-md-6 mb-0', onchange="myFunction()"),
                ),

            HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )

