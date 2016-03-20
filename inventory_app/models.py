from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=100, blank=False)
  last_modified = models.DateTimeField(auto_now=True)
  total = models.IntegerField(default=0)
  image = models.ImageField(upload_to="images", blank=True, null=True)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  outlets = models.ManyToManyField(Outlet)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=50, blank=False)

  def __str__(self):
    return self.name

class Outlet(models.Model):
  name = models.CharField(max_length=50, blank=False)

  def __str__(self):
    return self.name
