from django.shortcuts import render, redirect
from peliculas.models import Peliculas


def index(request):
  nombre_del_post = "error no hay data "
  data_peli = "no hay"
  cochallulo = ""
  try:
    if request.method == "POST":
      nombre_del_post = request.POST.get("nombre")      
      descripcion_del_post = request.POST.get("descripcion")   
      print(nombre_del_post)   
      data_peli = Peliculas.objects.get(nombre=nombre_del_post)
      
      if (data_peli.descripcion == descripcion_del_post):
        cochallulo = "las descripciones son iguales"
        contexto = {"nombrePost":nombre_del_post,"cochallulo":cochallulo}
        return redirect('/pagina2/')

      else:
        cochallulo = "las descripciones no son iguales"
        contexto = {"nombrePost":nombre_del_post,"cochallulo":cochallulo}
        return render(request,"index.html",contexto)
    else:
        contexto = {"nombrePost":nombre_del_post,"cochallulo":cochallulo}
        return render(request,"index.html",contexto)

  except:
    contexto = {"nombrePost":nombre_del_post,"cochallulo":cochallulo}
    return render(request,"index.html",contexto)
    






def registrarPelis(request):
  return render(request,"registrar.html")


def pagina2(request):
  peliculas = Peliculas.objects.all()
  contexto = {'listadoPeliculas':peliculas}
  return render(request,"pagina_2.html",contexto)

def pagina3(request):
  nombre_creador = "cachupin"
  contexto = {'creador':nombre_creador , 'parametro2':'tengotexto'}
  return render(request,"pagina_3.html",contexto)


def eliminarPelicula(request,id):
  PeliculaMala = Peliculas.objects.get(id=id)
  PeliculaMala.delete()
  return redirect('/pagina2/')

def agregarCualquerPelicula(request):

  Peliculas.objects.create(
                          nombre="objeto random",
                          descripcion="descripcion random",
                          disponible = 1,
                          director = "tarantulino")
  return redirect('/pagina2/')