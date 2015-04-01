# coding=utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
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
        try:
            if request.POST['name']:
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

        except MultiValueDictKeyError:
            try:
                if request.POST['code']:
                    user = User.objects.get(hash_code=request.POST['code'])
                    if user:
                        secret_friend = User.objects.get(id=user.friend_id)
                        result['data'] = u"Твой ТД — {0}<br>" \
                                         u"Факультет {1}<br>" \
                                         u"Курс — {2}<br>" \
                                         u"Номер группы — {3}<br>" \
                                         u"Профиль VK — {4}".format(
                            secret_friend.name, secret_friend.get_faculty(), secret_friend.course, secret_friend.group_num,
                            secret_friend.vk_link)

                    else:
                        result['status'] = 0
                        result['error_text'] = u"Неправильно введён код"

            except ObjectDoesNotExist:
                result['status'] = 0
                result['error_text'] = u"Неправильно введён код"


        return JsonResponse(result)