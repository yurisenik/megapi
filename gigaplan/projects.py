#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Projects(object):

    def __init__(self, request):
        self.request = request

    def as_list(self, folder='all', status='any', favorites=0, search='',
                detailed=False, filter_id='', parent='', actual=False,
                count=False, sort_by='', sort_order='asc', actions=False,
                limit=50, offset=0, time_updated=''):
        """See https://help.megaplan.ru/API_project_list"""

        uri = '/BumsProjectApiV01/Project/list.api'
        data = {}

        if folder in ['incoming', 'responsible', 'executor', 'owner',
                      'auditor', 'all']:
            data['Folder'] = folder
        else:
            data['Folder'] = 'all'

        if status in ['actual', 'inprocess', 'new', 'overdue', 'done',
                      'delayed', 'completed', 'failed', 'any']:
            data['Status'] = status
        else:
            data['Status'] = 'any'

        if favorites:
            data['FavoritesOnly'] = favorites

        if search:
            data['Search'] = search

        if detailed:
            data['Detailed'] = detailed

        if parent:
            data['SuperProjectId'] = parent

        if actual:
            data['OnlyActual'] = True

        if count:
            data['Count'] = True

        if sort_by in ['id', 'name', 'activity', 'deadline', 'responsible',
                       'owner', 'contractor', 'start', 'plannedFinish',
                       'plannedWork', 'completed', 'bonus', 'fine',
                       'plannedTime']:
            data['SortBy'] = sort_by

        if sort_order in ['asc', 'desc']:
            data['SortOrder'] = sort_order
        else:
            data['SortOrder'] = 'asc'

        data['Limit'] = limit
        data['Offset'] = offset

        if time_updated:
            data['TimeUpdated'] = time_updated

        return self.request(uri, data)

    def get(self, project_id):
        """See https://help.megaplan.ru/API_project_card"""

        uri = '/BumsProjectApiV01/Project/card.api'
        data = {'Id': project_id}

        return self.request(uri, data)

    def create(self, name, responsible_id, deadline='', executors=[],
               auditors=[], parent='', customer='', statement='', start=''):
        """See https://help.megaplan.ru/API_project_create"""
        #TODO: first - no file support

        uri = '/BumsProjectApiV01/Project/create.api'
        data = {'Model[Name]': name, 'Model[Responsible]': responsible_id}

        if deadline:
            data['Model[Deadline]'] = deadline

        if executors:
            data['Model[Executors]'] = executors

        if auditors:
            data['Model[Auditors]'] = auditors

        if parent:
            data['Model[SuperProject]'] = parent

        if customer:
            data['Model[Customer]'] = customer

        if statement:
            data['Model[Statement]'] = statement

        if start:
            data['Model[Start]'] = start

        return self.request(uri, data)

    def edit(self, project_id, name='', deadline='', owner='',
             responsible_id='', executors=[], auditors=[], parent='',
             customer='', statement='', start=''):
        """See https://help.megaplan.ru/API_project_edit"""
        #TODO: first - no file support

        uri = '/BumsProjectApiV01/Project/edit.api'
        data = {'Id': project_id}

        if name:
            data['Model[Name]'] = name

        if deadline:
            data['Model[Deadline]'] = deadline

        if owner:
            data['Model[Owner]'] = owner

        if responsible_id:
            data['Model[Responsible]'] = responsible_id

        if executors:
            data['Model[Executors]'] = executors

        if auditors:
            data['Model[Auditors]'] = auditors

        if customer:
            data['Model[Customer]'] = customer

        if statement:
            data['Model[Statement]'] = statement

        if start:
            data['Model[Start]'] = start

        return self.request(uri, data)

    def get_actions(self, project_id):
        """
        See https://help.megaplan.ru/API_project_action
        See https://help.megaplan.ru/API_project_available_actions
        See https://help.megaplan.ru/API_project_available_actions_for_list
        """

        uri = '/BumsProjectApiV01/Project/availableActions.api'
        uri_list = '/BumsProjectApiV01/Project/availableActionsForList.api'

        if isinstance(project_id, list):
            data = {'Ids': project_id}
            uri_use = uri_list
        else:
            data = {'Id': project_id}
            uri_use = uri

        return self.request(uri_use, data)

    def can_create(self):
        """See https://help.megaplan.ru/API_project_can_create"""

        uri = '/BumsProjectApiV01/Project/canCreate.api'
        data = {}

        if self.request(uri, data)['data']['CanCreate']:
            return True

        return False

    def convert_to_task(self, project_id):
        """See https://help.megaplan.ru/API_project_convert"""

        uri = '/BumsProjectApiV01/Project/convert.api'
        data = {'Id': project_id}

        return self.request(uri, data)

    def change_auditors(self, project_id, auditors=[]):
        """See https://help.megaplan.ru/API_project_save_auditors"""

        if not auditors:
            raise Exception('No auditors provided')

        uri = '/BumsProjectApiV01/Project/saveAuditors.api'
        data = {'Id': project_id,
                'Auditors': auditors}

        return self.request(uri, data)

    def change_executors(self, project_id, executors=[]):
        """See https://help.megaplan.ru/API_project_save_executors"""

        if not executors:
            raise Exception('No executors provided')

        uri = '/BumsProjectApiV01/Project/saveExecutors.api'
        data = {'Id': project_id,
                'Executors': executors}

        return self.request(uri, data)
