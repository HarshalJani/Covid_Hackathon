from django.contrib import admin

# Register your models here.
from .models import HospDeptInventory
from .models import OrderInfo
from .models import SellerInfo
from .models import SellerItems

admin.site.register(HospDeptInventory)
admin.site.register(OrderInfo)
admin.site.register(SellerInfo)
admin.site.register(SellerItems)