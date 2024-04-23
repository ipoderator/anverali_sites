from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField

from anverali_sites.settings import CUSTOMER_OR_PERFORMER


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters,'
            'digits and @/./+/-/_ only.'
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    first_name = models.CharField(
        _('first name'), max_length=150,
        validators=[RegexValidator(
            regex='^[^$%^&#:;!]+$',
            message=_('Имя не может содержать символы: $%^&#:;!'),
            code='invalid_first_name'
        )])
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(
        _('email address'),
        max_length=254,
        unique=True)
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        blank=True,
    )
    slug = AutoSlugField(
        populate_from='username',
        unique=True,
        db_index=True,
        verbose_name='URL',
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    resume_file = models.FileField(
        upload_to='media/%Y/%m/%d/',
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=30,
        choices=CUSTOMER_OR_PERFORMER,
        verbose_name='Роль',
        default='Исполнитель'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(
                ('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Experience(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
    )
    start_date = models.DateField(
        verbose_name='Дата зачисления'
    )
    end_date = models.DateField(
        verbose_name='Дата увольнения'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    expected_salary = models.PositiveIntegerField(
        verbose_name='Ожидаемая ЗП',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    skills = SortedManyToManyField(
        'Skill',
        verbose_name='Навыки'
    )
    slug = AutoSlugField(
        populate_from='slug_create',
        unique=True,
        verbose_name='URL',
        max_length=250
    )

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return f'{(self.user)}-{self.title}'

    def slug_create(self):
        return f'{(self.user)}-{self.title}'


class Vacancies(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    salary_min = models.PositiveIntegerField(
        verbose_name='минимальная_ЗП',
        blank=True,
        null=True
    )
    salary_max = models.PositiveIntegerField(
        verbose_name='максимальная_ЗП',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    skills = SortedManyToManyField(
        'Skill',
        verbose_name='Навыки'
    )
    slug = AutoSlugField(
        populate_from='slug_create',
        unique=True,
        verbose_name='URL',
        max_length=250
    )
    date = models.DateTimeField(
        verbose_name='Дата',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return f'{(self.user)}-{self.title}'

    def slug_create(self):
        return f'{(self.user)}-{self.title}'


class Skill(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=70,
        unique=True
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        verbose_name='URL',
        max_length=70
    )

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title
