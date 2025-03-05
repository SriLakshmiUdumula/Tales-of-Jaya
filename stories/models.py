from django.db import models
from django.utils.text import slugify

# Parvam model to represent a collection of stories
class Parvam(models.Model):
    name = models.CharField(max_length=100)  # Name of the Parvam
    description = models.TextField()  # Description of the Parvam

    def __str__(self):
        return self.name  # Display the name of the Parvam in the admin panel and elsewhere

# Story model to represent individual stories
class Story(models.Model):
    title = models.CharField(max_length=200)  # Title of the story
    slug = models.SlugField(unique=True, blank=True,null= True)  # Slug field for SEO-friendly URLs
    content = models.TextField()  # Full story content
    image = models.ImageField(upload_to='stories/')  # Story image
    parvam = models.ForeignKey(Parvam, on_delete=models.CASCADE, related_name='stories')  # Link to the Parvam
    likes = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title  # Display the title of the story in the admin panel and elsewhere
