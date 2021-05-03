"""
forms -- профиль клиента

created by pavelmstu in 5/3/21
Проект portal
"""

import datetime

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__status__ = 'Development'
__version__ = '20210503'

from core import app


@app.route('/profile/<user>', methods=['GET'])
def profile(user: str):
    """
    Страница с профилем клиента
    :return:
    :param user: GitHub пользователь
    """
    raise NotImplementedError()


@app.route('/profile/<user>/badges', methods=['GET'])
def badges(user: str):
    """
    Страница со значками пользователя
    :return:
    """
    raise NotImplementedError()


@app.route('/profile/search', methods=['GET'])
def profile_search():
    """
    Страница поиска различных пользователей
    :return:
    """
    raise NotImplementedError()


@app.route('/recipe', methods=['GET'])
def main_recipe():
    """
    Заглавная страница со всеми рецептами
    :return:
    """
    raise NotImplementedError()


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipe(recipe_id: int):
    """
    Страница с каким-либо рецептом
    :param id: идентификатор рецепта
    :return:
    """
    raise NotImplementedError()


@app.route('/recipe/<recipe_id>/edit', methods=['GET'])
def edit_recipe(recipe_id: int):
    """
    Страница с каким-либо рецептом (возможность редактирования)
    :param id: идентификатор рецепта
    :return:
    """
    raise NotImplementedError()


@app.route('/note/<note_id>', methods=['GET'])
def note(note_id: int):
    """
    Страница с заметкой
    :param id: идентификатор заметки
    :return:
    """
    raise NotImplementedError()


@app.route('/note/<note_id>/edit', methods=['GET'])
def edit_note(note_id: int):
    """
    Страница с заметкой (возможность редактирования)
    :param id: идентификатор заметки
    :return:
    """
    raise NotImplementedError()


@app.route('/skill/<skill_id>', methods=['GET'])
def _skill(skill_id: int):
    """
    Служебная страница (доступна корректорам и админам) по просмотру навыков.
    (обычным пользователем смотреть на навыки вне рамках рецепта нет необходимости)
    :param id: идентификатор навыка
    :return:
    """

    raise NotImplementedError()


@app.route('/calendar', methods=['GET'])
def calendar():
    """
    Страница с календарём.

    :return:
    """
    # TODO редирект на Google календарь
    raise NotImplementedError()


@app.route('/map', methods=['GET'])
def map_page():
    """
    Страница-карта со спецкурсами.
    :return:
    """
    raise NotImplementedError()


@app.route('/profile/<user>/diary', methods=['GET'])
def diary(user):
    """
    Дневник пользователя

    :return:
    """
    # TODO дневник только свой. Если чужой -- 403
    raise NotImplementedError()