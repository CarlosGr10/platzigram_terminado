#Django
#from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

#Forms
from post.forms import PostForm

# Models
from post.models import Post

nombres = [{'titulo':'Hola',
            'usuario':{
            'Nombre':'Carlos',
            'apellido':'Garcia',
            'avatar':'https://picsum.photos/id/865/200/300',
            'edad':24
            },
            'fecha':'Dic-2018',
            'foto':'https://picsum.photos/id/1/200/300'
            },
            {'titulo':'Fuck yeha!',
            'usuario':{
            'Nombre':'Rick',
            'apellido':'Sanchez',
            'avatar':'https://picsum.photos/id/866/200/300',
            'edad':29
            },
            'fecha':'Dic-2019',
            'foto':'https://picsum.photos/id/10/200/300'
            },
            {'titulo':'Hoy es un bonito día #love',
            'usuario':{
            'Nombre':'Homero',
            'apellido':'Simpson',
            'avatar':'https://picsum.photos/id/800/200/300',
            'edad':25
            },
            'fecha':'Dic-2019',
            'foto':'https://picsum.photos/id/15/200/300'
            }
            ]

"""@login_required
def lista(request):
    posts = Post.objects.all().order_by('-created') #query ORM, el guion es para revertir
    return render(request,'posts/feed.html',{'posts': posts})"""

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'
    

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:app')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

"""
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:app')

    else:
        form = PostForm()
        
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
"""
    
