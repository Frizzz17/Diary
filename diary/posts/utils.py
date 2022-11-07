from django.core.paginator import Paginator


def paginator(request, posts):
    pagin = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = pagin.get_page(page_number)

    return page_obj