from datetime import date, datetime

from api.models import AbsenseRecord, Employee, Record
from rest_framework import serializers
from authentication.exceptions import CustomValidationError
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'req_hours',
            'work_hours',
            'email',
            'flex_status',
            'records_count'
        )

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = (
            'id',
            'arrive_time',
            'exit_time',
            'status',
            'date'

        )
       
class RecordCreateSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()

    def validate(self, attrs):
        errors = {}
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
            employee_id = validated_data['employee_id'],
            arrive_time = validated_data.get('arrive_time',datetime.now()),
            exit_time = validated_data.get('exit_time',None),
            date = validated_data.get('date',date.today())
        )
        return record

    def to_representation(self, instance):
        return RecordSerializer(instance, context=self.context).data

       
class RecordUpdateSerializer(serializers.Serializer):
    arrive_time = serializers.DateTimeField(required=False)
    exit_time = serializers.DateTimeField(required=False)
    def update(self, instance, validated_data):
        instance.arrive_time = validated_data.get('arrive_time',instance.arrive_time)
        instance.exit_time = validated_data.get('exit_time',instance.exit_time)
        instance.save()
        instance.status = 1
        return instance
    def to_representation(self, instance):
        return RecordSerializer(instance, context=self.context).data
    
class AbsenseRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbsenseRecord
        fields = (
            'id',
            'employee__id',
            'comment',
            'date',
            'end_date'

        )
       
class AbsenseRecordCreateSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()

    def validate(self, attrs):
        errors = {}
        if not attrs.get('employee_id'):
            errors['employee_id'] = ['employee is not set']

        if errors:
            raise CustomValidationError({'errors': errors}, 400)
        return attrs

    def create(self, validated_data):
        record = AbsenseRecord.objects.create(
            employee_id = validated_data['employee_id'],
            comment = validated_data.get('comment',''),
            date = validated_data.get('date',None),
            end_date = validated_data.get('end_date',None)
        )
        return record

    def to_representation(self, instance):
        return AbsenseRecordSerializer(instance, context=self.context).data

       
class AbsenseRecordUpdateSerializer(serializers.Serializer):
    date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    comment = serializers.CharField(required=False)
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date',instance.date)
        instance.end_date = validated_data.get('end_date',instance.end_date)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.save()
        return instance
    def to_representation(self, instance):
        return AbsenseRecordSerializer(instance, context=self.context).data
    
