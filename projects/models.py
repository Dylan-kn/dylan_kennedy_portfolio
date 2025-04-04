from django.db import models
from django.utils.text import slugify

class Project(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField()
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    ordering_index = models.PositiveIntegerField(default=0)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title