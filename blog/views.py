from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post, Author, Series, Subscriber, Comment, Category, Likes, Save
# Create your views here.


def home(request):
    posts_obj = Post.objects.all()[::-1][:2]

    context = {
        "object_list": posts_obj
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def store(request):
    return render(request, 'store.html', {})


def article(request, post_pk):
    p = Post.objects.get(pk=post_pk)
    context = {
        "post": p,
        "next_post": p.get_next_post(),
        "related_posts": p.get_related_posts(),
        "tweet": f'''    🚀‍🚀The Astronaut blog ‍🚀🚀
********************************************
📰 {p.title} 
********************************************
written by: ✍️{p.author}  read now: http://127.0.0.1:8000{ reverse('Article', kwargs={"post_pk":p.pk})}''',

    }
    return render(request, 'article.html', context)


def series(request):
    return render(request, 'series.html', {})


def posts(request):
    categories = Category.objects.all()
    category = request.GET.get("category", "all")
    page = request.GET.get("page", 1)

    if category == "all":
        p = Post.objects.all()
        current = "all"
    else:
        c = Category.objects.get(name=category)
        p = c.get_posts()
        current = category

    paginator = Paginator(p[::-1], 3)
    num_pages = paginator.num_pages
    num_list = []
    for num in range(num_pages):
        num_list.append(num + 1)

    p = paginator.page(page)
    if p.has_next():
        ne = int(page)+1

    else:
        ne = int(page)

    if p.has_previous():
        previous = int(page) - 1

    else:
        previous = int(page)
    context = {
        "categories": categories,
        "posts": p,
        "current": current,
        "page_nums": num_list,
        "page_num": int(page),
        "next": ne,
        "previous": previous,
    }
    return render(request, 'posts.html', context)
