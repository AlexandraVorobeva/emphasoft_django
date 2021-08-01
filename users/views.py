from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Profile_of_user
from .license import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset=Profile_of_user.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Profile_of_user.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]
