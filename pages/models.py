from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели')
    code = models.CharField(max_length=20, verbose_name='Код (FXD, FXDB и т.д.)')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ (ссылка)')
    years = models.CharField(max_length=50, verbose_name='Годы выпуска')
    engine = models.CharField(max_length=100, verbose_name='Двигатель')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='bikes/', blank=True, null=True, verbose_name='Фото')
    photo_credit = models.CharField(max_length=200, blank=True, verbose_name='Автор фото')
    is_predecessor = models.BooleanField(default=False, verbose_name='Это предшественник? (FXR)')
    previous_model = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Предшественник (если есть)'
    )

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'

    def __str__(self):
        return f"{self.name} ({self.code})"

class ComparisonArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ (ссылка)')
    preview = models.TextField(max_length=300, verbose_name='Анонс')
    content = models.TextField(verbose_name='Полный текст')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Сравнительная статья'
        verbose_name_plural = 'Сравнительные статьи'
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email})"