
from api.permissions import HasAccess
from api.paginations import CustomDefaultPagination
from api.serializers import AbsenseRecordCreateSerializer, AbsenseRecordSerializer, AbsenseRecordUpdateSerializer, EmployeeSerializer, RecordCreateSerializer, RecordSerializer, RecordUpdateSerializer
from api.models import AbsenseRecord, Employee, Record
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class EmployeeViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.RetrieveModelMixin,  mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.UpdateModelMixin,):

    permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = []
    pagination_class = CustomDefaultPagination
    
class EmployeeDetailViewSet(viewsets.GenericViewSet,  mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.UpdateModelMixin,):

    permission_classes = (AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = []
    pagination_class = CustomDefaultPagination

    @action(methods=['post'], 
        detail=False,
        url_name='users_record',
        url_path='users_record',)
    def users_record(self,request):
        user_id=request.data.get('employee_id')
        if Employee.objects.filter(id=user_id).exists():
            record = Employee.objects.get(id=user_id).records
            ser = RecordSerializer(record,many=True)
            return Response({'data': ser.data}, status=status.HTTP_200_OK)
        return Response({'data': "Employee with this id doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
    
class RecordViewSet(viewsets.GenericViewSet):  
    permission_classes = (HasAccess,)
    queryset = Record.objects.select_related('employee')
    serializer_class = RecordSerializer
    filter_backends = []
    pagination_class = CustomDefaultPagination
    

    @action(methods=['post'], 
        detail=False,
    )
    def record_create(self,request):
        data=request.data
        ser = RecordCreateSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def record_update(self,request):
        data = request.data
        record = Record.objects.get(id=data.get('record_id'))
        ser = RecordUpdateSerializer(record,data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data}, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False)
    def record_delete(self,request):
        pk = request.data.get('record_id')
        record = Record.objects.filter(id=pk).first()
        if record is not None:
            record.delete()
            return Response({'data':'success'}, status=status.HTTP_200_OK)
        return Response({'data':'Not Found'}, status=status.HTTP_404_NOT_FOUND)

class AbsenseRecordViewSet(viewsets.GenericViewSet):  
    permission_classes = (HasAccess,)
    queryset = AbsenseRecord.objects.select_related('employee')
    serializer_class = AbsenseRecordSerializer
    filter_backends = []
    pagination_class = CustomDefaultPagination
    

    @action(methods=['post'], 
        detail=False,
    )
    def record_create(self,request):
        data = request.data
        ser = AbsenseRecordCreateSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data}, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def record_update(self,request):
        data = request.data
        record = AbsenseRecord.objects.get(id=data.get('record_id'))
        ser = AbsenseRecordUpdateSerializer(record,data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'data': ser.data}, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False)
    def record_delete(self,request):
        pk = request.data.get('record_id')
        record = AbsenseRecord.objects.filter(id=pk).first()
        if record is not None:
            record.delete()
            return Response({'data':'success'}, status=status.HTTP_200_OK)
        return Response({'data':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
