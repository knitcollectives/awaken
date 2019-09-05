from django.shortcuts import render, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm


# Create your views here.
def homepage(request):
    return render(request,
                  template_name='base.html',
                  context={"posts": Post.objects.all})

def services(request):
    return render(request,
                  template_name='services.html')
                  

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/blog")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/admin')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password. ")
    form = AuthenticationForm()
    return render(request,
                  template_name='login.html',
                  context={"form": form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("/blog")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}]")

        return render(request=request,
                      template_name="register.html",
                      context={"form": form})

    form = NewUserForm
    return render(request,
                  'register.html',
                  context={"form": form})


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        '-created_on'
    )
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
