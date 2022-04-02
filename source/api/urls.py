from django.urls import path

app_name = 'api'

urlpatterns = [
    path("add/", add, name="add_view"),

]
