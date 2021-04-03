from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.URLField()
    PRODUCT_CHOICES = (
        ('E', "ELECTRONICS"),
        ('H', "HOME"),
        ('T', "TOY"),
        ('E', "EDUCATION")        
    )
    category = models.CharField(max_length=2, choices=PRODUCT_CHOICES)
    start_price = models.IntegerField()
    



class UserListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE)  


class Bid(models.Model):

    user_listing = models.ForeignKey(UserListing, default = 0, on_delete = models.CASCADE)
    user = models.ForeignKey(User,default = 0, on_delete=models.CASCADE)
    bid_price = models.IntegerField()


class Comment(models.Model):
    user_listing = models.ForeignKey(UserListing, default = 0,  on_delete = models.CASCADE)
    user = models.ForeignKey(User, default = 0,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["id",'title', 'description', 'image', 'category', 'start_price']
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class':'form-control'}),
            "image": forms.TextInput(attrs={'class':'form-control'}),
            "category": forms.Select(attrs={'class':'form-control'}),
            "start_price": forms.TextInput(attrs={'class':'form-control'})
        }


class BiddingForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price']
        widgets = {
            "bid_price": forms.TextInput(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            "comment": forms.TextInput(attrs={'class':'form-control'})

        }

