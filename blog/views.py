from django.shortcuts import render


# Create your views here.

posts = [
    {
        "author": "Radu",
        "title": "BlogPost1",
        "content": "First post for the mans",
        "date_posted": "2022-09-21",
    },
    {
        "author": "Radu",
        "title": "BlogPost2",
        "content": "Second post for the mans",
        "date_posted": "2022-09-21",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
