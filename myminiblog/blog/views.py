from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Article, Author, Comments
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request,
                  'index.html',
                  )


class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 1


class ArticleDetailView(generic.DetailView):
    model = Article


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comments
    fields = ['content', ]

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Article, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.kwargs['pk'], })


class Registration(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)

    def form_invalid(self, form):
        return super(Registration, self).form_invalid(form)

    def get_success_url(self):
        return reverse("login")