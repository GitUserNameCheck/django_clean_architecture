from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Client
from clean_architecture.modules.infrastructure.db_repo.client_db_repository import ClientDbRepository
from clean_architecture.modules.interface.client_repository import ClientRepository
from clean_architecture.modules.interface.client_controller import ClientController
from clean_architecture.modules.useсases.client_use_cases import ClientUseCases



client_db_repo = ClientDbRepository()
client_repo = ClientRepository(client_db_repo)
client_use_cases = ClientUseCases(client_repo)
client_controller = ClientController(client_use_cases)

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

    def get_context_data(self, **kwargs):

            context = super().get_context_data(**kwargs)

            page = self.request.GET.get('page', 1)
            queryset = self.get_queryset()

            response, status = client_controller.view_clients(page=int(page), per_page=self.paginate_by, queryset=queryset)

            context['page_obj'] = response["clients"]

            return context

class ClientCreateView(DynamicTemplate, CreateView):

    model = Client

    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy('clients') 

    def form_valid(self, form):
        client_data = form.cleaned_data

        client = Client(
            name=client_data['name'],
        )
        
        response, status = client_controller.create_client(client)

        return HttpResponseRedirect(self.success_url)

class ClientDeleteView(DynamicTemplate, DeleteView):

    model = Client

    fields = ["id", "name"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('clients')

    def get_object(self, queryset=None):
        client_id = self.kwargs.get('pk')
        client = Client.objects.filter(id=client_id).first()
        if not client:
            raise Http404("Client not found")
        return client

    def delete(self, request, *args, **kwargs):

        client = self.get_object()
        response, status = client_controller.delete_client(client.id)

        return HttpResponseRedirect(self.success_url)


class ClientUpdateView(DynamicTemplate, UpdateView):

    model = Client

    fields = ["name"]
    template_name_suffix = "_update"
    success_url = reverse_lazy('clients')

    def get_object(self, queryset=None):
        client_id = self.kwargs.get('pk')
        client = Client.objects.filter(id=client_id).first()
        if not client:
            raise Http404("Client not found")
        return client

    def form_valid(self, form):
        client = form.save(commit=False)  # Don't save the form yet
        response, status = client_controller.update_client(client)  # Save using the repository

        if(status == 400):
            form.add_error(None, response["error"])
            return self.render_to_response(self.get_context_data(form=form))

        return HttpResponseRedirect(self.success_url)