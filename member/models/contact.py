from django.db import models
from config.models import TimeStampedModel


class Contact(TimeStampedModel):
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = verbose_name
    
    name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    
    mobile = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    
    birth = models.DateField(null=True)
    major = models.CharField(max_length=40, null=True)
    grade = models.IntegerField(null=True, verbose_name='학년')
    join_year = models.IntegerField(null=True, verbose_name='기수')
    study_class = models.IntegerField(null=True, verbose_name='반')

    boj_handle = models.CharField(max_length=20, null=True)