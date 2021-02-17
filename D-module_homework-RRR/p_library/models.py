from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=160, verbose_name='Имя')
    birth_year = models.SmallIntegerField(verbose_name='Дата рождения')
    country = models.CharField(max_length=2, verbose_name='Страна рождения')

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.CharField(max_length=160, verbose_name='Название')

    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=160, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    year_release = models.SmallIntegerField(verbose_name='Дата издания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    copy_count = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Издательство',
                 null=True, blank=True, related_name='books')
    friend = models.ForeignKey('Friend', on_delete=models.CASCADE, related_name='books',
                               verbose_name='Другу отдана', null=True, blank=True)

    image = models.ImageField(upload_to='book_photos/', blank=True, null=True,
                              verbose_name='Фото')

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/book_photos/book_default.jpg"

    def __str__(self):
        return self.title


class Friend(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')



    def __str__(self):
        return self.full_name
