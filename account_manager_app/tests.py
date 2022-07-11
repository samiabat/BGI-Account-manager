from django.test import TestCase

from account_manager_app.models import Employee

# Create your tests here.

def EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name='sami', email = 's@gmail.com', phone='+251921936070')
        Employee.objects.create(name = 'alemu', email= 'sa@gmail.com', phone = '+25191545885')
    def testEmployee(self):
        employee1 = Employee.objects.get(name = 'sami')
        employee2 = Employee.objects.get(name = 'alemu')
        self.assertEqual(employee1.email, 'the email is "s@gmail.com"')
        self.assertEqual(employee2.email, 'the email is "sa@gmail.com"')