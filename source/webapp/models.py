from django.utils import timezone

from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=2000, verbose_name='Вопрос')
    created_at = models.DateTimeField(verbose_name='Время создания', default=timezone.now)


    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"


    def __str__(self):
        return "{}. {}".format(self.pk, self.question)


class Choice(models.Model):
    option = models.TextField(max_length=2000, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='poll', on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return "{}. {}".format(self.pk, self.option)


