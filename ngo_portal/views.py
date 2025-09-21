# ngo_portal/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NGOEvent, VolunteerApplication
from .forms import NGOEventForm, VolunteerApplicationForm

# -------------------------------
# Homepage / Dashboard
# -------------------------------
@login_required(login_url='login')
def home(request):
    """Display all events on the homepage."""
    events = NGOEvent.objects.all()
    return render(request, 'ngo_portal/home.html', {'events': events})


# -------------------------------
# Event CRUD Views
# -------------------------------
@login_required
def event_list(request):
    """List all NGO events."""
    events = NGOEvent.objects.all()
    return render(request, 'ngo_portal/event_list.html', {'events': events})


@login_required
def event_create(request):
    """Create a new event."""
    if request.method == 'POST':
        form = NGOEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.ngo = request.user  # Assign the current user as NGO owner
            event.save()
            return redirect('event_list')
    else:
        form = NGOEventForm()
    return render(request, 'ngo_portal/event_form.html', {'form': form})


@login_required
def event_edit(request, id):
    """Edit an existing event (only by the event owner)."""
    event = get_object_or_404(NGOEvent, id=id, ngo=request.user)
    if request.method == 'POST':
        form = NGOEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = NGOEventForm(instance=event)
    return render(request, 'ngo_portal/event_form.html', {'form': form})


@login_required
def event_delete(request, id):
    """Delete an event (only by the event owner)."""
    event = get_object_or_404(NGOEvent, id=id, ngo=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'ngo_portal/event_confirm_delete.html', {'event': event})


# -------------------------------
# Volunteer Application Views
# -------------------------------
@login_required
def apply_event(request, id):
    """Apply to participate in an event."""
    event = get_object_or_404(NGOEvent, id=id)
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.event = event
            application.volunteer = request.user
            application.save()
            return redirect('event_list')
    else:
        form = VolunteerApplicationForm()
    return render(request, 'ngo_portal/apply_event.html', {'form': form, 'event': event})


@login_required
def view_applications(request, id):
    """View all volunteer applications for a specific event (only by the NGO owner)."""
    event = get_object_or_404(NGOEvent, id=id, ngo=request.user)
    applications = VolunteerApplication.objects.filter(event=event)
    return render(request, 'ngo_portal/view_applications.html', {
        'event': event,
        'applications': applications
    })
