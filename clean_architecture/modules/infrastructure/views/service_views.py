from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Service
from clean_architecture.modules.infrastructure.forms import ServicePriceForm


class ServiceListView(DynamicTemplate, ListView):
    model = Service
    queryset = Service.objects.order_by('id')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("id", None)

        if search_term is not None:
            qs = qs.filter(id__icontains=search_term)
        return qs

class ServiceCreateView(DynamicTemplate, CreateView):

    model = Service

    form_class = ServicePriceForm
    template_name_suffix = "_create"
    success_url = reverse_lazy('services') 

class ServiceDeleteView(DynamicTemplate, DeleteView):

    model = Service

    fields = ["id", "price", "description"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('services')

class ServiceUpdateView(DynamicTemplate, UpdateView):

    model = Service

    form_class = ServicePriceForm
    template_name_suffix = "_update"
    success_url = reverse_lazy('services')