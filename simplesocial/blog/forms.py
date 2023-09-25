from django import forms
from blog.models import BlogPost,BlogComment

class BlogPostForm(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('title','text')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
    }    

class BlogCommentForm(forms.ModelForm):

    class Meta():
        model = BlogComment
        fields = ('text',)

    widgets = {
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
    }     