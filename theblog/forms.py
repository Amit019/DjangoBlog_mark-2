from django import forms
from .models import Post, Category,Comment

choices= Category.objects.all().values_list("name",'name')

choices_list=[]
for item in choices:
    choices_list.append(item)

class PostFrom(forms.ModelForm):
    class Meta:
        model =Post
        fields =('title','author','category','body','snippets','thumbnail')

        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control','value':'','id':'user_name','type':'hidden'}),
           
            'category':forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'snippets':forms.Textarea(attrs={'class': 'form-control'}),
           

        }

class AddCommentFrom(forms.ModelForm):
    class Meta:
        model =Comment
        fields =('name','body',)

        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            
           

        }
