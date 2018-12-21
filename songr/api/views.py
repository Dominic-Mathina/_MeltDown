from rest_framework.generics import ListAPIView
from .serializers import PlistSerializer
from songr.models import PlaylistUpload


class PlayListAPIView(ListAPIView):
	queryset = PlaylistUpload.objects.all()
	serializer_class = PlistSerializer