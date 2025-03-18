from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import ServiceEmployee


class ServiceEmployeeListView(DynamicTemplate, ListView):
    model = ServiceEmployee
    queryset = ServiceEmployee.objects.order_by('id')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("id", None)

        if search_term is not None:
            qs = qs.filter(id__icontains=search_term)
        return qs

class ServiceEmployeeCreateView(DynamicTemplate, CreateView):

    model = ServiceEmployee

    fields = ["employee", "service"]
    template_name_suffix = "_create"
    success_url = reverse_lazy('service_employees') 

class ServiceEmployeeDeleteView(DynamicTemplate, DeleteView):

    model = ServiceEmployee

    fields = ["id", "employee", "service"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('service_employees')

class ServiceEmployeeUpdateView(DynamicTemplate, UpdateView):

    model = ServiceEmployee

    fields = ["employee", "service"]
    template_name_suffix = "_update"
    success_url = reverse_lazy('service_employees')