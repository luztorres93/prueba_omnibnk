
from .models import category
from .models import movie
from .forms import MovieForm
from django.views.generic import CreateView, UpdateView,DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required,  name='dispatch')
class movieList(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
         context = super(movieList, self).get_context_data(**kwargs)
         context['object_movie'] = movie.objects.all()
         
         context['object_category'] = category.objects.all()
         return context
   
class movieListFilter(TemplateView ):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
         context = super(movieListFilter, self).get_context_data(**kwargs)
        
         if kwargs['category_id'] != '0':
             context['object_movie'] = movie.objects.filter(category = kwargs['category_id'])
         else:
             context['object_movie'] = movie.objects.all()
             
         context['object_category'] = category.objects.all()
         return context

class movieRecommended(TemplateView ):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(movieRecommended, self).get_context_data(**kwargs)
        
        context['object_movie'] = movie.objects.filter(score__gt=8)
         
        context['object_category'] = category.objects.all()
        return context
     
class movieCreate(CreateView):
    model= movie
    form_class = MovieForm
    template_name = 'form_movie.html'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(movieCreate, self).form_valid(form)

    
class movieUpdate(UpdateView):
    model = movie
    form_class = MovieForm
    template_name = 'form_movie.html'

    
class movieDelete(DeleteView):
    model= movie
    template_name = 'form_delete_movie.html'



class movieSearch(TemplateView):

    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(movieSearch, self).get_context_data(**kwargs)
        q = self.request.GET.get('q', '')
        context['object_movie'] = movie.objects.filter(name__icontains=q)
         
        context['object_category'] = category.objects.all()
        return context