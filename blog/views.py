from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import SendingForm
from django.shortcuts import render
from django.core.mail import send_mail

def post_list(request):
    posts = Post.objects.all
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})


def index(request):
    return render(request, 'blog/index.html', {})


def sight(request):
    return render(request, 'blog/sight.html', {})

def send(request):
    if (request.method == 'POST'):
        form = SendingForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            send_mail(
                '{} {}'.format(name, email),
        'test meassage',
                'officialabzal@gmail.com',
                ['gazizktk@gmail.com', 'example@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'blog/result.html', {
                     'name': form.cleaned_data['name'],
               'email': form.cleaned_data['email'],
        })
    else:
        form = SendingForm()
    return render(request, 'blog/send.html', {'form':form});
