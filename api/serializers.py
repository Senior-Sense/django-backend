from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer) :
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required = True ,
        write_only = True ,
        validators = [validate_password]
    )
    password2 = serializers.CharField(write_only = True , required = True )

    class Meta :
        model = User
        fields = ['username','password','email','first_name','last_name' , 'password2']

    def validate(self, attrs) :
        if attrs['password'] != attrs['password2'] :
            raise serializers.ValidationError({'password' : 'Passwords do not match please try again'})
        return attrs

    def create(self , validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def validate(self, data):
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError("New password cannot be the same as the old password.")
        return data
