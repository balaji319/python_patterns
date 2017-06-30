from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from .models import Movie
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django .http import HttpResponse
from .forms import UserFoms

class IndexView(generic.ListView):
    template_name = 'user/index.html'
    def get_queryset(self):
        return Movie.objects.all()

class Index1View(generic.DetailView):
    model = Movie
    template_name = 'user/index1.html'


class MovieCreate(CreateView):
    model = Movie
    fields = ['actor','actor_movie','genre']

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['actor','actor_movie','genre']

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')

class  UserFormView(View):
    form_class = UserFoms
    template_name = 'user/Registration_form.html'

    #display balnk form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

     #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form': form})

        if form.is_valid():

           user = form.save(commit=False)

           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()


           user = authenticate(username=username , password=password)

           if user is not None:

              if user.is_active:
                 login(request,user)
                 return  render('index')

        return render(request, self.template_name, {'form': form})
