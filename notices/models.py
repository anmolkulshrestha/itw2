from django.db import models
from django.utils import timezone
from django.urls import reverse


"""
    All the database entities of notices app are described in this module.
"""

class Notice(models.Model):
    """
     Notice model represents the notice uploaded by the college admin.

     Each notice should have a unique heading/title.

    """
    heading = models.CharField(max_length=100, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    author = models.CharField(max_length=100, default='Admin')

    def get_absolute_url(self):
        """
                :return: url of the corresponding notice on basis of heading as notices/{heading}
        """
        return reverse('notice', args=(self.heading,))

    def __str__(self):
        return f'{self.heading}'

    @staticmethod
    def get_notices_by_date():
        """
        :return: list of notices in descending order of date_posted (latest notice first)
        """
        return Notice.objects.all().order_by('-date_posted')

    @staticmethod
    def get_notice(heading):
        """
        :type heading: string
        :param heading: heading/title of notice
        :return: notice object with the heading passed as parameter
        """
        return Notice.objects.get(heading=heading)
