import datetime
from django.test import TestCase


# Create your tests here.
from django.utils import timezone

from emerline.task.models import Task


class TaskTests(TestCase):
    def test_duedate_after_now(self):
        time = timezone.now() - datetime.timedelta(days=1)
        past_task = Task(dueDate=time)
        self.assertEqual(past_task.duedate_after_now(), False)
