from django.utils import timezone

from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Question')
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now)


    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"


    def __str__(self):
        return "{}. {}".format(self.pk, self.question)


class Choice(models.Model):
    option = models.TextField(max_length=2000, verbose_name='Options')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return "{}. {}".format(self.pk, self.option)


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answer', on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name='Time of answer', default=timezone.now)
    choption = models.ForeignKey('webapp.Choice', related_name='choption', on_delete=models.CASCADE, verbose_name=" Chosen option")


