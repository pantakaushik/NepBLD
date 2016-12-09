from django.shortcuts import render, redirect
from django.views.generic import View
from Index.forms import RegisterClassForm,SearchForm
from Index.models import RegisterClass
# Create your views here.


class IndexView(View):
	template_name = 'index.html'
	form_class = SearchForm

	def get(self,request):
		form = self.form_class()
		# bloodgroup = self.request.GET.get('bloodgroup')
		# city = self.request.GET.get('city')
		# result = RegisterClass.objects.filter(bloodgroup=bloodgroup,city=city)
		return render(request, self.template_name,{'form':form})

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

class SearchView(View):
	template_name = 'search.html'
	form_class = SearchForm

	def get(self, request):
		form = self.form_class()
		bloodgroup = self.request.GET.get('bloodgroup')
		city = self.request.GET.get('city')
		result = RegisterClass.objects.filter(bloodgroup=bloodgroup,city=city)
		return render(request, self.template_name,{'form':form,'result':result,'bloodgroup':bloodgroup,'city':city})

