from django.shortcuts import render, redirect
from django.views.generic import View
from Index.forms import RegisterClassForm
# Create your views here.


class IndexView(View):
	template_name = 'index.html'

	def get(self,request):
		return render(request, self.template_name )

class RegisterView(View):
	template_name = 'register.html'
	form_class = RegisterClassForm

	def get(self, request, *args,**kwargs):
		form = self.form_class()
		return render(request, self.template_name,{'form':form})
		

	def post(self, request, *args,**kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('/success/')
		return render(request,self.template_name,{'form':form})
class SuccessView(View):
	template_name='success.html'

	def get(self, request):
		return render(request, self.template_name)