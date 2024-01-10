from rest_framework import serializers

from .models import Ballots, Comment


class BallotSerializer(serializers.ModelSerializer):
    """
    Ballot serializer
    """
     

    class Meta:
        model = Ballots
        fields="__all__"
        



class CommentSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Comment
        fields="__all__"
