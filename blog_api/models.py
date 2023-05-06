from django.db import models

# Create your models here.
class Blog_Category(models.Model):
    title = models.CharField(max_length=50)
    categoty_image = models.ImageField(upload_to='blog_cat/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'
        
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    author = models.CharField(max_length=50)
    metades = models.CharField(max_length=150)
    image_title = models.ImageField(upload_to='title-image/', null=True, blank=True)
    content = models.TextField()
    images0 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images1 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images2 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images3 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images4 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images5 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images6 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images7 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images8 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    images9 = models.ImageField(upload_to='blog-image/', null=True, blank=True)
    file1 = models.FileField(upload_to='blog-docs/')
    file2 = models.FileField(upload_to='blog-docs/')
    file3 = models.FileField(upload_to='blog-docs/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    
    
    