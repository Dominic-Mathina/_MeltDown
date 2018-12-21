from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from .models import PlaylistUpload, PickSong
from itertools import groupby
from users.forms import PlaylistForm, PickSongForm
from django.views.generic import (
	View,
	ListView, 
	CreateView, 
	FormView,
	UpdateView, 
	DetailView
	)
from songr.decorators import dejay_required
#from django.core.files.storage import FileSystemStorage


class PlayListView(ListView):
	model = PlaylistUpload
	template_name = 'songr/home.html'
	ordering = ['-date_posted']
	context_object_name = 'songs'

	# def get_queryset(self):
	# 	queryset=super(PlayListView, self).get_queryset()
	# 	queryset = queryset.filter(playlistupload__dejay__is_dejay=self.kwargs['is_dejay'])
	
	# def save_m2m():
	# 	if request.method == 'POST':
	# 		form = PickSongForm(request.POST)
	# 		if form.is_valid():
	# 			picksong = form.save(commit=False)
	# 			picksong.user = request.user
	# 			picksong.save()		
	# 			form.save_m2m()
	# 		else:
	# 			form = PickSongForm()		
	# 	return render(template_name, {'form':form}, context_instance=RequestContext(request))


class PickSongView(CreateView):
	model = PickSong
	form_class = PickSongForm
	template_name = 'songr/picks.html'
	#ordering = ['-date_posted']
	#context_object_name = 'songs'
	#queryset = PickSong.objects.prefetch_related('interests')
	success_url = ''

	def get_object(self):
		return self.request.user

	def form_valid(self, form):
		messages.success(self.request, 'Interests updated with success!')
		return super().form_valid(form)

# def playing(request):
# 	context = {
# 		'inters': PickSong.objects.all()
# 	}
# 	return render(request, 'songr/playing.html', context)

@method_decorator([login_required, dejay_required], name='dispatch')
class PlayCreateView(CreateView):
	form_class = PlaylistForm
	template_name = 'users/dj_profile.html'

	
	def form_valid(self, form):
		form.instance.dejay = self.request.user
		if self.request.FILES and form.is_valid:
			uploaded_fs = self.request.FILES.getlist('song_file')
			if len(uploaded_fs) >= 2:
				for f in range(len(uploaded_fs) - 1):
					PlaylistUpload.objects.create(song_file=uploaded_fs[f], dejay=self.request.user)
		return super().form_valid(form)

	

	# def song_inlist(self):
	# 	song_list = PlaylistUpload.objects.filter(playlistupload__dejay__is_dejay=dejay).values_list('playlistupload__song_file')
	# 	return song_list

class PlayDetailView(DetailView):
	model = PlaylistUpload

