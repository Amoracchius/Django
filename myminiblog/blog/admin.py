from django.contrib import admin
from .models import Article, Author, Comments

# Register your models here.

# admin.site.register(Article)
# admin.site.register(Author)
admin.site.register(Comments)


class ArticleInLine(admin.TabularInline):
    model = Article
    extra = 0


class CommentsInLine(admin.TabularInline):
    model = Comments
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'public_date')
    inlines = [CommentsInLine]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography')
    inlines = [ArticleInLine]




