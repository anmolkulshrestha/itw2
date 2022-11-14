from django.shortcuts import render
from .models import Notice
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def notice(request):
    """
    :type request: HTTPRequest
    :param request: carries request info

    -> All the notices from the database are paginated with 8 notice objects in a page.
    -> Page number is specified as the query parameter, notices?page=4.
    -> If page number is not given, default is 1.
    -> All the notices of the specified page number is passed to notices-list.html.

    :return: renders notices-list.html with all the notices of specified page number
    """
    page_num = request.GET.get('page', 1)
    notices = Notice.get_notices_by_date()
    paginator = Paginator(notices, 8)  # 8 notices in one page

    try:
        notices = paginator.page(page_num)

    except PageNotAnInteger:
        notices = paginator.page(1)

    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    return render(request, 'notices/notices-list.html', {'notices': notices})


def single_notice(request, heading):
    """
    :type request: HTTPRequest
    :param request: carries request info
    :type heading: string
    :param heading: heading/title of notice
    :return: renders notice.html with notice of given heading
    """
    return render(request, 'notices/notice.html', {'notice': Notice.get_notice(heading)})
