from django.db import models
from abc import abstractmethod
from django.conf import settings

class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        abstract = True,
        ordering = ("pk")

    @abstractmethod
    def __str__(self):
        raise NotImplementedError('Implement __str__ method !!')


class Article(MyBaseModel):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Title')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ("id",)

    def __str__(self):
        return self.title


class Keyword(MyBaseModel):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Title')

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'
        ordering = ("id",)

    def __str__(self):
        return self.title


class SearchByKeyword(MyBaseModel):
    keyword = models.ForeignKey(Keyword, null=True, blank=True, related_name='searches', on_delete=models.CASCADE, verbose_name='Keyword')
    page_count = models.IntegerField(default=settings.DEFAULT_PAGE_COUNT, verbose_name='Page Count')

    class Meta:
        verbose_name = 'Search By Keyword'
        verbose_name_plural = 'Search By Keywords'
        ordering = ("id",)

    def __str__(self):
        return self.keyword.title


class ArticleSearchByKeywordItem(MyBaseModel):
    search_by_keyword = models.ForeignKey(
        SearchByKeyword,
        related_name='article_search_by_keyword_items',
        null=True, 
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Search By Keyword'
    )
    article = models.ForeignKey(
        Article,
        related_name='article_search_by_keyword_items',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Article'
    )
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Title')
    is_scraped = models.BooleanField(default=False, verbose_name='Is Scraped')

    class Meta:
        verbose_name = 'Article Search By Keyword Item'
        verbose_name_plural = 'Article Search By Keyword Items'
        ordering = ("id",)

    def __str__(self):
        return f'{self.title}({self.search_by_keyword.keyword.title})'

