import matplotlib.pyplot as plt
from .models import Author, Tag, ArticleAuthor, ArticleTag
import matplotlib
matplotlib.use('TkAgg')


x_items = list()
articles = list()


def plot_article_author():
    authors = Author.objects.all()

    for author in authors:
        x_items.append(author.name)
        articles.append(len(ArticleAuthor.objects.filter(author=author).all()))

    plt.bar(x_items, articles, width=0.2)
    plt.xlabel('Authors')
    plt.xticks(rotation=45)
    plt.ylabel('Articles Count')
    plt.title('Plot Articles / Authors')

    plt.show()


def plot_article_tag():
    tags = Tag.objects.all()

    for tag in tags:
        x_items.append(tag.title)
        articles.append(len(ArticleTag.objects.filter(tag=tag).all()))

    plt.bar(x_items, articles, width=0.2)
    plt.xlabel('Tags')
    plt.xticks(rotation=45)
    plt.ylabel('Articles Count')
    plt.title('Plot Articles / Tags')

    plt.show()
