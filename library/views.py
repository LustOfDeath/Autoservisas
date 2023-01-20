from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Paslauga, Automobilis, Uzsakymas


def index(request):
    num_paslaugu = Paslauga.objects.all().count()
    num_uzsakymu_atliktu = Uzsakymas.objects.filter(status__exact="a").count()
    num_automobiliu = Automobilis.objects.all().count()
    context = {'num_paslaugu': num_paslaugu,
               'num_uzsakymu_atliktu': num_uzsakymu_atliktu,
               'num_automobiliu': num_automobiliu}
    return render(request, 'index.html', context=context)


def automobiliai(request):
    # automobiliai = Automobilis.objects.all()
    paginator = Paginator(Automobilis.objects.all(), 1)
    page_number = request.GET.get('page')
    paged_automobiliai = paginator.get_page(page_number)
    context = {
        'automobiliai': paged_automobiliai
    }
    return render(request, 'automobiliai.html', context=context)


def automobilis(request, automobilis_id):
    single_auto = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, 'automobilis.html', {'automobilis': single_auto})


class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = 'uzsakymas_list.html'


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas_detail.html'


def search(request):
    query = request.GET.get("query")
    search_results = Automobilis.objects.filter(Q(klientas__icontains=query) |
                                                Q(valstybinis_nr__icontains=query) |
                                                Q(vin_kodas__icontains=query) |
                                                Q(automobilis_id__modelis__icontains=query))

    return render(request, "search.html", {'automobilis': search_results, "query": query})
