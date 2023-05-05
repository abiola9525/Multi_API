from django.db import models

class Continent(models.Model):
    continent = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['continent']
           
    def __str__(self):
        return self.continent
    
class Country(models.Model):
    country = models.CharField(max_length=50, unique=True)
    capital = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    population = models.IntegerField()
    currency = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='flags', null=True, blank=True)
    language = models.CharField(max_length=50)
    m_ethnic = models.CharField(max_length=500)
    time_zone = models.CharField(max_length=50)
    calling_code = models.CharField(max_length=10)
    land_area = models.CharField(max_length=150)
    climate = models.CharField(max_length=500)
    goverment = models.CharField(max_length=500)
    gdp = models.CharField(max_length=50)
    date_of_independence = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['country']
    
    def __str__(self):
        return self.country
    
    
    
