# -*- coding: utf-8 -*-


class Payers(object):
    def __init__(self, request):
        self.request = request

    def edit(self, payer_id, contractor_id, payer_type='Legal', address=''):
        """See https://help.megaplan.ru/API_payer_save"""

        url = '/BumsCrmApiV01/Payer/save.api'

        data = {
            'PayerId': payer_id,
            'PayerType': payer_type,
            'ContractorId': contractor_id
        }

        if address:
            data['Model[Address]'] = address

        return self.request(url, data)
