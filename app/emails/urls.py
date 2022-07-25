from django.urls import path

from . import views

app_name = 'emails'

urlpatterns = [
    path('', views.RecipientList.as_view(), name='all-recipients'),
    path('all-recipients-filter/', views.RecipientsFilterList.as_view(), name='all-recipients-filter'),
    path('send/<int:recipient_id>/', views.send_mail_for_one_recipient, name='send_mail'),

    # CRUD-MODEL-RECIPIENT
    path('add-new-recipient/', views.RecipientCreate.as_view(), name='new-recipient'),
    path('detail-recipient/<int:pk>', views.RecipientDetail.as_view(), name='detail-recipient'),
    path('edit-recipient/<int:pk>/', views.RecipientUpdate.as_view(), name='edit-recipient'),
    path('delete-recipient/<int:pk>/', views.RecipientDelete.as_view(), name='delete-recipient'),
    # END CRUD-MODEL-RECIPIENT

    # CRUD-MODEL-COMPANY
    path('add-new-company/', views.CompanyCreate.as_view(), name='new-company'),
    path('detail-company/<int:pk>/', views.CompanyDetail.as_view(), name='detail-company'),
    path('edit-company/<int:pk>/', views.CompanyUpdate.as_view(), name='edit-company'),
    path('delete-company/<int:pk>/', views.CompanyDelete.as_view(), name='delete-company'),
    # END CRUD-MODEL-COMPANY

    path('add-new-position/', views.PositionCreate.as_view(), name='new-position'),
    path('send-mass-mail/', views.send_mass_malling_for_all_recipient, name='send-mass-mail'),
    path('send-mail-to-company/', views.send_mass_mail_for_selected_company, name='send-mail-to-company'),
]
