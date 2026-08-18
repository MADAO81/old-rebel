from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('stories', 'Истории'),
        ('codex', 'Кодекс'),
        ('reviews', 'Разборы'),
        ('books', 'Книжная полка'),
        ('video', 'Видео'),
        ('about', 'Кто я'),
    ]

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='ЧПУ')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name='Рубрика')
    content = models.TextField(verbose_name='Текст')
    preview = models.TextField(max_length=300, verbose_name='Анонс')
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name='Обложка')
    youtube_url = models.URLField(blank=True, verbose_name='YouTube')
    tiktok_url = models.URLField(blank=True, verbose_name='TikTok')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Блог'
        ordering = ['-created_at']

    def __str__(self):
        return self.title