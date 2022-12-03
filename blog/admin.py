from django.contrib import admin

from blog.models import Tag, Author, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ("tags", )
    list_display = ("title", "author")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
