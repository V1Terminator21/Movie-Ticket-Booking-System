from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Show, Booking

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Show
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    show = ShowSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
