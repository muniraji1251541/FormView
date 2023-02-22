from django import forms
from app.models import *

class Djando_form(forms.Form):
	name=forms.CharField(max_length=50)
	age=forms.IntegerField()
	marks=forms.IntegerField()

class Model_form(forms.ModelForm):
	class Meta:
		model=Profile
		fields='__all__'