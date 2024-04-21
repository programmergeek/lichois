from rest_framework import viewsets
from lichois.visa.models import DisposalMoney
from ..serializers import DisposalMoneySerializer


class DisposalMoneyViewSet(viewsets.ModelViewSet):
    queryset = DisposalMoney.objects.all()
    serializer_class = DisposalMoneySerializer
