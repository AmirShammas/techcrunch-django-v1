# Generated by Django 4.2 on 2024-04-29 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='SearchByKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('page_count', models.IntegerField(default=1, verbose_name='Page Count')),
                ('keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='scraper.keyword', verbose_name='Keyword')),
            ],
            options={
                'verbose_name': 'Search By Keyword',
                'verbose_name_plural': 'Search By Keywords',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ArticleSearchByKeywordItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Title')),
                ('is_scraped', models.BooleanField(default=False, verbose_name='Is Scraped')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_search_by_keyword_items', to='scraper.article', verbose_name='Article')),
                ('search_by_keyword', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_search_by_keyword_items', to='scraper.searchbykeyword', verbose_name='Search By Keyword')),
            ],
            options={
                'verbose_name': 'Article Search By Keyword Item',
                'verbose_name_plural': 'Article Search By Keyword Items',
                'ordering': ('id',),
            },
        ),
    ]