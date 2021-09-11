from . import views
from django.urls import path

covid = views.COVIDTrackerModel()
sugar = views.SugarCalculatorModel()
yoga = views.YogaModel()
inner_mind = views.InnerMind()

urlpatterns = [
    path("", views.home, name="index"),
    path("covid/", covid.covid_tracker, name="covid_tracker"),
    path("sugar/", sugar.sugar, name="sugar"),
    path("yoga/", yoga.yoga, name="yoga"),
    path("inner_mind/", inner_mind.inner_mind, name="inner_mind"),
    path("inner_mind/done/", inner_mind.done, name="done"),
    path("inner_mind/stop/", inner_mind.stop, name="done")
]
