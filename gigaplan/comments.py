# -*- coding: utf-8 -*-


class Comments(object):

    def __init__(self, request):
        self.request = request

    def add(self, subject_type, subject_id, text='', spent=0.0, date=''):
        """See https://help.megaplan.ru/API_comment_create"""
        #TODO: first - no file support

        if subject_type not in ['task', 'project', 'contractor', 'deal']:
            raise Exception('Error in subject_type')

        uri = '/BumsCommonApiV01/Comment/create.api'
        data = {'SubjectType': subject_type, 'SubjectId': subject_id}

        if text:
            data['Model[Text]'] = text

        if spent:
            data['Model[Work]'] = spent

        if date:
            data['Model[WorkDate]'] = date

        return self.request(uri, data)

    def as_list(self, subject_type, subject_id, updated_from='', order='asc',
                as_html=False, unread=False, limit=50, offset=0):
        """See https://help.megaplan.ru/API_comment_list"""

        if subject_type not in ['task', 'project', 'contractor', 'deal']:
            raise Exception('Error in subject_type')

        uri = '/BumsCommonApiV01/Comment/list.api'
        data = {'SubjectType': subject_type, 'SubjectId': subject_id}

        if updated_from:
            data['TimeUpdated'] = updated_from

        if order in ['asc', 'desc']:
            data['Order'] = order
        else:
            data['Order'] = 'asc'

        if as_html:
            data['TextHtml'] = True

        data['Limit'] = limit
        data['Offset'] = offset

        return self.request(uri, data)

    def mark_read(self, comment_id):
        """See https://help.megaplan.ru/API_comment_mark_as_read"""

        uri = '/BumsCommonApiV01/Comment/markAsRead.api'

        if isinstance(comment_id, list):
            data = {'IdList': comment_id}
        else:
            data = {'Id': comment_id}

        return self.request(uri, data)

    def get_actual(self, actual=False):
        """See https://help.megaplan.ru/API_comment_all"""

        uri = '/BumsCommonApiV01/Comment/all.api'
        data = {'OnlyActual': actual}

        return self.request(uri, data)

    def get_by_id(self, comment_id):
        """See https://help.megaplan.ru/API_comment_by_id"""

        uri = '/BumsCommonApiV01/Comment/commentById.api'
        data = {'Id': comment_id}

        return self.request(uri, data)
