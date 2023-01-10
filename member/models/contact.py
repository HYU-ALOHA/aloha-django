from django.db import models
from config.models import TimeStampedModel


class Contact(TimeStampedModel):
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = verbose_name
    
    name = models.CharField(max_length=20, verbose_name='이름')
    student_id = models.CharField(db_index=True, max_length=20, verbose_name='학번')
    join_year = models.IntegerField(db_index=True, verbose_name='기수')
    
    mobile = models.CharField(max_length=20, null=True, verbose_name='연락처')
    email = models.EmailField(null=True, verbose_name='이메일')
    
    birth = models.DateField(null=True, verbose_name='생년월일')
    major = models.CharField(max_length=40, null=True, verbose_name='소속')
    grade = models.CharField(max_length=10, null=True, verbose_name='학년')
    study_class = models.CharField(max_length=20, null=True, verbose_name='분반')
    
    role = models.CharField(max_length=20, null=True, verbose_name='직급')
    status = models.CharField(max_length=20, null=True, verbose_name='회원 구분')
    
    memo = models.TextField(null=True, verbose_name='비고')

    boj_handle = models.CharField(max_length=20, null=True, verbose_name='BOJ 핸들')
