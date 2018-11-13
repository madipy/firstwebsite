from django.shortcuts import render

posts = [
    {
        'Author': 'Madison Mcdonald',
        'Title': 'Blog post 1',
        'Content': 'First post content',
        'Date_posted': 'Nov 11 2018'
    },
{
        'Author': 'Jane Doe',
        'Title': 'Blog post 2',
        'Content': 'Second post content',
        'Date_posted': 'Nov 12 2018'
    }


]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'Title': 'About'})

