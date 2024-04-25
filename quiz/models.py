from django.db import models
# from django.contrib.auth.models import User

from users.models import UserProfile


class TestSet(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    text = models.TextField()
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class UserTestResult(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='test_results')
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)
    correct_answers = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.user} - {self.correct_answers} / {self.total_questions} ({self.percentage}%)'