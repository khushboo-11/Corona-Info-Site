from django.contrib import admin

# Register your models here.


from covid.models import Questions,Answers,User

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(User)