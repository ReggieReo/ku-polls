import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    A class representing a question in a poll with attributes:
        question_text : The text of the question.
        pub_date : The date and time when the question was published.
        end_date : The date and time of the last day of voting period,
        if it is null, then voting is allowed anytime after pub_date.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    end_date = models.DateTimeField("end date", null=True, blank=True, default=None)

    def was_published_recently(self):
        """
        Checks if the question was published recently.
        Returns True if the question was published within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        """
        Returns a string text of the question.
        """
        return self.question_text

    def is_published(self):
        """
        Returns True if the current date is on or after question’s publication date.
        """
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """
        returns True if voting is allowed for this question.
        the current date/time is between the pub_date and end_date
        """
        now = timezone.now()
        if not self.is_published():
            return False
        if self.end_date is None or self.pub_date <= now <= self.end_date:
            return True
        return False


class Choice(models.Model):
    """
    A class representing a choice for a question in a poll with Attributes:
        question : The question to which this choice belongs.
        choice_text : The text of the choice.
        votes : The number of votes received for this choice.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string text of the choice.
        """
        return self.choice_text
