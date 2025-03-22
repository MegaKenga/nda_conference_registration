from django.db import models

class Person(models.Model):
    class Manager(models.TextChoices):
        MARKAROV = 'Маркаров Иван'
        GARTSUEV = 'Гарцуев Александр'

    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    father_name = models.CharField(
        max_length=50,
        verbose_name='Отчество'
    )
    company_inn = models.CharField(
        max_length=50,
        verbose_name='ИНН организации'
    )
    person_email = models.EmailField(
        max_length=50,
        verbose_name='Email для связи'
    )
    person_phone = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Контактный телефон'
    )
    company_related_manager = models.CharField(
        choices=Manager.choices,
        verbose_name='Менеджер партнера'
    )

    class Meta:
        ordering = ['company_inn']
        verbose_name = 'Зарегистрированный партнер'
        verbose_name_plural = 'Зарегистрированные партнеры'

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name) + ' ' + str(self.father_name)
