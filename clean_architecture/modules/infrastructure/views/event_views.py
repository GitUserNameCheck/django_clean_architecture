from django.urls import reverse_lazy
from django.forms import ModelForm, DateTimeInput
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from clean_architecture.dynamic_template import DynamicTemplate
from clean_architecture.modules.infrastructure.db import Event


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

class EventCreateView(DynamicTemplate, CreateView):

    model = Event

    form_class = EventDateTimeForm
    template_name_suffix = "_create"
    success_url = reverse_lazy('events') 

class EventDeleteView(DynamicTemplate, DeleteView):

    model = Event

    fields = ["id", "location", "client", "event_start", "event_end"]
    template_name_suffix = "_delete"
    success_url = reverse_lazy('events')

class EventUpdateView(DynamicTemplate, UpdateView):

    model = Event

    form_class = EventDateTimeForm
    template_name_suffix = "_update"
    success_url = reverse_lazy('events')