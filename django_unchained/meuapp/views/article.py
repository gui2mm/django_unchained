from django.shortcuts import render, get_object_or_404, redirect
from meuapp.models.article import Article
from meuapp.forms.article_form import ArticleForm


def list(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "meuapp/article_list.html", context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meuapp:article_list')
    else:
        form = ArticleForm()
    context = {"form": form}
    return render(request, "meuapp/article_create.html", context)

def delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    try:
        article.delete()
        # TODO: message
        return redirect('meuapp:article_list')
    except:
        context = {}
        # TODO: message
        return render(request, "meuapp/article_list", context)

def read(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {"article": article,}
    return render(request, "meuapp/article_read.html", context)

def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    try:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                # TODO: message
                return redirect('meuapp:article_list')
        else:
            form = ArticleForm(instance=article)
            context = {"form":form,
            "article_id":article_id}
            return render(request, "meuapp/article_edit.html", context)
    except:
        # TODO: message
        return redirect(request, "meuapp:article_list")