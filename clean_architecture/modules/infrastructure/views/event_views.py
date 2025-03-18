from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import ModelForm, DateTimeInput
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Event
from clean_architecture.modules.infrastructure.db_repo.event_db_repository import EventDbRepository
from clean_architecture.modules.useсases.event_use_cases import EventUseCases
from clean_architecture.modules.interface.event_repository import EventRepository
from clean_architecture.modules.interface.event_controller import EventController

event_db_repo = EventDbRepository()
event_repo = EventRepository(event_db_repo)
event_use_cases = EventUseCases(event_repo)
event_controller = EventController(event_use_cases)


class EventDateTimeForm(ModelForm):
    class Meta:
        model = Event
        fields = ["location", "client", "event_start", "event_end"]
        widgets = {
            'event_start': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'event_end': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
        }

class EventListView(DynamicTemplate, ListView):
    model = Event
    queryset = Event.objects.order_by('id')
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

        response, status = event_controller.view_events(page=int(page), per_page=self.paginate_by, queryset=queryset)

        context['page_obj'] = response["events"]

        return context
    

class EventCreateView(DynamicTemplate, CreateView):

    model = Event

    form_class = EventDateTimeForm
    template_name_suffix = "_create"
    success_url = reverse_lazy('events') 

    def form_valid(self, form):
        event_data = form.cleaned_data

        event = Event(
            location=event_data['location'],
            client=event_data['client'],
            event_start=event_data['event_start'],
            event_end=event_data['event_end']
        )
        
        response, status = event_controller.create_event(event)

        if(status == 400):
            form.add_error(None, response["error"])
            form.add_error("event_start", "")
            form.add_error("event_end", "")
            return self.render_to_response(self.get_context_data(form=form))

        return HttpResponseRedirect(self.success_url)


class EventDeleteView(DynamicTemplate, DeleteView):

    model = Event

    fields = ["id", "location", "client", "event_start", "event_end"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('events')

    def get_object(self, queryset=None):
        event_id = self.kwargs.get('pk')
        event = Event.objects.filter(id=event_id).first()
        if not event:
            raise Http404("Event not found")
        return event

    def delete(self, request, *args, **kwargs):

        event = self.get_object()
        response, status = event_controller.delete_event(event.id)

        return HttpResponseRedirect(self.success_url)

class EventUpdateView(DynamicTemplate, UpdateView):

    model = Event

    form_class = EventDateTimeForm
    template_name_suffix = "_update"
    success_url = reverse_lazy('events')

    def get_object(self, queryset=None):
        event_id = self.kwargs.get('pk')
        event = Event.objects.filter(id=event_id).first()
        if not event:
            raise Http404("Event not found")
        return event

    def form_valid(self, form):
        event = form.save(commit=False)  # Don't save the form yet
        response, status = event_controller.update_event(event)  # Save using the repository

        if(status == 400):
            form.add_error(None, response["error"])
            form.add_error("event_start", "")
            form.add_error("event_end", "")
            return self.render_to_response(self.get_context_data(form=form))

        return HttpResponseRedirect(self.success_url)