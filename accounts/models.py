from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.EmailField(unique=True, null=False, max_length=254, verbose_name='이메일')
    nickname = models.CharField(max_length=200, blank=True, verbose_name='이름')
    phone = models.CharField(max_length=30, validators=[RegexValidator('^010[0-9]\d{6,7}$')], verbose_name='휴대폰') 
    address = models.TextField(blank=True, verbose_name='주소')
    GENDER_C = (
        ('', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_C, blank=True, verbose_name='성별')

    def __str__(self):
        return self.username

    class Meta:
        db_table='users'
        verbose_name='고객'
        verbose_name_plural='고객'
