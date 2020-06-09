import json
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Game
from .forms import SomeForm
def index(request):
  if request.method == 'GET':
    game_list = Game.objects.order_by('-name')
    template = loader.get_template('indexTemplate.html')
    context = {
          'game_list': game_list,
      }
    return HttpResponse(template.render(context, request))
  else:
    if request.method == 'POST' and request.is_ajax():
      try:
        data0 = json.loads(request.body.decode())  
        data = SomeForm(data0)
      except ValueError:
        return JsonResponse({'error': 'bla bla bla',})
      
      if data.is_valid():
        #assert False
        game = Game(name=data.cleaned_data['name'],                  
          description=data.cleaned_data['description'],                 
          release_date=data.cleaned_data['release_date'],              
            rating=data.cleaned_data['rating'],)
        game.save()
        return render(request,"indexTemplate.html",context = {'game_list' : Game.objects.order_by('-name')})
    else:
     return render(request,"indexTemplate.html",context = {'game_list' : Game.objects.order_by('-name')})


def Games(request,Game_id):
  game = Game.objects.get(pk=Game_id)
  NameOfGame = game.name
  DateOfRelease = game.release_date
  Description = game.description
  Img_name = game.img_name
  Rating = game.rating
  data = {"NameOfGame":NameOfGame, "DateOfRelease":DateOfRelease,"Img_name":Img_name,"Description": Description, "Rating":Rating}
  return render(request, "gameTemplate.html", context=data)
  
def sign_up(request):
  return render(request, "Sign_up.html")

def create(request):
    if request.method == 'POST':
         game = Game(name = request.POST.get('name'),description = request.POST.get('description'),release_date=request.POST.get('release_date'),rating = request.POST.get('rating'))
         game.save()
    return HttpResponseRedirect("/")

def update(request):
  if request.method == 'GET':
    game_list = list(Game.objects.all())
    n = len(game_list)
    context = n
  return HttpResponse(context,request)