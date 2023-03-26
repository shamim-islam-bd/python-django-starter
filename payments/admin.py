from django.contrib import admin
from payments.models import pay_method

# Register your models here.

#it is used to display the organige model in admin panel
class pay_methodAdmin(admin.ModelAdmin):
    list_display = ['id','pay_id', 'pay_option', 'min_pay']
    class Meta:
        model = pay_method

#it is used to register the model in admin panel
admin.site.register(pay_method, pay_methodAdmin) 

