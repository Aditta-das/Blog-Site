from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import *
def index(request):
    styleone = StyleOne.objects.order_by('-timestamp')

    context = {
        'styleone': styleone,
    }
    return render(request, 'index.html', context)

def create_post(request):
    if request.POST:
        blog = request.POST['blog']
        title = request.POST['title']
        image = request.POST['image']
        user_id = request.session['user_id']

        obj = StyleOne(blog=blog, title=title, image=image)
        obj.user_id_id = user_id
        obj.save()
        return redirect('index')
    return render(request, 'create_post.html')



def cate(request):
    styleone = StyleOne.objects.order_by('-timestamp')
    paginator = Paginator(styleone, 6)
    page = request.GET.get('page')
    paged_styleone = paginator.get_page(page)
    context = {
        'styleone': paged_styleone,
    }

    return render(request, 'category.html', context)


def details(request, details_id):
    if request.method == 'POST':
        user_id = request.session['user_id']
        massage = request.POST['massage']
        post_id = details_id
        query = Comment(massage=massage)
        query.user_id_id = user_id
        query.post_id_id = post_id
        query.save()
    list = get_object_or_404(StyleOne, pk=details_id)
    comment = Comment.objects.all().filter(post_id=details_id)
    styleone = StyleOne.objects.order_by('-timestamp')[:5]
    is_liked = False
    if list.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {
        'list': list,
        'is_liked': is_liked,
        'total_likes': list.total_likes(),
        'comment': comment,
        'styleone': styleone,
    }
    return render(request, 'details.html', context)

def like_post(request):
    post = get_object_or_404(StyleOne, id=request.POST.get('details_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())


def search(request):
    query_list = StyleOne.objects.order_by('-timestamp')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(Q(blog__icontains=keywords) | Q(category__icontains=keywords))

    context = {
        'styleone': query_list,
    }
    return render(request, 'search.html', context)

