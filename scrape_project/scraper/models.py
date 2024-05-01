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
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    thumbnail = models.TextField(null=True, blank=True, verbose_name='Thumbnail')
    text = models.TextField(null=True, blank=True, verbose_name='Text')
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
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    url = models.TextField(null=True, blank=True, verbose_name='Url')
    is_scraped = models.BooleanField(default=False, verbose_name='Is Scraped')

    class Meta:
        verbose_name = 'Article Search By Keyword Item'
        verbose_name_plural = 'Article Search By Keyword Items'
        ordering = ("id",)

    def __str__(self):
        return f'{self.title}({self.search_by_keyword.keyword.title})'

class Author(MyBaseModel):
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Name')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ("id",)

    def __str__(self):
        return self.name


class Tag(MyBaseModel):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name='Title')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ("id",)

    def __str__(self):
        return self.title

class ArticleTag(MyBaseModel):
    article = models.ForeignKey(
        Article,
        related_name='article_tags',
        on_delete=models.CASCADE,
        verbose_name='Article'
    )
    tag = models.ForeignKey(
        Tag,
        related_name='article_tags',
        on_delete=models.CASCADE,
        verbose_name='Tag'
    )

    class Meta:
        verbose_name = 'Article Tag'
        verbose_name_plural = 'Article Tags'
        ordering = ("id",)

    def __str__(self):
        return f'{self.article.title}_{self.tag.title}'

class ArticleAuthor(MyBaseModel):
    article = models.ForeignKey(
        Article,
        related_name='article_authors',
        on_delete=models.CASCADE,
        verbose_name='Article',
    )
    author = models.ForeignKey(
        Author,
        related_name='article_authors',
        on_delete=models.CASCADE,
        verbose_name='Author',
    )

    class Meta:
        verbose_name = 'Article Author'
        verbose_name_plural = 'Article Authors'
        ordering = ("id",)

    def __str__(self):
        return f'{self.article.title}_{self.author.name}'

