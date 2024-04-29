from django.shortcuts import render
from .forms import SearchForm
from .tasks import search_task


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

