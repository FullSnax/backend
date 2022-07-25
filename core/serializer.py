from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
	class Meta:
		model = React
		fields = ['name', 'detail']

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['address', 'created_date']