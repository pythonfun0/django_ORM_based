from django import forms
from .models import Post


class CreateNewPost(forms.Form):
	title = forms.CharField(max_length=50, required=True)
	slug = forms.SlugField(required=False)
	date_of_creation = forms.DateTimeField(required=False)
	content = forms.CharField(required=True, widget=forms.Textarea)


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'slug', 'content', 'date_of_creation']
