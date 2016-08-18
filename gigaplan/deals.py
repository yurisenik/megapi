# -*- coding: utf-8 -*-


class Deals(object):
    def __init__(self, request):
        self.request = request

    def create(self, program_id, contractor_id, status_id='', manager_id=0, contact_id=0, auditor_ids=(),
               description=''):
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

        return self.request(uri, data)
