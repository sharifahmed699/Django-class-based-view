from django.shortcuts import render
from django.views import View
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse, reverse_lazy
from django.views.generic import( FormView,
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView)
from .forms import ArticleForm,CommentForm
from .mixins import PageTitleMixin,PublicMixin

from .models import Article,Comment

# Create your views here.


class ArticleListView(PageTitleMixin, PublicMixin, ListView):
    template_name='article/list_article.html'
    page_title='Article List Page'
    #queryset=Article.objects.filter(is_public=True)
    model=Article

    # def get_context_data(self,*args,**kwargs):
    #     context=super().get_context_data(*args,**kwargs)
    #     context['page_title']='Article List Page'
    #     context['articles']=context.get('object_list')
    #     return context



class ArticleDetailView(PageTitleMixin, DetailView):
    model=Article
    template_name='article/detail.html'
   # page_title='Article Detaile Page'
    query_pk_and_slug=True

    def get_object(self,queryset=None):
        obj=super().get_object(queryset=queryset)
        self.page_title=obj.title
        return obj



class ArticleCreateView(PageTitleMixin, CreateView):
    model=Article
    #fields=('title','body','is_public')
    form_class=ArticleForm
    success_url=reverse_lazy('articles:list')
    template_name='article/create_article.html'
    page_title='Create An Article'


class ArticleUpdateView(PageTitleMixin, UpdateView):
    model=Article
    form_class=ArticleForm
    template_name='article/update.html'
    success_url=reverse_lazy('articles:list')
    query_pk_and_slug=True

    def get_object(self,queryset=None):
        obj=super().get_object(queryset=queryset)
        self.page_title=obj.title
        return obj

class ArticleDeleteView(DeleteView):
    model=Article
    template_name='article/delete.html'
    success_url=reverse_lazy('articles:list')
    query_pk_and_slug=True


class CommentCreateView(CreateView):
    model=Comment
    #fields=('article', 'comment')
    form_class=CommentForm
    template_name='article/create_comment.html'
    # success_url=reverse_lazy('articles:list')
    # query_pk_and_slug=True

    def get_success_url(self):
        return reverse_lazy(
            'articles:detail',
            kwargs={'pk':self.object.article.id, 'slug':self.object.article.slug }
        )

    def get_form_kwargs(self, *agrs, **kwargs):
        kwargs=super().get_form_kwargs(*agrs, **kwargs)
        kwargs['article_id']=self.kwargs.get('pk')
        return kwargs



# class ArticleListView(TemplateView):
#     template_name='article/list_article.html'

#     def get_context_data(self,*args,**kwargs):
#         articles=Article.objects.all()
#         context=super().get_context_data(*args,**kwargs)
#         context['articles']=articles
#         return context

# class ArticleListView(View):
#     def get(self, request):
#         articles=Article.objects.all()
#         context={
#             'articles':articles
#         }
#         return render (request,'article/list_article.html', context)




# class ArticleFormView(FormView):
#     form_class=ArticleForm
#     template_name='article/create_article.html'

#     #success_url='/article/'

#     def get_success_url(self):
#         return reverse('articles:list')
    
#     def form_valid(self, form):
#         data=form.cleaned_data
#         print(data)
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         return super().form_invalid(form)


# class ArticleListView(View):
    
#     def get(self, request):
#         return render (request,'article/list.html')

#     def post(self, request):
#         pass


