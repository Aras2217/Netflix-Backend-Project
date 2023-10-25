from django.shortcuts import render, redirect, get_object_or_404
from appUser.models import Profile
from appUser.models import *
from appMy.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from bs4 import BeautifulSoup


def indexPage(request):
   context = {}
   return render(request, 'index.html',context)

def profileLogin(request, pid):
   
   if Profile.objects.filter(user=request.user, id=pid).exists():
      # kullanıcın tüm profillerinin plogin değerini false yapar
      Profile.objects.filter(user=request.user).update(plogin=False)
      profile = Profile.objects.filter(user=request.user).get(id=pid)
      profile.plogin = True
      profile.save()
      return redirect('indexBrowsePage1')
   else:
      messages.error(request, "Hatalı url yönlendirmesi")
      return redirect("loginUser")

def indexBrowsePage(request, cate="all", grid=4):
   # get hata verir önlem al, her kullanıcının kendi profillerine giriş yapabilmeli
   profile = Profile.objects.filter(user=request.user).get(plogin=True)
   
   movies = Movie.objects.none()
   categorys = Category.objects.none()
   
   if cate != "all":
        movies = Movie.objects.filter(category__title=cate)
   else:
        movies = Movie.objects.all()
        categorys = Category.objects.all()
        
   #To Bring Category title to site     
   category_title = cate
   
   if cate == "all":
      category_title = "Anasayfa"
   
   context = {
      "profile":profile,
      "movies" : movies,
      "cate" : cate,
      "grid" : grid,
      "categorys": categorys,
      "category_title": category_title,
   }
   return render(request, 'indexBrowse.html',context)

def create_listem_category(request, movie_id):
    # Get the movie and the 'listem' category
    movie_to_move = get_object_or_404(Movie, id=movie_id)
    #print(movie_to_move)
    listem_category = get_object_or_404(Category, title="Listem")
    #print(listem_category)

    # Check if the movie is already in the 'listem' category
    if movie_to_move.category == listem_category:

        return redirect('movie_already_in_listem')

    # Move the movie to the 'listem' category and save
    movie_to_move.category.add(listem_category)
    movie_to_move.save()

    updated_movie_category = movie_to_move.category.name
   # return render(request, "indexBrowse.html")
    return redirect('indexBrowsePage3')


