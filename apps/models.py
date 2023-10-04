from django.db import models

class Actor(models.Model):
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    full_name = models.CharField(verbose_name = 'имя актера', max_length=150, unique=True)

    def __str__(self):
        return f'{self.full_name}'
    

class Director(models.Model):

    class Meta:
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'

    full_name = models.CharField(verbose_name = 'имя режиссёра', max_length=150, unique=True)

    def __str__(self):
        return f'{self.full_name}'


class Genre(models.Model):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    name = models.CharField(max_length=100, verbose_name='название')
    year = models.IntegerField(verbose_name='год выпуска')
    rating = models.IntegerField(verbose_name='рейтинг')
    image = models.ImageField(upload_to='images/', verbose_name='обложка',)
    inner_image = models.ImageField(upload_to='inner_images/', verbose_name='внутренная обложка',)
    overview = models.CharField(max_length=1000, verbose_name='Краткое описание',)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='movies', )
    # content = models.TextField(verbose_name='контент', null=True) 
    director = models.ForeignKey(Director, verbose_name = 'Режиссёр', on_delete=models.CASCADE, related_name='movies',)
    # actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='movies')
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='автор', null=True)

    def __str__(self):
        return f'{self.name} - {self.year}'
    

class Comment(models.Model):

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарий'
    
    name = models.CharField(max_length=100, verbose_name='Имя и фамилия')
    text = models.TextField(verbose_name='текст')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                            verbose_name='Фильм', related_name='comments')
    date = models.DateField(verbose_name='дата добавление', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.movie.name}'
  

# class Series(models.Model):

#     class Meta:
#         verbose_name = 'Фильм'
#         verbose_name_plural = 'Фильмы'

#     name = models.CharField(max_length=100, verbose_name='название')
#     year = models.IntegerField(verbose_name='год выпуска')
#     rating = models.IntegerField(verbose_name='рейтинг')
#     image = models.ImageField(upload_to='images/', verbose_name='обложка',)
#     inner_image = models.ImageField(upload_to='inner_images/', verbose_name='внутренная обложка',)
#     overview = models.CharField(max_length=1000, verbose_name='Краткое описание',)
#     genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='movies', )
#     director = models.ForeignKey(Director, verbose_name = 'Режиссёр', on_delete=models.CASCADE, related_name='movies',)
#     # actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='movies')

#     def __str__(self):
#         return f'{self.name} - {self.year}'