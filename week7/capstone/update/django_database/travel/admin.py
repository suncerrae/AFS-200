
# # Register your models here.
# from django.contrib import admin
# from travel.models import Question
# # Register your models here.

from django.contrib import admin

from .models import Question

admin.site.register(Question)


# class TravelAdmin(admin.ModelAdmin): 
#     list_display=("text", "created_on", "total_likes")
#     list_filter = ['created_on']
#     search_fields = ['text']

# admin.site.register(Question)
