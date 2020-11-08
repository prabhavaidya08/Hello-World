from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    age= models.IntegerField()
    is_active= models.BooleanField(default=False)

    def save(self, **kwargs):
        self.fullclean()
        return super().save(**kwargs)
 