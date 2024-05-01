from django.shortcuts import render
from .forms import SearchForm, PlotForm
from .tasks import search_task
from .plots import plot_article_author, plot_article_tag


def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            result = search_task.delay(
                keyword=form.cleaned_data['keyword'],
                page_count=form.cleaned_data['page_count'],
            )
            print('search_task results:', result)
    else:
        form = SearchForm()

    return render(request, 'templates/search.html', {'form': form})


def PlotView(request):
    if request.method == 'POST':
        form = PlotForm(request.POST)
        if form.is_valid():
            plot_type = form.cleaned_data['plot_type']
            if plot_type == 'article_author':
                plot_article_author()
            elif plot_type == 'article_tag':
                plot_article_tag()

    else:
        form = PlotForm()

    return render(request, 'templates/plot.html', {'form': form})
