#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Todos(object):

    def __init__(self, request):
        self.request = request

    def create_todo(self, data):
        """See https://help.megaplan.ru/API_todolist_create"""

        uri = '/BumsTimeApiV01/TodoList/create.api'
        return self.request(uri, data)

    def edit_todo(self, data):
        """See https://help.megaplan.ru/API_todolist_edit"""

        uri = '/BumsTimeApiV01/TodoList/edit.api'
        return self.request(uri, data)

    def delete_todo(self, data):
        """See https://help.megaplan.ru/API_todolist_delete"""

        uri = '/BumsTimeApiV01/TodoList/delete.api'
        return self.request(uri, data)

    def list_todo(self, data):
        """See https://help.megaplan.ru/API_todolist_list"""

        uri = '/BumsTimeApiV01/TodoList/list.api'
        return self.request(uri, data)

    def list_events(self, data):
        """See https://help.megaplan.ru/API_event_list"""

        uri = '/BumsTimeApiV01/Event/list.api'
        return self.request(uri, data)

    def create_event(self, data):
        """See https://help.megaplan.ru/API_event_create"""

        uri = '/BumsTimeApiV01/Event/create.api'
        return self.request(uri, data)

    def show_event(self, data):
        """See https://help.megaplan.ru/API_event_card"""

        uri = '/BumsTimeApiV01/Event/card.api'
        return self.request(uri, data)

    def edit_event(self, data):
        """See https://help.megaplan.ru/API_event_update"""

        uri = '/BumsTimeApiV01/Event/update.api'
        return self.request(uri, data)

    def delete_event(self, data):
        """See https://help.megaplan.ru/API_event_delete"""

        uri = '/BumsTimeApiV01/Event/delete.api'
        return self.request(uri, data)

    def get_places(self):
        """See https://help.megaplan.ru/API_event_places"""

        uri = '/BumsTimeApiV01/Event/places.api'
        data = {}
        return self.request(uri, data)

    def get_event_categories(self):
        """See https://help.megaplan.ru/API_event_categories"""

        uri = '/BumsTimeApiV01/Event/categories.api'
        data = {}
        return self.request(uri, data)

    def finish_event(self, data):
        """See https://help.megaplan.ru/API_event_finish"""

        uri = '/BumsTimeApiV01/Event/finish.api'
        return self.request(uri, data)
