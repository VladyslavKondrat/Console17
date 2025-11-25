from django.shortcuts import render
from django.views.generic import TemplateView

#class page(TemplateView):
#    template_name = 'game.html'
def first_view(request):
    return render(request, "game.html")