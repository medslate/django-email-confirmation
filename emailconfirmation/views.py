from django.shortcuts import render_to_response
from django.template import RequestContext

from emailconfirmation.models import EmailConfirmation


def confirm_email(request, confirmation_key):
    
    confirmation_key = confirmation_key.lower()
    
    confirmation = None
    try:
        confirmation = EmailConfirmation.objects.get(
            confirmation_key=confirmation_key)
    except EmailConfirmation.DoesNotExist:
        pass

    if confirmation and confirmation.email_address.user == request.user:
        email_address = EmailConfirmation.objects.confirm_email(confirmation_key)
    else:
        email_address = None

    return render_to_response("emailconfirmation/confirm_email.html", {
        "email_address": email_address,
    }, context_instance=RequestContext(request))
