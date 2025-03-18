from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import EventServiceEmployee

class EventServiceEmployeeListView(DynamicTemplate, ListView):
    model = EventServiceEmployee
    queryset = EventServiceEmployee.objects.order_by('id')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("id", None)

        if search_term is not None:
            qs = qs.filter(id__icontains=search_term)
        return qs

class EventServiceEmployeeCreateView(DynamicTemplate, CreateView):

    model = EventServiceEmployee

    fields = ["event", "service_employee"]
    template_name_suffix = "_create"
    success_url = reverse_lazy('event_service_employees') 

class EventServiceEmployeeDeleteView(DynamicTemplate, DeleteView):

    model = EventServiceEmployee

    fields = ["id", "event", "service_employee"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('event_service_employees')

class EventServiceEmployeeUpdateView(DynamicTemplate, UpdateView):

    model = EventServiceEmployee

    fields = ["event", "service_employee"]
    template_name_suffix = "_update"
    success_url = reverse_lazy('event_service_employees')