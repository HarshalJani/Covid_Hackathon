from django.db import models
import uuid

# Create your models here.
class SellerInfo(models.Model):
    s_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_name = models.CharField(max_length=300)
    seller_city = models.CharField(max_length=300)
    seller_state = models.CharField(max_length=300)
    seller_zipcode = models.CharField(max_length=10)
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=14)
    seller_lat = models.CharField(max_length=300)
    seller_long = models.CharField(max_length=300)

    def __str__(self):
        return self.sellerInfo_text

class alerts(models.Model):
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_id = models.CharField(max_length=300)
    item_name = models.CharField(max_length=300)
    item_expiry = models.DateField()
    item_request_count = models.BigIntegerField()
    staff_notification = models.CharField(max_length=20)

class HospDeptInventory(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_count = models.BigIntegerField()
    item_name = models.CharField(max_length=300)
    item_expiry = models.DateField()
    item_desc = models.CharField(max_length=500)
    item_received_date = models.DateField()
    min_required = models.BigIntegerField()
    item_shipping_date = models.DateField()
    item_checked = models.BigIntegerField()
    item_defect = models.BigIntegerField()
    item_return = models.BigIntegerField()
    item_return_date = models.DateField()

    def __str__(self):
        return self.hospDeptInventory_text

class OrderInfo(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.BigIntegerField()
    order_item_name = models.CharField(max_length=300)
    order_item_id = models.CharField(max_length=300)
    order_item_count = models.BigIntegerField()
    #order_received_from = 
    #order_staff_id =
    seller_id = models.ForeignKey('SellerInfo', on_delete=models.CASCADE,) 
    #order_const =
    #payment_info = 

    def __str__(self):
        return self.orderInfo_text

class SellerItems(models.Model):
    seller_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seller_item_name = models.CharField(max_length=200)
    seller_item_count = models.BigIntegerField()
    seller_item_expiry = models.DateField()
    seller_item_category = models.CharField(max_length=200)
    seller_item_request_count = models.BigIntegerField()

    def __str__(self):
        return self.sellerItems_text