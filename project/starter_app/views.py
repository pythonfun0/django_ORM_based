from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

from .forms import CreateNewPost


def show_posts(request):
	context_dict = {
		'posts': Post.objects.all()
	}
	return render(request, 'starter_app/home.html', context_dict)


def post_detail(request, pk):
	context_dict = {
		'post': get_object_or_404(Post, pk=pk),
		'posts': Post.objects.all()
		}
	return render(request, 'starter_app/post_detail.html', context_dict)


def create_new_post(request):
	form = CreateNewPost()
	title = None
	slug = None
	date_of_creation = None
	content = None

	message = ''
	created = False
	if request.method == 'POST':
		form = CreateNewPost(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			slug = slugify(cd['title'])
			date_of_creation = timezone.now()
			content = cd['content']

			new_post = Post(title=title, slug=slug, date_of_creation=date_of_creation, content=content)
			if new_post.title in [item.title for item in Post.objects.all()]:
				message = "A post is already exist with the given title!"
				return render(request, 'starter_app/create_new_post.html', {'posts': Post.objects.all(),
															'form': form,
															'title': title,
															'slug': slug,
															'message': message,
															'created': created
															})
			else:
				created = True
				message = "The new post was successfully saved!"
				new_post.save()
				return render(request, 'starter_app/create_new_post.html', {'posts': Post.objects.all(),
															'message': message,
															'created': created
															})

	return render(request, 'starter_app/create_new_post.html', {'posts': Post.objects.all(),
																'form': form,
																'title': title,
																'slug': slug,
																'date_of_creation': date_of_creation,
																'created': created
																})


class EditPost(UpdateView):
	model = Post
	fields = ['title', 'content']
	success_url = reverse_lazy('starter_app:posts')





# def update_post(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	old_title = post.title
# 	old_content = post.content
# 
# 	form = CreateNewPost(request.POST, instance=Post.objects.get(pk=pk))
# 	updated = False
# 	
# 	if request.method == 'POST':
# 		form = CreateNewPost(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			title = cd['title']
# 			content = cd['content']
# 			if old_title == title and old_content == content:
# 				message = 'Nothing has changed in the post yet!'
# 				context_dict = {'posts': Post.objects.all(),
# 					'message': message,
# 					'updated': updated
# 				}
# 				return(request, 'starter_app/update_post.html', context_dict)
# 			else:
# 				update_post = Post(title=title, slug=slugify(cd['title']),
# 								   date_of_creation=timezone.now(), content=content)
# 				message = 'The post was successfully updated!'
# 				update_post.save()
# 				updated = True
# 				return(request, 'starter_app/update_post.html', {'posts': Post.objects.all(),
# 															'message': message,
# 															'updated': updated
# 															})
# 
# 	return render(request, 'starter_app/update_post.html', {
# 													'form': form,
# 													'title': post.title,
# 													'content': post.content,
# 													'updated': updated,
# 													# 'message': '',
# 													'post': post,
# 													'posts': Post.objects.all()
# 													})
