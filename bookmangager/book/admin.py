from django.contrib import admin

# Register your models here.


from book.models import BookInfo, PersonInfo
admin.site.register(BookInfo)
admin.site.register(PersonInfo)

