from datetime import date

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=254)
    tagline = models.TextField()


    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Entry(models.Model):
    headline = models.CharField(max_length=254)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body_text = models.TimeField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    author = models.ManyToManyField(Author)
    number_of_comments = models.PositiveIntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
