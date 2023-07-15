from django.db import models
from django.contrib.auth.models import AbstractUser


class Profession(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    phone_code = models.PositiveIntegerField(verbose_name='Код телефона')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    phone_code = models.PositiveIntegerField()
    country = models.ForeignKey(Country, models.PROTECT, verbose_name='Страна')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Science(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Научная область'
        verbose_name_plural = 'Научные области'


class Phone(models.Model):
    number = models.CharField(max_length=100, verbose_name="Номер")
    city = models.ForeignKey(City, models.PROTECT, verbose_name='Город')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'


class Person(AbstractUser):
    middle_name = models.CharField(
        max_length=100,
        verbose_name='Отчество',
        blank=True,
        null=True
    )
    birth_of_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='images/avatars/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    profession = models.ForeignKey(
        Profession,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Профессия'
    )
    science = models.ForeignKey(
        Science, models.PROTECT,
        verbose_name='Научная область',
        blank=True,
        null=True
    )
    phone = models.ForeignKey(
        Phone, models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )
    city = models.ForeignKey(
        City, models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Город"
    )

    def __str__(self):
        return f'{self.username}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"


class Author(models.Model):
    person = models.OneToOneField(Person, models.SET_NULL, blank=True, null=True, verbose_name='Персон')
    first_name = models.CharField(max_length=123, blank=True, null=True, verbose_name='Имя')
    middle_name = models.CharField(max_length=123, blank=True, null=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=123, blank=True, null=True, verbose_name='Фамилия')

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.person:
            self.first_name = self.person.first_name
            self.middle_name = self.person.middle_name
            self.last_name = self.person.last_name
            return super(Author).save()
        else:
            return super(Author).save()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Project(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    science = models.ForeignKey(Science, models.PROTECT, verbose_name='Наука')
    year = models.DateField(verbose_name='Год')
    created_date = models.DateTimeField(auto_now_add=True)
    annotation = models.TextField(verbose_name='Аннотации')
    description = models.TextField(verbose_name='Описание')
    members = models.ManyToManyField(Person, verbose_name='Участники')
    image = models.ImageField(upload_to='images/project/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Material(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True, verbose_name='Проект')
    year = models.DateField(verbose_name='Год')
    created_date = models.DateTimeField(auto_now_add=True)
    annotation = models.TextField(verbose_name='Аннотации')
    description = models.TextField(verbose_name='Описание')
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    pdf = models.FileField(upload_to='files/materials/%Y/%m/%d/', verbose_name='PDF файл')
    youtube = models.URLField(verbose_name='Ютуб ссылка')
    image = models.ImageField(upload_to='images/materials/%Y/%m/%d/', blank=True, null=True, verbose_name='Название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


