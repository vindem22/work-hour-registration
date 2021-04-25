from django.db import models
from authentication.models   import CoreUser

# Create your models here.
class Employee(models.Model):
    req_hours = models.IntegerField(default=40)
    work_hours = models.IntegerField(default=0)
    auth_emp1 = models.ForeignKey(CoreUser,on_delete=models.DO_NOTHING,default=None,related_name="emp1",null=True)
    auth_emp2 = models.ForeignKey(CoreUser,on_delete=models.DO_NOTHING,default=None,related_name="emp2",null=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)


    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    
    @property
    def flex_status(self):
        return self.req_hours - self.work_hours
    
    @property
    def records_count(self):
        return self.records.count()


class Record(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="records")
    arrive_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True,default=None)
    status = models.SmallIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'


class AbsenseRecord(models.Model):   
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="absent_records") 
    comment = models.TextField()
    date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = 'AbsenseRecord'
        verbose_name_plural = 'AbsenseRecords'
    

