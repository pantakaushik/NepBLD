from django import forms
from Index.models import RegisterClass

class RegisterClassForm(forms.ModelForm):

	class Meta:
		model = RegisterClass
		fields = "__all__"