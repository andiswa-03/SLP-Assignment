from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from django.shortcuts import render
from .models import Article

from django.shortcuts import render
from blog.models import BlogPost  # Ensure BlogPost is correctly imported

def blog_list(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'blog/blog_list.html', {'posts': posts})

def index(request):
    articles = Article.objects.all()  # Get all articles
    return render(request, 'blog/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form})

def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_update.html', {'form': form})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
