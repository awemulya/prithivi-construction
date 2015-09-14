from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from project.models import Project
from user.models import AweUser

__author__ = 'awemulya'


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'address', 'start_date', 'incharge')
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class InChargeSerializer(serializers.ModelSerializer):
    sites = SerializerMethodField('get_sites', read_only= True)

    class Meta:
        model = AweUser
        fields = ('id', 'name')
        depth = 2

        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def get_sites(self):
        # from django.db.models import Q
        sites = self.incharge_set.all()
        serializer = SitesSerializer(instance=sites, many=True)
        return serializer.data