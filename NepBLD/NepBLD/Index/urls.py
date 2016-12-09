from django.conf.urls import url
from Index.views import IndexView,RegisterView,SuccessView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register/$', RegisterView.as_view(), name='register'),
	url(r'^success/$', SuccessView.as_view(), name='success'),
]