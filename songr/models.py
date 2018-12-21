from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils import timezone
from users.models import User
from django.urls import reverse

class PlaylistUpload(models.Model):
	song_file   = models.FileField(upload_to = 'videos/', null = True, verbose_name = "")
	date_posted = models.DateTimeField(default = timezone.now)
	dejay       = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE, related_name='playlist')

	def __str__(self):
		return str(self.song_file)
		
	def get_absolute_url(self):
		return reverse('djroll-home')


class PickSong(models.Model):
	user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	interests = models.ManyToManyField(PlaylistUpload, related_name='song_interests')	
		



# 	def clean_file(self):
# 		file = self.cleaned_data['song_file']
# 		return file
			

