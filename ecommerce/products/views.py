from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Product



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html" 

    
    # def get_context_data(self,*args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesnt exist")
        return instance
        print(instance)
