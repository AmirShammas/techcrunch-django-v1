from django.contrib import admin
from django.contrib.admin import register
from .models import ArticleAuthor, ArticleTag, Tag, Author, Article, Keyword, SearchByKeyword, ArticleSearchByKeywordItem


@admin.action(description="Activate Selected Items")
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Inactivate Selected Items")
def inactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "thumbnail", "text", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("title", "description",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("title",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(SearchByKeyword)
class SearchByKeywordAdmin(admin.ModelAdmin):
    list_display = ("id", "keyword", "page_count", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "keyword",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("keyword",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(ArticleSearchByKeywordItem)
class ArticleSearchByKeywordItemAdmin(admin.ModelAdmin):
    list_display = ("id", "search_by_keyword", "article", "is_scraped", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "search_by_keyword",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("search_by_keyword", "article",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "name",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("name",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "title",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("title",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ("id", "article", "tag", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "tag",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("article", "tag",)
    actions = (activate_selected_items, inactivate_selected_items)


@register(ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "article", "author", "is_active",)
    list_editable = ("is_active",)
    list_display_links = ("id", "author",)
    list_filter = ("is_active", "created_at", "updated_at",)
    search_fields = ("article", "author",)
    actions = (activate_selected_items, inactivate_selected_items)

