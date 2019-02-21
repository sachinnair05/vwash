from django.db import models

# Create your models here.

class bookings(models.Model):
    status = ( ('Done','done'),('Pending','pending'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    area_code = models.IntegerField(null=True)
    phone_number = models.IntegerField()
    email_id = models.EmailField(null=True)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=30) 
    state = models.CharField(max_length=20,null=True)
    postal_code = models.IntegerField(null=True)
    country = models.CharField(max_length=20,null=True)
    pickup_date = models.DateField()
    pickup_time = models.CharField(max_length=100,null=True)
    details_of_service_request = models.CharField(max_length=200,null=True)
    special_instructions = models.CharField(max_length=200,null=True)
    is_deleted = models.IntegerField(default=0)
    status= models.CharField(max_length=20,choices=status,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Bookings"

class services(models.Model):
    order_id = models.ForeignKey(bookings,on_delete=models.CASCADE)
    service = models.CharField(max_length=30)
    is_deleted= models.IntegerField(default=0)        

    class Meta:
        db_table="Services"