# -*- coding: utf-8 -*-

import django.dispatch

questionnaire_completed = django.dispatch.Signal(providing_args=["instance", "data"])
