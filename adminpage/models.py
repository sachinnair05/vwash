from django.db import models

# Create your models here.

class admin(models.Model):
    user_id=models.EmailField(max_length=50)
    user_password = models.CharField(max_length=50)
    is_deleted= models.IntegerField()

    class Meta:
        db_table="admin"
