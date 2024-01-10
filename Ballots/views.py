from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import permissions


from .models  import Ballots, Comment, Topics  

from .serializers import BallotSerializer


# Create your views here.

class BallotView(mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):

    queryset= Ballots.objects.all()
    serializer_class = BallotSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = BallotSerializer(data=request.data)
        if serializer.is_valid():
            serializer["creator"] = user
            serializer.save()
        return Response(serializer.data)


