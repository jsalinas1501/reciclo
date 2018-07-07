from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from rest_framework import viewsets

from .models import TrashCan, Level
from .forms import TrashCanForm
from .serializers import TrashCanSerializer, LevelSerializer


def my_list_view(request):
    template_name = 'trashcan/lista.html'
    context = {
        'cans': TrashCan.objects.get_lat_lng(),
    }
    return render(request, template_name, context)


class CreateView(View):

    template_name = 'trashcan/crear.html'
    form = TrashCanForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home_app:home')
        context = {
            'errors': kwargs.get('errors'),
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            data = dict(request.POST)
            data.pop('csrfmiddlewaretoken')
            data = {k: v[0] for k, v in data.items()}
            TrashCan.objects.create(**data)
            return redirect('trashcan_app:can-list')
        return self.get(request, errors=form.errors)


class DetailView(View):

    template_name = 'trashcan/detalle.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home_app:home')
        pk = kwargs.get('pk')
        context = {
            'errors': kwargs.get('errors'),
            'can': TrashCan.objects.filter(pk=pk).first(),
            'levels': Level.objects.get_levels(pk),
        }
        return render(request, self.template_name, context)


class TrashCanViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer
    filter_fields = (
        'barcode',
    )
    search_fields = (
        'barcode',
    )


class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all()
    serializer_class = LevelSerializer
