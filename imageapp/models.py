from django.db import models


# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    postimg = models.ImageField(upload_to='postimages')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + '-' + self.author

class Myupload(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="myimages")
    
    def __str__(self):
        return self.f_name
    
class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    doj = models.CharField(max_length=255)
    dob = models.CharField(max_length=255) 
    empphoto = models.FileField(upload_to='empphoto')
    
    @property
    def get_photo_url(self):
        if self.empphoto and hasattr(self.empphoto, 'url'):
            return self.empphoto.url
        else:
            return '/empphoto/noimg.jpg'
            
    
    def __str__(self):
        return str(self.empid) + ' ' + str(self.name) + ' ' +  str(self.contact) + ' ' +  str(self.email) + ' ' +  str(self.dept) + ' ' +  str(self.doj) + ' ' +  str(self.dob) + ' ' +  str(self.empphoto) 
    