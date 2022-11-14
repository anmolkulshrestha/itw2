from .models import Program
from notices.models import Notice

"""
    It contains the context which are shared by multiple templates.
    Instead of passing context from each view, they are registered here only once.
"""


def get_context_global_variable(request):
    """
           :type request: HTTPRequest
           :param request: carries request info
           :return: context which is available in all templates

    """
    programs = Program.objects.all()
    side_bar_notices = Notice.get_notices_by_date()[:5]

    context = {
        'programs': programs,
        'side_bar_notices': side_bar_notices,
    }
    return context
