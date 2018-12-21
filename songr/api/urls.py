from songr.api.views import PlayListAPIView
from django.urls import path

urlpatterns = [
	path('', PlayListAPIView.as_view(), name = 'playlt-api'),

]