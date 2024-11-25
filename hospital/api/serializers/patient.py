from rest_framework import serializers
from api.models import Patient

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'date_of_birth', 'gender']


class PatientDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'date_of_birth', 'gender', 'contact_info']


class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'








# from rest_framework import serializers
#
# from api.models import Patient
#
#
# class PatientListSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     full_name = serializers.CharField()
#     date_of_birth = serializers.DateField()
#     gender = serializers.CharField()
#
#
# class PatientDetailedSerializer(serializers.ModelSerializer):
#    contact_info = serializers.CharField()
#
#
# class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
#
#       class Meta:
#           model = Patient
#           fields = '__all__'


