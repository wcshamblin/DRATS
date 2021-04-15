from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ticket

class ticketSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ticket
        fields = ('idstr', 'owner', 'ctime', 'email', 'fname', 'lname', 'ticket', 'status')

class UserSerializer(serializers.ModelSerializer):
    user_tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=ticket.objects.all())

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user