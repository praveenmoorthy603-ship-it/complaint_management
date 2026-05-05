from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
     
    def __str__(self):
        return self.name
    
class Complaint(models.Model):
    Status_Choices=[
        ('Pending','pending'),
        ('In progress','in progress'),
        ('Resolved','resolved')
    ]


    Priority_Choices=[
        ('Low','low'),
        ('Medium','medium'),
        ('High','high')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    status = models.CharField(max_length=50, choices=Status_Choices, default='Pending')
    priority = models.CharField(max_length=50, choices=Priority_Choices, default='Low')

    customer_name = models.CharField(max_length=50, null=True, blank=True )
    email = models.EmailField()
    location = models.CharField(max_length=50)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



