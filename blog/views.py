from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    my_posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': my_posts})

def category(request, category_id):
    my_category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category': my_category})
    
    """ # Buscar las publicaciones para pasarlas al template (forma rudimentaria)
    my_posts = Post.objects.filter(categories=my_category)
    return render(request, 'blog/category.html', {'category': my_category, 'posts': my_posts}) """


# TODO: Crear un templeate de error 404