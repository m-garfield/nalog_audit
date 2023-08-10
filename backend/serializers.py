from rest_framework import serializers
from backend.models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'title', 'position_work']

    def __str__(self):
        return f"{self.id}, {self.first_name}, {self.last_name}, {self.title}, {self.position_work}"
