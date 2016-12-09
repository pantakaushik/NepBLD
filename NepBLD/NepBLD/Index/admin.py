from django.contrib import admin
from Index.models import RegisterClass
# Register your models here.
class RegisterClassAdmin(admin.ModelAdmin):
	list_display = ('first_name','middle_name','last_name','gender','bloodgroup','city','address','email','contact_number')

admin.site.register(RegisterClass, RegisterClassAdmin)