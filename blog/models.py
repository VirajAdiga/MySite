from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return f'# {self.caption}'

    class Meta:
        verbose_name_plural = 'tags##'


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="posts", null=True)
    excerpt = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
