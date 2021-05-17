from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class blog(models.Model):
    title=models.CharField(max_length= 200) #제한된 문자열 필드
    writer= models.CharField(max_length= 100)
    pud_data= models.DateField() # 날짜와 시간을 저장해주는 필드
    body = models.TextField()
    image = models.ImageField(upload_to = 'blog/', blank = True, null = True)

    def __str__(self): #이름표
        return self.title
    
    def summary(self):
        return self.body[:100]
        