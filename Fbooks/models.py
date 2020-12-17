from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, default='')
    number = models.CharField(max_length=100, default='')
    fbooks = models.ForeignKey('Fbooks', related_name='fbooks_FRK', on_delete=models.CASCADE, blank=True)
    # fbooks는 Fbooks API 객체에 삽입될 컬럼. related_name이 필요하다.
    # 모델 설정 상으로 Fbooks모델은 User모델을 몰라야 한다.

    def __str__(self):
        return self.name

class Fbooks(models.Model):
    search = models.CharField(max_length=100, blank=True)
    #user모델이 삽입될 것임에도 모델상으로는 아무런 표시가 없다.
    #실제 삽입은 serialize.py 통해 이뤄진다. 

    def __str__(self):
        return 'Fbooks'


# # Create your models here.
