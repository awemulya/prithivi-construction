from rest_framework import serializers
from user.models import AweUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AweUser
        fields = ('id', 'email','is_site_manager','is_active','is_admin')


class UserIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = AweUser
        fields = ('id', 'email')
        extra_kwargs = {
            "email": {
                "read_only": True,
                "required": False,
            },
            "id": {
                "read_only": False,
                "required": False,
            },
        }


