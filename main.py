from django.db.models import Q, F
from django.db.models import Value as V
from django.db.models.functions import Concat 

user_list = models.User.objects.annotate(
                        full_name=Concat('first_name', V(' '), 'last_name')
                    ).filter(   
                        Q(full_name__icontains=keyword) | 
                        Q(first_name__icontains=keyword) | 
                        Q(last_name__icontains=keyword)
                    )



def index(request, slug=None):
    if slug:
        category_obj = Categorie.objects.filter(Q(name__icontains=slug))
        if category_obj:
            print(category_obj[0].id)
    else:
        pass
    
    categories = Categorie.objects.all()
    return render(request, 'index.html', {'categories':categories})


User.objects.filter(first_name__contains='John', last_name__contains='Smith') 






class FilterForm(Form):
    FILTER_CHOICES = (
        ('all', 'All'),
        ('people', 'People'),
        ('certification', 'Certification'),
        ('skillset', 'Skillset'),
    )
    search = CharField(required=False)
    filter_field = ChoiceField(choices=FILTER_CHOICES)
