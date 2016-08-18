# -*- coding: utf-8 -*-


class Tags(object):

    def __init__(self, request):
        self.request = request

    def assign(self, subject_type, subject_id, tags_id=[]):
        """See https://help.megaplan.ru/API_tags_assign"""

        if not tags_id:
            raise Exception('No tags provided')

        if subject_type not in ['task', 'project']:
            raise Exception('Error in subject_type')

        if not isinstance(tags_id, list):
            raise Exception('Parameter tags_id must be list')

        uri = '/BumsCommonApiV01/Tags/assign.api'
        data = {'SubjectType': subject_type}

        if isinstance(subject_id, list):
            pass
        else:
            subject_id = [subject_id]

        for k, _ in enumerate(subject_id):
            data['SubjectIds[{0}]'.format(k)] = _
            for kk, __ in enumerate(tags_id):
                data['TagIds[{0}]'.format(kk)] = __
                
        return self.request(uri, data)

    def create(self, subject_type, name, is_global=False):
        """See https://help.megaplan.ru/API_tags_create"""

        if subject_type not in ['task', 'project']:
            raise Exception('Error in subject_type')

        uri = '/BumsCommonApiV01/Tags/create.api'
        data = {'SubjectType': subject_type, 'Model[Name]': name,
                'Model[IsGlobal]': is_global}

        return self.request(uri, data)

    def update(self, data):
        """See https://help.megaplan.ru/API_tags_update"""

        uri = '/BumsCommonApiV01/Tags/update.api'
        return self.request(uri, data)

    def as_list(self, subject_type, include_global=False):
        """See https://help.megaplan.ru/API_tags_list"""

        if subject_type not in ['task', 'project', 'event']:
            raise Exception('Error in subject_type')

        uri = '/BumsCommonApiV01/Tags/list.api'
        data = {'SubjectType': subject_type, 'IncludeGlobal': include_global}

        return self.request(uri, data)

    def search(self, tag_id, name):
        """See https://help.megaplan.ru/API_tags_search"""

        uri = '/BumsCommonApiV01/Tags/search.api'
        data = {'Id': tag_id, 'Model[Name]': name}

        return self.request(uri, data)

    def delete(self, tag_id):
        """See https://help.megaplan.ru/API_tags_delete"""

        uri = '/BumsCommonApiV01/Tags/delete.api'
        data = {'Id': tag_id}

        return self.request(uri, data)
