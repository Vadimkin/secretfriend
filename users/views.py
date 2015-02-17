from django import http
from django.views import generic
from users.models import User
from users.utils import FACULTIES_TYPES, COURSE_TYPES


class IndexView(generic.CreateView):
    template_name = "users/index.html"
    model = User
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['faculties'] = FACULTIES_TYPES
        context['courses'] = COURSE_TYPES

        return context

    def post(self, request, **kwargs):
        # request.POST
        return http.HttpResponse("Post")