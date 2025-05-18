from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import ProductForm

# Function-based views
def add_product(request):
    """Add a new product using model form"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def update_product(request, pk):
    """Update a product using form"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': form})

# Class-based views
class ProductListView(ListView):
    """List all products using class-based view"""
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        # Only return non-deleted products
        return Product.objects.filter(is_deleted=False)

class ProductDeleteView(DeleteView):
    """Delete a product using class-based view"""
    model = Product
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        # Soft delete instead of hard delete
        self.object = self.get_object()
        self.object.soft_delete()
        return redirect(self.success_url)

def hard_delete_product(request, pk):
    """Permanently delete a product from the database"""
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
