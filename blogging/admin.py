from django.contrib import admin
from .models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ("title", "author", "created_date", "published_date")
    search_fields = ("title", "text")
    list_filter = ("created_date", "published_date", "author")


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
    list_display = ("name", "description")
    search_fields = ("name", "description")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
