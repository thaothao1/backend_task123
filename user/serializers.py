from rest_framework import serializers
from .models import CustomerUser
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [ 'username' , 'email' , 'password']
        extra_kwargs={
            'password':{
                "write_only" : True
            }
        }
    # class Meta:
    #     model = CustomerUser
    #     fields = ('username','email' ,  'password')
    
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'email')
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user