from rest_framework.serializers import ModelSerializer

from songr.models import PlaylistUpload


class PlistSerializer(ModelSerializer):
	class Meta:
		model = PlaylistUpload
		fields = ['dejay', 'date_posted', 'song_file']