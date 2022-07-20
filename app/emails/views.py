from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.conf import settings
from .models import Recipient, Company, Position
from .forms import MailForm, RecipientForm, CompanyForm, PositionForm
from .filters import RecipientFilter


# ==================== CRUD-MODEL-RECIPIENT ====================
class RecipientList(ListView):
    """List all Recipients"""
    model = Recipient
    context_object_name = 'recipients'
    template_name = 'emails/recipient_list.html'


class RecipientCreate(CreateView):
    """Create new recipient in DB"""
    form_class = RecipientForm
    model = Recipient
    template_name = 'emails/recipient_create.html'


class RecipientDetail(DetailView):
    """Detail view for selected recipient from DB"""
    model = Recipient
    context_object_name = 'recipient'
    template_name = 'emails/recipient_detail.html'


class RecipientUpdate(UpdateView):
    """Edit selected recipients in DB"""
    model = Recipient
    form_class = RecipientForm
    template_name = 'emails/recipient_edit.html'
    success_url = reverse_lazy('emails:all-recipients')


class RecipientDelete(DeleteView):
    """Deleted selected recipient from DB"""  # ДОБАВИТЬ ВСПЛЫВАЮЩЕЕ ОКНО
    model = Recipient
    template_name = 'emails/recipient_delete.html'
    success_url = reverse_lazy('emails:all-recipients')

# ================== END CRUD-MODEL-RECIPIENT ===================


class CompanyCreate(CreateView):
    """Create new company in DB"""
    form_class = CompanyForm
    model = Company
    template_name = 'emails/company_create.html'


class PositionCreate(CreateView):
    """Create new position in DB"""
    form_class = PositionForm
    model = Position
    template_name = 'emails/position_create.html'


def send_mail_for_one_recipient(request, recipient_id):
    """Send email message for to the selected recipient"""
    if request.method == 'POST':
        form = MailForm(request.POST)
        recipient = Recipient.objects.get(id=recipient_id)

        if form.is_valid():
            message = form.cleaned_data

            send_mail(
                message['subject'],
                message['message'],
                settings.EMAIL_FROM,
                [recipient.email, ]
            )

            return redirect('emails:all-recipients')

    else:
        form = MailForm()
        context = {'form': form}
        return render(request, 'emails/send_mail.html', context)


def send_mass_malling_for_all_recipient(request):
    """Send email message for to the all recipients"""
    if request.method == 'POST':
        form = MailForm(request.POST)
        recipients = Recipient.objects.all()
        emails = []
        for recipient in recipients:
            emails.append(recipient.email)

        if form.is_valid():
            message = form.cleaned_data

            send_mail(
                message['subject'],
                message['message'],
                settings.EMAIL_FROM,
                emails,
            )

            return redirect('emails:all-recipients')

    else:
        form = MailForm()
        context = {'form': form}
        return render(request, 'emails/send_mail.html', context)


def send_mass_mail_for_selected_company(request):
    """Send email message for to the all recipients of the selected company"""
    companies = Company.objects.all()

    if request.method == 'POST':
        form = MailForm(request.POST)
        company_id = request.POST.get('company_id')
        recipients = Recipient.objects.filter(company=company_id)
        emails = []
        for recipient in recipients:
            emails.append(recipient.email)

        if form.is_valid():
            message = form.cleaned_data

            send_mail(
                message['subject'],
                message['message'],
                settings.EMAIL_FROM,
                emails,
            )

            return redirect('emails:all-recipients')

    else:
        mail_form = MailForm()
        context = {
            'mail_form': mail_form,
            'companies': companies,
        }
        return render(request, 'emails/send_mail_to_company.html', context)


class RecipientsFilterList(ListView):
    """List all Recipients with search filter"""
    model = Recipient
    context_object_name = 'recipients'
    template_name = 'emails/recipient_list_filter.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RecipientFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

