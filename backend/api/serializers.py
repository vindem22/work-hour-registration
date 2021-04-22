from datetime import date, datetime
from api.models import Employee, Record
from rest_framework import serializers
from authentication.exceptions import CustomValidationError
class EmployeeSerializer(serializers.ModelSerializer):
    flex_status = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'req_hours',
            'work_hours',
            'email',
            'flex_status'
        )

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = (
            'id',
            'arrive_time',
            'exit_time',
            'status',

        )
       
class RecordCreateSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()

    def validate(self, attrs):
        errors = {}
        print(attrs)
        if not attrs.get('employee_id'):
            errors['employee_id'] = ['employee is not set']
        else:
            if Record.objects.filter(employee_id=attrs.get('employee_id'),date=datetime.now()).exists():
                errors['record'] = ['Today record is created']
        if errors:
            raise CustomValidationError({'errors': errors}, 400)
        return attrs

    def create(self, validated_data):
        record = Record.objects.create(
            employee_id = validated_data['employee_id']
        )
        return record

    def to_representation(self, instance):
        return RecordSerializer(instance, context=self.context).data

       
# class RecordUpdateSerializer(serializers.ModelSerializer):
#     arrive_time = serializers.DateTimeField()
#     exit_time = serializers.DateTimeField()
#     def update(self, instance, validated_data):
