from django.db import models
import json

# Create your models here.

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    sage = models.IntegerField()
    sdepartment = models.CharField(max_length=100)
    ssubject = models.TextField(default='[]')

    @property
    def list(self):
        return json.loads(self._list)

    @list.setter
    def list(self, value):
        self._list = json.dumps(self.list + value)

    class Meta:
        db_table = "student"
