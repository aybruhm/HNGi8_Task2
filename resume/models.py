from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="images/")
    linkedin = models.URLField()
    twitter = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    demo = models.URLField()
    tag = models.ManyToManyField("Tag", related_name="tags")

    def __str__(self):
        return self.title
