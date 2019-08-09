from datetime import timedelta
from allauth.account.utils import send_email_confirmation, user_email
from allauth.account import app_settings, signals
from allauth.account.models import  EmailConfirmation
from allauth.account.adapter import get_adapter
from allauth.account.app_settings import EmailVerificationMethod
from allauth.account.models import EmailAddress
from django.utils.timezone import now


def send_email_confirmation(request, user, signup=False):
    cooldown_period = timedelta(
        seconds=app_settings.EMAIL_CONFIRMATION_COOLDOWN
    )
    email = user_email(user)
    if email:
        try:
            email_address = EmailAddress.objects.get_for_user(user, email)
            if not email_address.verified:
                if app_settings.EMAIL_CONFIRMATION_HMAC:
                    send_email = True
                else:
                    send_email = not EmailConfirmation.objects.filter(
                        sent__gt=now() - cooldown_period,
                        email_address=email_address).exists()
                if send_email:
                    email_address.send_confirmation(request,
                                                    signup=signup)
            else:
                send_email = False
        except EmailAddress.DoesNotExist:
            send_email = True
            email_address = EmailAddress.objects.add_email(request,
                                                           user,
                                                           email,
                                                           signup=signup,
                                                           confirm=True)
            assert email_address


def send_mail(request, user, email_verification,
                  redirect_url=None, signal_kwargs=None,
                  signup=False):

    adapter = get_adapter(request)
    if not user.is_active:
        return adapter.respond_user_inactive(request, user)

    has_verified_email = EmailAddress.objects.filter(user=user,
                                                     verified=True).exists()
    if email_verification == EmailVerificationMethod.NONE:
        pass
    elif email_verification == EmailVerificationMethod.OPTIONAL:
        # In case of OPTIONAL verification: send on signup.
        if not has_verified_email and signup:
            send_email_confirmation(request, user, signup=signup)
    elif email_verification == EmailVerificationMethod.MANDATORY:
        if not has_verified_email:
            send_email_confirmation(request, user, signup=signup)
            return

def complete_signup(request, user, email_verification, success_url,
                    signal_kwargs=None):
    if signal_kwargs is None:
        signal_kwargs = {}
    signals.user_signed_up.send(sender=user.__class__,
                                request=request,
                                user=user,
                                **signal_kwargs)
    return send_mail(request, user,
                         email_verification=email_verification,
                         signup=True,
                         redirect_url=success_url,
                         signal_kwargs=signal_kwargs)


