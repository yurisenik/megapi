# -*- coding: utf-8 -*-


class Deals(object):
    def __init__(self, request):
        self.request = request

    def create(self, program_id=12, contractor_id, status_id='', manager_id=0, contact_id=0, auditor_ids=(),
               description='', operator_id=0, interest=''):
        """See https://help.megaplan.ru/API_deal_save"""

        uri = '/BumsTradeApiV01/Deal/save.api'
        data = {'ProgramId': program_id, 'Model[Contractor]': contractor_id}

        if status_id:
            data['StatusId'] = status_id

        if manager_id:
            data['Model[Manager]'] = manager_id

        if contact_id:
            data['Model[Contact]'] = contact_id

        if auditor_ids:
            data['Model[Auditors]'] = ','.join([str(auditor_id) for auditor_id in auditor_ids])

        if description:
            data['Model[Description]'] = description

        if operator_id:
            if program_id=='12':
                data['Model[Category1000057CustomField1YaLiniya]'] = operator_id
            if program_id=='14':
                data['Model[Category1000059CustomField1YaLiniya]'] = operator_id

        if interest:
            if program_id=='14':
                data['Model[Category1000059CustomFieldSferaInteresa]'] = interest

        return self.request(uri, data)

    def get_fields(self, program_id):
        """See https://help.megaplan.ru/API_deal_available_fields_list"""

        uri = '/BumsTradeApiV01/Deal/listFields.api'
        data = {'ProgramId': program_id}

        return self.request(uri, data)

    def as_list(self, filter_fields='', requested_fields='', extra_fields='', limit=0, offset=0):
        """See https://help.megaplan.ru/API_deal_list"""

        uri = '/BumsTradeApiV01/Deal/list.api'
        data = {}

        if filter_fields:
            data['FilterFields'] = filter_fields

        if requested_fields:
            data['RequestedFields'] = requested_fields

        if extra_fields:
            data['ExtraFields'] = extra_fields

        if limit:
            data['Limit'] = limit

        if offset:
            data['Offset'] = offset

        return self.request(uri, data)
