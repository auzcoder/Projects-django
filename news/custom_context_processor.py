from .models import New

def news_list(request):
    news_list = New.published.all().order_by('-date')[:5]

    context = {
        'news_list': news_list,
    }

    return (context)