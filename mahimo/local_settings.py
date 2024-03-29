
# django-allauth Configuration variables you might like to change.

# Specifies the login method to use -- whether the user logs in by entering
# their username, e-mail address, or either one of both. Possible values
# are 'username' | 'email' | 'username_email'
ACCOUNT_AUTHENTICATION_METHOD = "username"

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL

# Determines the expiration date of email confirmation mails (# of days).
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1


ACCOUNT_EMAIL_CONFIRMATION_HMAC = False

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "optional"
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"


# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
ACCOUNT_EMAIL_SUBJECT_PREFIX = ' mahimo.com '
# A string pointing to a custom form class
# (e.g. 'myapp.forms.SignupForm') that is used during signup to ask
# the user for additional input (e.g. newsletter signup, birth
# date). This class should implement a `def signup(self, request, user)`
# method, where user represents the newly signed up user.
ACCOUNT_SIGNUP_FORM_CLASS = None

# When signing up, let the user type in their password twice to avoid typ-o's.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses.
ACCOUNT_UNIQUE_EMAIL = True

# A callable (or string of the form 'some.module.callable_name') that takes
# a user as its only argument and returns the display name of the user. The
# default implementation returns user.username.
# ACCOUNT_USER_DISPLAY

# An integer specifying the minimum allowed length of a username.
ACCOUNT_USERNAME_MIN_LENGTH = 4

# The user is required to enter a username when signing up. Note that the
# user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set
# to email. Set to False when you do not wish to prompt the user to enter a
# username.
ACCOUNT_USERNAME_REQUIRED = True

# render_value parameter as passed to PasswordInput fields.
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# Request e-mail address from 3rd party account provider? E.g. using OpenID
# AX, or the Facebook 'email' permission.
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

# Attempt to bypass the signup form by using fields (e.g. username, email)
# retrieved from the social account provider. If a conflict arises due to a
# duplicate e-mail address the signup form will still kick in.
SOCIALACCOUNT_AUTO_SIGNUP = True

# Enable support for django-avatar. When enabled, the profile image of the
# user is copied locally into django-avatar at signup. Default is
# 'avatar' in settings.INSTALLED_APPS.
# SOCIALACCOUNT_AVATAR_SUPPORT

ACCOUNT_EMAIL_MAX_LENGTH =254
# Maximum length of the email field.
# You won’t need to alter this unless using MySQL with
# the InnoDB storage engine and the utf8mb4 charset,
# and only in versions lower than 5.7.7,
# because the default InnoDB settings don’t allow indexes bigger
# than 767 bytes. When using utf8mb4, characters are 4-bytes wide,
# so at maximum column indexes can be 191 characters long (767/4).
# Unfortunately Django doesn’t allow specifying index lengths,
# so the solution is to reduce the length in characters of indexed
# text fields. More information can be found at MySQL’s documentation
# on converting between 3-byte and 4-byte Unicode character sets.

ACCOUNT_LOGOUT_ON_GET = True
# Determines whether or not the user is automatically logged out
# by a GET request. GET is not designed to modify the server state,
# and in this case it can be dangerous.
# See LogoutView in the documentation for details.
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# When signing up, let the user type in their email address twice to avoid typo’s.

REST_USE_JWT = True

REST_SESSION_LOGIN = True
# Dictionary containing provider specific settings.

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}