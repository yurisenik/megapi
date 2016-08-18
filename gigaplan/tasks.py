# -*- coding: utf-8 -*-


class Tasks(object):
    """Storage for all action on tasks"""

    def __init__(self, request):
        self.request = request

    def as_list(self, folder='all', time_updated='', status='any',
                favorites=False, search='', detailed=False, actual=False,
                filter_id=None, count=False, user_id='', project_id='',
                parent='', sort_by='', sort_order='asc',
                show_actions=False, limit=50, offset=0):
        """See https://help.megaplan.ru/API_task_list"""

        uri = '/BumsTaskApiV01/Task/list.api'
        data = {}

        if folder in ['incoming', 'responsible', 'executor',
                      'owner', 'auditor', 'all']:
            data['Folder'] = folder
        else:
            data['Folder'] = 'all'

        if status in ['actual', 'inprocess', 'new', 'overdue', 'done',
                      'delayed', 'completed', 'failed', 'any']:
            data['Status'] = status
        else:
            data['Status'] = any

        if time_updated:
            data['TimeUpdated'] = time_updated

        if favorites:
            data['FavoritesOnly'] = 1

        if search:
            data['Search'] = search

        if detailed:
            data['Detailed'] = True

        if actual:
            data['OnlyActual'] = True

        if filter_id:
            data['FilterId'] = filter_id

        if count:
            data['Count'] = True

        if user_id:
            data['EmployeeId'] = user_id

        if project_id:
            data['ProjectId'] = project_id

        if parent:
            data['SuperTaskId'] = parent

        if sort_by in ['id', 'name', 'activity', 'deadline', 'responsible',
                       'owner', 'contractor', 'start', 'plannedFinish',
                       'plannedWork', 'actualWork', 'completed', 'bonus',
                       'fine', 'plannedTime']:
            data['SortBy'] = sort_by

        if sort_order in ['asc', 'desc']:
            data['SortOrder'] = sort_order
        else:
            data['SortOrder'] = 'asc'

        if show_actions:
            data['ShowActions'] = True

        data['Limit'] = limit
        data['Offset'] = offset

        return self.request(uri, data)

    def get(self, task_id):
        """See https://help.megaplan.ru/API_task_card"""

        uri = '/BumsTaskApiV01/Task/card.api'
        data = {'Id': task_id}

        return self.request(uri, data)

    def create(self, name, responsible=None, executors=[], deadline='',
               auditors=[], parent='', customer='', is_group=False,
               statement=''):
        """See https://help.megaplan.ru/API_task_create"""
        #TODO: first - no file support

        if is_group and not executors:
            raise Exception('No executors provided')

        if not responsible and not executors:
            raise Exception('Need more people')

        uri = '/BumsTaskApiV01/Task/create.api'
        data = {'Model[Name]': name}

        if responsible:
            data['Model[Responsible]'] = responsible

        if executors:
            data['Model[Executors]'] = executors

        if deadline:
            data['Model[Deadline]'] = deadline

        if auditors:
            data['Model[Auditors]'] = auditors

        if parent:
            data['Model[SuperTask]'] = parent

        if customer:
            data['Model[Customer]'] = customer

        if is_group:
            data['Model[IsGroup]'] = 1

        if statement:
            data['Model[Statement]'] = statement

        return self.request(uri, data)

    def edit(self, task_id, name='', deadline='', owner='', responsible='',
             executors=[], auditors=[], parent='', customer='', statement=''):
        """See https://help.megaplan.ru/API_task_edit"""
        #TODO: first - no file support

        uri = '/BumsTaskApiV01/Task/edit.api'
        data = {'Id': task_id}

        if name:
            data['Model[Name]'] = name

        if deadline:
            data['Model[Deadline]'] = deadline

        if owner:
            data['Model[Owner]'] = owner

        if responsible:
            data['Model[Responsible]'] = responsible

        if executors:
            data['Model[Executors]'] = executors

        if auditors:
            data['Model[Auditors]'] = auditors

        if parent:
            data['Model[SuperTask]'] = parent

        if customer:
            data['Model[Customer]'] = customer

        if statement:
            data['Model[Statement]'] = statement

        return self.request(uri, data)

    def apply_action(self, task_id, action):
        """See https://help.megaplan.ru/API_task_action"""

        uri = '/BumsTaskApiV01/Task/action.api'

        if action not in ['act_accept_task', 'act_reject_task',\
                         'act_accept_work', 'act_reject_work',\
                         'act_done', 'act_pause', 'act_resume',\
                         'act_cancel', 'act_expire', 'act_renew', 'act_delete']:
            raise ValueError('Provide correct action')

        data = {'Id': task_id, 'Action': action}
        return self.request(uri, data)


    def get_actions(self, task_id):
        """
        See https://help.megaplan.ru/API_task_available_actions
        See https://help.megaplan.ru/API_task_available_actions_for_list
        """

        uri = '/BumsTaskApiV01/Task/availableActions.api'
        uri_list = '/BumsTaskApiV01/Task/availableActionsForList.api'

        if isinstance(task_id, list):
            data = {'Ids': task_id}
            uri_use = uri_list
        else:
            data = {'Id': task_id}
            uri_use = uri

        return self.request(uri_use, data)

    def change_deadline(self, subject_id, subject_type, deadline, text):
        """See https://help.megaplan.ru/API_task_change_deadline"""

        if not subject_type in ['task', 'project']:
            raise Exception('Type must be task or project')

        uri = '/BumsTaskApiV01/Task/deadlineChange.api'
        data = {'SubjectId': subject_id,
                'SubjectType': subject_type}

        if deadline:
            data['Deadline'] = deadline
        if text:
            data['Request'] = text

        return self.request(uri, data)

    def accept_deadline(self, query_id, accept=True):
        """See https://help.megaplan.ru/API_task_deadline_action"""

        uri = '/BumsTaskApiV01/Task/deadlineAction.api'

        if accept:
            action = 'act_accept_deadline'
        else:
            action = 'act_reject_deadline'

        data = {'Id': query_id,
                'Action': action}

        return self.request(uri, data)

    def change_executors(self, task_id, executors=[]):
        """See https://help.megaplan.ru/API_task_save_executors"""

        if not executors:
            raise Exception('No executors provided')

        uri = '/BumsTaskApiV01/Task/saveExecutors.api'
        data = {'Id': task_id,
                'Executors': executors}

        return self.request(uri, data)

    def change_auditors(self, task_id, auditors=[]):
        """See https://help.megaplan.ru/API_task_save_auditors"""

        if not auditors:
            raise Exception('No auditors provided')

        uri = '/BumsTaskApiV01/Task/saveAuditors.api'
        data = {'Id': task_id,
                'Auditors': auditors}

        return self.request(uri, data)

    def delegate(self, task_id, user_id):
        """See https://help.megaplan.ru/API_task_delegate"""

        uri = '/BumsTaskApiV01/Task/delegate.api'
        data = {'Id': task_id,
                'ResponsibleId': user_id}

        return self.request(uri, data)

    def can_delegate(self, task_id, responsible_id):
        """See https://help.megaplan.ru/API_task_check_delegate"""

        uri = '/BumsTaskApiV01/Task/checkDelegate.api'
        data = {'Id': task_id,
                'ResponsibleId': responsible_id}

        if self.request(uri, data)['data']['CanDelegate']:
            return True

        return False

    def list_to_delegate(self, task_id):
        """See https://help.megaplan.ru/API_task_employees_to_delegate"""

        uri = '/BumsTaskApiV01/Task/employeesToDelegate.api'
        data = {'Id': task_id}

        return self.request(uri, data)

    def whos_your_daddy(self, only_projects=False):
        """
        See https://help.megaplan.ru/API_task_super_tasks
        See https://help.megaplan.ru/API_task_super_projects
        """
        uri = '/BumsTaskApiV01/Task/superTasks.api'
        uri_projects = '/BumsTaskApiV01/Task/superProjects.api'
        data = {}
        uri_use = uri_projects if only_projects else uri

        return self.request(uri_use, data)

    def convert_to_project(self, task_id):
        uri = '/BumsTaskApiV01/Task/convert.api'
        data = {'Id': task_id}

        return self.request(uri, data)
