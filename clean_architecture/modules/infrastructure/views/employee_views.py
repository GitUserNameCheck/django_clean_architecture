from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Employee

class EmployeeListView(DynamicTemplate, ListView):
    model = Employee
    queryset = Employee.objects.order_by('id')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("id", None)

        if search_term is not None:
            qs = qs.filter(id__icontains=search_term)
        return qs

class EmployeeCreateView(DynamicTemplate, CreateView):

    model = Employee

    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy('employees') 

class EmployeeDeleteView(DynamicTemplate, DeleteView):

    model = Employee

    fields = ["id", "name"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('employees')

class EmployeeUpdateView(DynamicTemplate, UpdateView):

    model = Employee

    fields = ["name"]
    template_name_suffix = "_update"
    success_url = reverse_lazy('employees')