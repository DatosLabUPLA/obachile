from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from django import template
# Create your views here.
def index(request):
    

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'index.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'index.html' )
        return HttpResponse(html_template.render(context, request))


def charts(request):
    labels = []
    dat = []
    label = []
    dato = []
    lab =[]
    da =[]
    labe =[]
    datas =[]

    queryset = Autor.objects.order_by('-citas')[:15]
    

    dataset = Autor.objects.all()[:15] 
    for autores in dataset:
        labels.append(autores.nombre_autor)
        dat.append(autores.citas)

    query = AutorPaper.objects.all()[:15]
    for autor in query:
        labe.append(autor.año)
        datas.append(autor.citado_por)
    quer = AutorPaper.objects.all()[:15]
    for autor in query:
        lab.append(autor.revista)
        da.append(autor.citado_por)

    querys = AutorPaper.objects.all()[:15]
    for autor in querys:
        label.append(autor.titulo_paper)
        dato.append(autor.citado_por)

    return render(request, 'index.html', {
        'queryset': queryset,
        'label': label,
        'dato': dato,
        'labels': labels,
        'dat': dat,
        'dataset': dataset,
        'da': da,
        'lab': lab,
        'datas': datas,
        'labe': labe,
    })
def chartsperfiles(request):
    
    label = []
    dato = []
      
    perfils = Autor.objects.all()
    dataset = Citas.objects.all()[:15]
    for autores in queryset:
        label.append(autores.year_hist)
        dato.append(autores.citas_hist)


    return render(request, 'user-profile-lite.html', {
        'label': label,
        'dato': dato,
        
    })
def table(request):
    tabla1 = Autor.objects.order_by('-todas_citas')[:10]
    tabla2 = AutorPaper.objects.order_by('-citado_por')[:10]
    return render(request, 'tables.html', {'tabla1' : tabla1, 'tabla2' : tabla2})
def table2(request):
    tabla1 = Autor.objects.order_by('-todas_citas')[:10]
    tabla2 = AutorPaper.objects.order_by('-citado_por')[:10]
    return render(request, 'tables2.html', {'tabla1' : tabla1, 'tabla2' : tabla2})
def perfil(request, id):
    perfils = Autor.objects.get(id=id)
    perfils2 = AutorPaper.objects.get(a_id=id)
    label = []
    dato = []

    dataset = Citas.objects.all()[:35]
    for autores in dataset:
        label.append(autores.year_hist)
        dato.append(autores.citas_hist)
    
    context = { 'perfils': perfils, 'label': label,
        'dato': dato,'perfils2': perfils2 }
    return render(request, 'user-profile-lite.html', {'perfils': perfils, 'label': label,
        'dato': dato,})

def perfil2(request, a_id):
   
    perfils2 = AutorPaper.objects.get(a_id=a_id)
    label = []
    dato = []

    querys = AutorPaper.objects.all()[:15]
    for autor in querys:
        label.append(autor.titulo_paper)
        dato.append(autor.citado_por)

    return render(request, 'paper-profile.html', {'perfils2': perfils2, 'label': label,
        'dato': dato,})