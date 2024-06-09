from django.contrib import admin
from .models import Post

class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "published_date", "created_date")

admin.site.register(Post,MemberAdmin)