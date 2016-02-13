# coding=utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
import re
from django.http import JsonResponse
from django.views import generic
from users.models import User
from users.utils import FACULTIES_TYPES, COURSE_TYPES, site_mode, UNIVERSITY_TYPES


class IndexRedirectView(generic.RedirectView):
    mode = site_mode()

    print(mode)

    if mode == 0:
        url = "/register/"
    else:
        url = "/profile/"


class RegisterTemplateView(generic.TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super(RegisterTemplateView, self).get_context_data(**kwargs)

        context['faculties'] = FACULTIES_TYPES
        context['courses'] = COURSE_TYPES
        context['universities'] = UNIVERSITY_TYPES

        return context

    def post(self, request):
        result = {}

        # if len(User.objects.filter(ip=request.META.get('REMOTE_ADDR'))) > 0:
        #     result['status'] = 1
        #     result['data'] = "<h5>Ошибка</h5>" \
        #                      "<p class='small'>На один компьютер не более одной регистрации</p>"

        if request.POST['name']:
            for data in request.POST:
                if request.POST[data] == "":
                    result['status'] = 0
                    result['error_value'] = data
                    print(result)
                    return JsonResponse(result)

            user = User(name=request.POST['name'], vk_link=request.POST['vk_link'], faculty=request.POST['faculty'],
                        course=request.POST['course'], group_num=request.POST['group_num'],
                        mobile_num="+38" + re.sub("[^0-9]", "", request.POST['mobile_num']),
                        university=request.POST['university'])
            user.save()

            result['status'] = 1
            result['data'] = "<h5>Спасибо, заявка успешно отправлена.</h5>" \
                             "<p class='small'>Перед началом игры Вам придёт SMS.</p>"

        return JsonResponse(result)


class ProfileTemplateView(generic.TemplateView):
    template_name = "users/game.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileTemplateView, self).get_context_data(**kwargs)

        context['faculties'] = FACULTIES_TYPES
        context['courses'] = COURSE_TYPES

        return context


class ProfileAjaxView(generic.TemplateView):
    mode = site_mode()

    def post(self, request):
        result = {}

        if self.mode == 2:
            try:
                if request.POST['code']:
                    user = User.objects.get(hash_code=request.POST['code'])
                    if user:
                        secret_friend = User.objects.get(friend=user)
                        result['data'] = u"<h3>Твоим ТД был(а) — {0}</h3>" \
                                         u"Факультет {1}<br>" \
                                         u"Курс — {2}<br>" \
                                         u"Номер группы — {3}<br>" \
                                         u"Профиль VK — <a href=\"//vk.com/id{4}\">id{4}</a>".format(
                                secret_friend.name, secret_friend.get_faculty(), secret_friend.course,
                                secret_friend.group_num,
                                secret_friend.vk_link)

                    else:
                        result['status'] = 0
                        result['error_text'] = u"Неправильно введён код"

            except ObjectDoesNotExist:
                result['status'] = 0
                result['error_text'] = u"Неправильно введён код"

        elif self.mode == 1:
            try:
                if request.POST['code']:
                    user = User.objects.get(hash_code=request.POST['code'])
                    if user:
                        secret_friend = User.objects.get(id=user.friend_id)
                        result['data'] = u"<h3>Твой ТД — {0}</h3>" \
                                         u"Факультет {1}<br>" \
                                         u"Курс — {2}<br>" \
                                         u"Номер группы — {3}<br>" \
                                         u"Профиль VK — {4}".format(
                                secret_friend.name, secret_friend.get_faculty(), secret_friend.course,
                                secret_friend.group_num,
                                secret_friend.vk_link)

                    else:
                        result['status'] = 0
                        result['error_text'] = u"Неправильно введён код"

            except ObjectDoesNotExist:
                result['status'] = 0
                result['error_text'] = u"Неправильно введён код"

        return JsonResponse(result)
