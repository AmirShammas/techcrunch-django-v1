from celery import shared_task
from django.conf import settings

from .handler import ScraperHandler
from .models import SearchByKeyword, Keyword, ArticleSearchByKeywordItem


@shared_task()
def search_task(keyword, page_count=settings.DEFAULT_PAGE_COUNT):
    print(f'Search for keyword "{keyword}" started !!')

    keyword, _ = Keyword.objects.get_or_create(title=keyword)

    search_by_keyword = SearchByKeyword.objects.create(
        keyword=keyword,
        page_count=page_count,
    )

    scraper_handler = ScraperHandler(base_url=settings.BASE_URL, search_url=settings.SEARCH_URL)
    scraped_items_count = scraper_handler.search_by_keyword(search_by_keyword_instance=search_by_keyword)

    print(f'Search for keyword "{keyword}" finished!!')

    return {
        'keyword': keyword,
        'page_count': page_count,
        'scraped_items_count': scraped_items_count,
        'status': 'Finished',
    }
