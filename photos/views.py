from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/list.html'
    context_object_name = 'photos'
    ordering = ['upload_date']


class PhotoTagListView(PhotoListView):
    template_name = 'photos/taglist.html'
    # Custom method
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/detail.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image', 'tags']
    template_name = 'photos/create.html'
    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UserIsSubmitter(UserPassesTestMixin):
    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))
    
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().author
        else:
            raise PermissionDenied('Sorry you are not allowed here')
        

class PhotoUpdateView(UserIsSubmitter, UpdateView):
    template_name = 'photos/update.html'
    model = Photo
    fields = ['title', 'description', 'tags']
    success_url = reverse_lazy('photo:list')


class PhotoDeleteView(UserIsSubmitter, DeleteView):
    template_name = 'photos/delete.html'
    model = Photo
    success_url = reverse_lazy('photo:list')  

