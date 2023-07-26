from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    main_page = "<h1>Мой первый Django сайт</h1><br><br><br><div>Создан в целях изучения Django framework</div>"
    logger.info("Страницу Main посетили")
    return HttpResponse(main_page)


def about(request):
    about_page = "<h1>Обо мне:</h1><br><br><h3>Молоканов Михаил</h3><br><div>Студент онлайн-школы GeekBrains по " \
                 "специальности - программирование</div>"
    logger.info("Страницу About посетили")
    return HttpResponse(about_page)
