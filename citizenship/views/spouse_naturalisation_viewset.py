from rest_framework import viewsets
from ..models import SpouseNaturalization
from lichois.citizenship.api.serializers import SpouseNaturalizationSerializer


class SpouseNaturalizationViewSet(viewsets.ModelViewSet):
    queryset = SpouseNaturalization.objects.all()
    serializer_class = SpouseNaturalizationSerializer
