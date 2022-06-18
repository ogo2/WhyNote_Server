from django.shortcuts import render
from .models import article, Comment
from profile_user.models import Profile
from .forms import *

def list_magazine(request):
    article_inf = article.objects.all()
    print(article_inf[0].name_user.profile.photo)
    return render(request, 'magazine/article_list.html', {'article': article_inf})
def add_article(request):
    if request.method == 'POST':
        add_form_article = Add_article(request.POST, request.FILES)
        print('fuck')
        if add_form_article.is_valid():
            add = add_form_article.save(commit=False)
            add.name_user = request.user
            add.share = ''.join(random.choice(string.ascii_letters) for _ in range(50))
            add.save()
    else:
        add_form_article = Add_article()
    return render(request, 'magazine/add_article.html', {'form': add_form_article})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def page_magazine(request, share):
    article_inf = article.objects.get(share=share)
    comment_info = Comment.objects.filter(post_name=article_inf.id)
    user_info = Profile.objects.get(user=article_inf.name_user)
    if request.user == True:
        article_inf.views.add(request.user)
    else:
        pass
    liks_user_true = False

    form_class = CommentForm
    print(request.POST.get('like'))
    if request.method == 'POST':
        if request.POST.get('this') == 'like':
            article_inf.like.add(request.user)
            comm_form = CommentForm()
            liks_user_true = False
        elif request.POST.get('this') == 'disslike':
            article_inf.like.remove(request.user)
            comm_form = CommentForm()
            liks_user_true = True
        else:
            comm_form = CommentForm(request.POST)
            print('fuck')
            if comm_form.is_valid():
                add = comm_form.save(commit=False)
                add.user_name = request.user
                add.post_name = article_inf
                # comm_form = comm_form.save(commit=False)
                print('fuck2')
                add.save()

    else:
        comm_form = CommentForm()
    print(article_inf.like.all())
    print(request.POST.get('this'))
    for user in article_inf.like.all():
        print(user)
        if user == request.user:
            print(1)
            liks_user_true = True
            break
        else:
            print(2)
            liks_user_true = False
    views_user_page = len(article_inf.views.all())
    liks = len(article_inf.like.all())
    return render(request, 'magazine/article_page.html', {'article': article_inf,
                                                          'user_info': user_info,
                                                          'comment_info': comment_info,
                                                          'comm_user_info': comment_info,
                                                          'form': comm_form,
                                                          'views_user_page': views_user_page,
                                                          'liks': liks,
                                                          'liks_user_true': liks_user_true})
