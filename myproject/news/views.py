from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm
from django.utils import timezone

@login_required  # чтобы только залогиненный мог заходить на страницу с добавлением новости
def index(request):
    news = NewsPost.objects.all().order_by('-pub_date')

    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            news_post = form.save(commit=False)
            news_post.author = request.user  # ставим автора текущего пользователя
            news_post.pub_date = timezone.now()
            news_post.save()
            return redirect('news:news_home')
    else:
        form = NewsPostForm()

    return render(request, 'news/news.html', {'news': news, 'form': form})
