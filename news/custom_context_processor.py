from .models import New, Category

def news_list(request):
    news_list = New.published.all().order_by('-date')[:5]
    categories = Category.objects.all()

    context = {
        'news_list': news_list,
    }

    return (context)