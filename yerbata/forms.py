from django import forms
from .models import Post, Category, Comment

# choices = [('refreshing', 'refreshing'), ('sour', 'sour'), ]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'author', 'category', 'body', 'snippet')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog title..'}),
                   'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                   'author': forms.TextInput(
                       attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
                   # 'author': forms.Select(attrs={'class': 'form-control'}),
                   'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type blog stuff..'}),
                   'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type snippet..'}),
                   }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog title..'}),
                   'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type blog stuff..'}),
                   'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type snippet..'}),
                   }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author name..'}),
                   'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment..'}),
                   }
