from django.contrib import admin
from django.contrib.admin import register
from .models import Article, Keyword, SearchByKeyword, ArticleSearchByKeywordItem


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active",)
    list_editable = ("is_active",)


@register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active",)
    list_editable = ("is_active",)


@register(SearchByKeyword)
class SearchByKeywordAdmin(admin.ModelAdmin):
    list_display = ("id", "keyword", "page_count", "is_active",)
    list_editable = ("is_active",)


@register(ArticleSearchByKeywordItem)
class ArticleSearchByKeywordItemAdmin(admin.ModelAdmin):
    list_display = ("id", "search_by_keyword", "article", "is_scraped", "is_active",)
    list_editable = ("is_active", "is_scraped",)


