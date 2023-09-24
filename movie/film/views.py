from django.shortcuts import render
from film.models import Film
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from film.forms import filmform



# function based views here.
# def home(request):
#     k=Film.objects.all()
#     return render(request,'home.html',{'b':k})

# class based view
class movielistview(ListView):
    model=Film
    template_name="home.html"
    context_object_name="b"

# def add(request):
#     if (request.method=="POST"):
#         i=request.FILES['i']
#         t=request.POST['t']
#         d=request.POST['d']
#         n=request.POST['n']
#         f=request.POST['f']
#         r=request.POST['r']
#         b=Film.objects.create(cover=i,title=t, desc=d,name=n,date=f,rating=r)
#         b.save()
#         return home(request)
#     return render(request,'add.html')

class createview(CreateView):
    model=Film
    template_name="add.html"
    fields=["cover","title","desc","name","date","rating"]
    success_url=reverse_lazy("home")


# def details(request,p):
#         b=Film.objects.get(id=p)
#         return render(request,'details.html',{'b':b})

class detailview(DetailView):
    model=Film
    template_name="details.html"
    context_object_name="b"


# def delete_movie(request,p):
#     if request.method=="POST":
#         film= Film.objects.get(id=p)
#         film.delete()
#         return home(request)
#     return render(request,'delete.html')

class deleteview(DeleteView):
    model=Film
    template_name="delete.html"
    success_url=reverse_lazy("home")

# def update_movie(request,p):
#     film=Film.objects.get(id=p)
#     form=filmform(instance=film)
#     if(request.method=="POST"):
#         form=filmform(request.POST,request.FILES,instance=film)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request,'update.html',{'form':form})



class updateview(UpdateView):
    model=Film
    template_name="add.html"
    fields = ["cover", "title", "desc", "name", "date", "rating"]
    success_url = reverse_lazy("home")