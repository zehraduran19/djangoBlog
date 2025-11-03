# Create your views here.
from django.shortcuts import render,  get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm


def home(request, category_id=None):
    posts = Post.objects.all()
    categories = Category.objects.all()
    for post in posts:
        print(post)
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category_id)
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': category
    })

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return redirect('post_detail', post_id=post.id)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})