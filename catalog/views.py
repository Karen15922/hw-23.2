from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from catalog.models import Product, Release
from pytils.translit import slugify
from catalog.forms import ProductForm, ReleaseForm, ModeratorProductForm, ModeratorReleaseForm
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ImproperlyConfigured
from catalog.services import get_products_from_cache


# контроллер для страницы создания нового продукта
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ReleaseFormset = inlineformset_factory(Product, Release, ReleaseForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ReleaseFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ReleaseFormset(instance=self.object)
        return context_data 


    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            product = form.save()
            product.owner = self.request.user
            product.save()
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
    
   # контроллер для страницы редактирования продукта
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return(reverse('catalog:product_detail', args=[self.kwargs.get('pk')]))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ReleaseFormset = inlineformset_factory(Product, Release, ReleaseForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ReleaseFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ReleaseFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
        
    def get_form_class(self):
        user = self.request.user
        if self.request.user.is_superuser:
            return ProductForm
        if user.has_perms(['catalog.can_edit_product_description', 'catalog.can_edit_category', 'catalog.can_edit_is_active']):
            return ModeratorProductForm
        elif self.object.owner == user:
            return ProductForm
        raise PermissionDenied
        

# контроллер для страницы отображения списка продуктов
class ProductListView(ListView):
    model = Product
    
    def get_queryset(self):
        return get_products_from_cache()

# контроллер для страницы детального отображения продукта
class ProductDetailView(DetailView):
    model = Product

# контроллер для страницы подтверждения удаления продукта
class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

# контроллер для страницы контактов
class ContactsPageView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) "{message}"')
        return render(request, 'catalog/contacts.html')

