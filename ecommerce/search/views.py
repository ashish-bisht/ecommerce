from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product
# Create your views here.


class SearchProductView(ListView):
    template_name = "search/view.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()