from django.conf.urls import url
from Index.views import IndexView,RegisterView,SuccessView, SearchView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register/$', RegisterView.as_view(), name='register'),
	url(r'^success/$', SuccessView.as_view(), name='success'),
	url(r'^searchdata/$', SearchView.as_view(), name='search'),


]