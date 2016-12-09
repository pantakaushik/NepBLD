from django.conf.urls import url
from Index.views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view()),
]