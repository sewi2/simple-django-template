from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import Avatar, AccessKey, Profile, User, Site


class AvatarSerializer(serializers.ModelSerializer):
    image = serializers.CharField()

    class Meta:
        model = Avatar
        fields = ('id', 'image',)


class SiteSerializer(serializers.ModelSerializer):
    url = serializers.CharField()

    class Meta:
        model = Site
        fields = ('id', 'url',)


class AccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessKey
        fields = ('id', 'key',)


class ProfileSerializer(WritableNestedModelSerializer):
    # Direct ManyToMany relation
    sites = SiteSerializer(many=True)

    # Reverse FK relation
    avatars = AvatarSerializer(many=True)

    # Direct FK relation
    access_key = AccessKeySerializer(allow_null=True)

    class Meta:
        model = Profile
        fields = ('id', 'sites', 'avatars', 'access_key',)


class UserSerializer(WritableNestedModelSerializer):
    # Reverse OneToOne relation
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'profile', 'username',)
