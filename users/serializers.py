from rest_framework import serializers
from .models import NewUser

class RegisteruserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewUser
        fields=('email', 'user_name', 'password')
        extra_kwargs={'password': {'write_only':True} }
        
        
    def create(self, validate_data):
        password= validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
        if password is None:
            instance.set_password(password) 
        instance.save()
        return instance