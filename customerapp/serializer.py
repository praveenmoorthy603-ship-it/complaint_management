from .models import Complaint 
from rest_framework import serializers


class ComplaintSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name', read_only=True) # only for categroy name view instead of ID
    class Meta:
        model = Complaint
        fields = "__all__"



from django.contrib.auth.models import User

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self, validated_data):
            user = User.objects.create_user(username=validated_data["username"],
                                           password=validated_data["password"])
            return user

