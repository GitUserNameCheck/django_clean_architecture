from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Client

class ClientListView(DynamicTemplate, ListView):
    model = Client
    queryset = Client.objects.order_by('id')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("id", None)

        if search_term is not None:
            qs = qs.filter(id__icontains=search_term)
        return qs

class ClientCreateView(DynamicTemplate, CreateView):

    model = Client

    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy('clients') 

class ClientDeleteView(DynamicTemplate, DeleteView):

    model = Client

    fields = ["id", "name"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('clients')

class ClientUpdateView(DynamicTemplate, UpdateView):

    model = Client

    fields = ["name"]
    template_name_suffix = "_update"
    success_url = reverse_lazy('clients')