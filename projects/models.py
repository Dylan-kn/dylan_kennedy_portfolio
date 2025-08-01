from django.db import models
from django.utils.text import slugify
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage

PROJECT_TYPES = [
    ('pm', 'Project Management'),
    ('dev', 'Development'),
]

class Project(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, storage=MediaCloudinaryStorage())
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    ordering_index = models.PositiveIntegerField(default=0)
    project_type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPES,
        default='dev'
    )

class Resume(models.Model):
    title = models.CharField(max_length=100, default='My Resume')
    pdf = models.FileField(upload_to='resumes/', storage=RawMediaCloudinaryStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title