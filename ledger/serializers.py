from rest_framework import serializers
from ledger.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
