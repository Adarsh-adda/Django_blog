from django.contrib import admin

from blog.models import Post


admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
