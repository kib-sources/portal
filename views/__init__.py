"""
__init__.py

TODO описание модуля

created by pavel in pavel as 5/3/21
Проект portal
"""

import datetime

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__status__ = 'Development'
__version__ = '20210503'

from core import app


@app.route('/note/<note_id>/json', methods=['POST'])
def json_note(note_id: int):
    """
    JSON-cловарь, содержащий заметку
    :param note_id: идентификатор заметки
    :return:
    """

    example = {
        "note_id": 1242135,
        "title": "Заголовок заметки",
        "tags": ["#linux", "#group-ib"],
        "create": "2021-04-03 13:05:23",
        "change": "2021-04-03 13:05:23",
        "author": "pavelmstu",
        "body": """
            Большая markdown страница.
        """,
    }

    raise NotImplementedError()


@app.route('/note/<note_id>/json/head/', methods=['POST'])
def json_note_head(note_id: int):
    """
    JSON-cловарь, содержащий заметку БЕЗ тела.
    :param note_id: идентификатор заметки
    :return:
    """
    raise NotImplementedError()


@app.route('/recipe/<recipe_id>/json', methods=['POST'])
def json_recipe(recipe_id: int):
    """
    Страница с каким-либо рецептом
    :param id: идентификатор рецепта
    :return:
    """

    example = {
        "recipe_id": 345345345,
        "title": "Заголовок рецепта",
        "skills": [235235, 23522, 235235],
        "create": "2021-04-03 13:05:23",
        "change": "2021-04-03 13:05:23",
        "author": "pavelmstu",
    }

    raise NotImplementedError()


@app.route('/recipe/<recipe_id>/json/head', methods=['POST'])
def json_recipe_head(recipe_id: int):
    """
    Страница с каким-либо рецептом
    :param recipe_id: идентификатор рецепта
    :return:
    """
    raise NotImplementedError()


@app.route('/skill/<skill_id>/json', methods=['POST'])
def json_skill(skill_id: int):
    """
    Определённый JSON с навыком
    :param skill_id: идентификатор навыка
    :return:
    """

    example = {
        "skill_id": 23522,
        "title": "Заголовок навыка",
        "create": "2021-04-03 13:05:23",
        "change": "2021-04-03 13:05:23",
        "author": "pavelmstu",
        "body": """
            Markdown описание навыка
        """
    }

    raise NotImplementedError()


@app.route('/profile/<user>/badges/json', methods=['POST'])
def json_badges(user: str):
    """
    Значки пользователя в JSON описании
    :return:
    """

    example = {
        "user": "pavelmstu",
        "badges": [23, 12, 13523, 235235],
    }

    raise NotImplementedError()


@app.route('/badge/<badge_id>/json', methods=['POST'])
def json_badge(badge_id: int):
    """
    JSON информация о значке
    :return:
    """

    example = {
        "badge_id": 23,
        "title": "Python exam pass",
        "description": "Студент сдал хардкорный экзамен по питону",
        "link": "portal.kib.su/.../.../",  # полная ссылка на страницу, при нажатии на значёк"
    }

    raise NotImplementedError()


@app.route('/badge/<badge_id>/image', methods=['GET'])
def image_badge(badge_id: int):
    """
    Изображение значка
    :return:
    """
    raise NotImplementedError()


@app.route('/profile/<user>/image', methods=['GET'])
def image_profile(user: str):
    """
    Аватар профиля
    :return:
    """
    raise NotImplementedError()


@app.route('/profile/<user>/image/set', methods=['POST'])
def set_image_profile(user: str):
    """
    Задать аватар профиля
    :return:
    """
    # TODO обсудить какие поля в теле

    raise NotImplementedError()


# -----------
# Отношения

# (user, skill_id)
@app.route('/profile/status/skill', methods=['POST'])
def status_skill():
    """
    определяет статус данного скилла в рамках указанного пользователя
    :return:
    """
    # TODO договорится как передаются user и skill_id

    raise NotImplementedError()



