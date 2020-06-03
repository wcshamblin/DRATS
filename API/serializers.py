from rest_framework import serializers

from .models import WTB

class WTBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WTB
        fields = ('idstr', 'email', 'fname', 'lname', 'addr', 'city', 'zcode', 'ccnum', 'ccname', 'ccexpr', 'ccsecc')