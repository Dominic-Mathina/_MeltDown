from django.contrib import admin
from .models import PlaylistUpload, PickSong
#from users.models import User


class PlayUploadAdmin(admin.ModelAdmin):
	"""docstring for PlayUploadAdmin"""
	def save_model(self, obj, form, change):
		obj.user = request.user
		obj.save()

class PickSongAdmin(admin.ModelAdmin):
	list_display = ['user']
		
admin.site.register(PlaylistUpload, PlayUploadAdmin)
admin.site.register(PickSong, PickSongAdmin)
