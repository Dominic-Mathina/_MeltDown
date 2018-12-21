from django.urls import path
from . import views
from songr.views import PlayListView, PlayCreateView, PlayDetailView, PickSongView


urlpatterns = [
	path('', PlayListView.as_view(), name = 'djroll-home'),
	path('profile/', PlayCreateView.as_view(), name = 'dj-profile'),
	path('pdetail/<int:pk>', PlayDetailView.as_view(), name = 'pdetail'),
	path('playing/', PickSongView.as_view(), name = 'picks'),
	#path('playing/',views.playing, name = 'uinterests' )
]