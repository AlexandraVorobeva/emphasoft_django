from rest_framework import serializers
from .models import Profile_of_user


class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Profile_of_user
        fields='__all__'
