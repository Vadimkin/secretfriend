# coding=utf-8
import re
from django.http import JsonResponse
from django.views import generic
from users.models import User
from users.utils import FACULTIES_TYPES, COURSE_TYPES, site_mode


class IndexView(generic.TemplateView):
    if site_mode() == 0:
        template_name = "users/index.html"
    elif site_mode() == 1:
        template_name = "users/game.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['faculties'] = FACULTIES_TYPES
        context['courses'] = COURSE_TYPES

        return context

    def post(self, request):
        result = {}
        for data in request.POST:
            if request.POST[data] == "":
                result['status'] = 0
                result['error_value'] = data
                print(result)
                return JsonResponse(result)

        user = User(name=request.POST['name'], vk_link=request.POST['vk_link'], faculty=request.POST['faculty'],
                    course=request.POST['course'], group_num=request.POST['group_num'],
                    mobile_num="+38" + re.sub("[^0-9]", "", request.POST['mobile_num']))
        user.save()

        result['status'] = 1
        result['data'] = "<h5>Спасибо, заявка успешно отправлена.</h5>" \
                         "<p class='small'>Перед началом игры Вам придёт SMS.</p>"

        return JsonResponse(result)