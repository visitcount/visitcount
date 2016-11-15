from django.views.generic import DetailView

from .models import Item


class ItemDetail(DetailView):

    model = Item