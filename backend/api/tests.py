from datetime import datetime
from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from django.test import TestCase
from .models import AbsenseRecord, Employee, Record
from django.utils import timezone
from authentication.models import CoreUser

# models test
class EmployeeCreation(TestCase):

    def create_employee(self, first_name="Test", last_name="TestU",email ="test@gmail.com",password="testtest",password_confirmation="testtest"):
        if not CoreUser.objects.filter(
        email=email):
            return CoreUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        return False
    def delete_employee(self,email ="test@gmail.com"):
        CoreUser.objects.filter(email=email).delete()
        return True

    def test_employee_creation(self):
        w = self.create_employee()
        self.assertTrue(isinstance(w, CoreUser))
        self.assertTrue(isinstance(w.user, Employee))
        self.delete_employee()
    
    def test_employee_creation_with_wrong_mail(self):
        w = self.create_employee(email="dsadas")
        self.assertFalse(isinstance(w, CoreUser))
        
    
    def test_employee_creation_with_wrong_mail(self):
        w = self.create_employee()
        w = self.create_employee()
        self.assertFalse(isinstance(w, CoreUser))
        self.delete_employee()
    
    def test_flex_status(self):
        w = self.create_employee()
        emp = w.user
        req = emp.req_hours
        work = emp.work_hours
        self.assertEqual(emp.flex_status,emp.req_hours - emp.work_hours)
        

class RecordTest(TestCase):
    def create_employee(self, first_name="Test", last_name="TestU",email ="test1@gmail.com",password="testtest",password_confirmation="testtest"):
        if not CoreUser.objects.filter(
        email=email):
            return CoreUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        return CoreUser.objects.get(email=email)

    def test_record_create(self):
        w = self.create_employee().user
        r = Record.objects.create(employee = w)
        self.assertTrue(isinstance(r, Record))

    def test_absense_record_create(self):
        w = self.create_employee().user
        r = AbsenseRecord.objects.create(employee = w,comment="Hello",date=timezone.now(),end_date = timezone.now())
        self.assertTrue(isinstance(r, AbsenseRecord))   

        
    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    

    
    
