from django import forms
from django.conf import settings


class SearchForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=250)
    page_count = forms.IntegerField(
        label='Page Count',
        min_value=1,
        max_value=settings.MAXIMUM_PAGE_COUNT,
        initial=settings.DEFAULT_PAGE_COUNT,
    )

class PlotForm(forms.Form):
    CHOICES = (
        ('article_author', 'Article Author'),
        ('article_tag', 'Article Tag')
    )

    plot_type = forms.CharField(
        label='Plot Type',
        widget=forms.Select(choices=CHOICES ),
        initial=settings.DEFAULT_PLOT_TYPE
    )
