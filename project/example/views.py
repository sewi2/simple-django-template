from rest_framework import generics

from project.example import (
    models as example_models,
    serializers as example_serializers,
    filtersets as example_filtersets
)


class UserMixin:
    queryset = example_models.User.objects.all()
    serializer_class = example_serializers.UserSerializer
    filter_class = example_filtersets.UserFilterSet
    ordering = ('-id',)


class UserCreateListView(UserMixin,
                         generics.ListCreateAPIView):
    pass


class UserDetailView(UserMixin,
                     generics.RetrieveUpdateDestroyAPIView):
    pass
