# -*- coding: utf-8 -*-


class Clients(object):
    #TODO: check if user has rights todo actions
    def __init__(self, request):
        self.request = request

    def add_human(self, last_name, first_name, middle_name='', email='', parent_company=0, phones=(),
                  responsible_ids=()):
        """See https://help.megaplan.ru/API_contractor_save"""

        uri = '/BumsCrmApiV01/Contractor/save.api'
        data = {'Model[TypePerson]': 'human'}
        data['Model[FirstName]'] = first_name
        data['Model[LastName]'] = last_name
        if middle_name:
            data['Model[MiddleName]'] = middle_name
        if email:
            data['Model[Email]'] = email
        if parent_company:
            data['Model[ParentCompany]'] = parent_company

        if responsible_ids:
            data['Model[Responsibles]'] = ','.join([str(responsible_id) for responsible_id in responsible_ids])

        if phones:

            def norm(tel):
                return tel[1:] + '\t' if len(tel) == 12 else '7' + tel[1:] + '\t'

            def form(tel):
                return tel[0:1] + '-' + tel[1:4] + '-' + tel[4:]

            def pref(tel):
                return 'ph_m-' + tel if tel[2:3] == '9' else 'ph_w-' + tel

            for index in range(0, len(phones)):
                data['Model[Phones][' + str(index) + ']'] = pref(form(norm(phones[index])))

        return self.request(uri, data)

    def add_company(self, name, email='', responsible_ids=(), phones=(), website=''):
        """See https://help.megaplan.ru/API_contractor_save"""

        uri = '/BumsCrmApiV01/Contractor/save.api'
        data = {'Model[TypePerson]': 'company'}
        data['Model[CompanyName]'] = name

        if email:
            data['Model[Email]'] = email

        if responsible_ids:
            data['Model[Responsibles]'] = ','.join([str(responsible_id) for responsible_id in responsible_ids])

        if phones:

            def norm(tel):
                return tel[1:] + '\t' if len(tel) == 12 else '7' + tel[1:] + '\t'

            def form(tel):
                return tel[0:1] + '-' + tel[1:4] + '-' + tel[4:]

            def pref(tel):
                return 'ph_m-' + tel if tel[2:3] == '9' else 'ph_w-' + tel

            for index in range(0, len(phones)):
                data['Model[Phones][' + str(index) + ']'] = pref(form(norm(phones[index])))

        if website:
            data['Model[Site]'] = website

        return self.request(uri, data)

    def edit_human(self, client_id,first_name='', last_name='',
                   middle_name='', email='', parent_company=0, phones=(), responsible_ids=()):
        """See https://help.megaplan.ru/API_contractor_save"""

        uri = '/BumsCrmApiV01/Contractor/save.api'
        data = {'Id': client_id, 'Model[TypePerson]': 'human'}

        if first_name:
            data['Model[FirstName]'] = first_name

        if last_name:
            data['Model[LastName]'] = last_name

        if middle_name:
            data['Model[MiddleName]'] = middle_name

        if email:
            data['Model[Email]'] = email

        if parent_company:
            data['Model[ParentCompany]'] = parent_company

        if responsible_ids:
            data['Model[Responsibles]'] = ','.join([str(responsible_id) for responsible_id in responsible_ids])

        if phones:

            def norm(tel):
                return tel[1:] + '\t' if len(tel) == 12 else '7' + tel[1:] + '\t'

            def form(tel):
                return tel[0:1] + '-' + tel[1:4] + '-' + tel[4:]

            def pref(tel):
                return 'ph_m-' + tel if tel[2:3] == '9' else 'ph_w-' + tel

            for index in range(0, len(phones)):
                data['Model[Phones][' + str(index) + ']'] = pref(form(norm(phones[index])))

        return self.request(uri, data)

    def edit_company(self, client_id, name='', email=''):
        """See https://help.megaplan.ru/API_contractor_save"""

        uri = '/BumsCrmApiV01/Contractor/save.api'
        data = {'Id': client_id, 'Model[TypePerson]': 'company'}

        if name:
            data['Model[CompanyName]'] = name

        if email:
            data['Model[Email]'] = email

        return self.request(uri, data)

    def get(self, client_id, fields=''):
        """See https://help.megaplan.ru/API_contractor_card"""

        uri = '/BumsCrmApiV01/Contractor/card.api'
        data = {'Id': client_id}

        if fields:
            data['RequestedFields'] = fields

        return self.request(uri, data)

    def delete(self, client_id):
        """See https://help.megaplan.ru/API_contractor_delete"""

        uri = '/BumsCrmApiV01/Contractor/delete.api'
        data = {'Id': client_id}

        return self.request(uri, data)

    def as_list(self, filter_id='', limit=50, offset=0, search='',
                phone='', filters=''):
        """See https://help.megaplan.ru/API_contractor_list"""

        uri = '/BumsCrmApiV01/Contractor/list.api'
        data = {'Limit': limit, 'Offset': offset}

        if filter_id:
            data['FilterId'] = filter_id

        if search:
            data['qs'] = search

        if phone:
            data['Phone'] = phone

        if filters:
            data['Model'] = filters

        return self.request(uri, data)

    def get_fields(self):
        """See https://help.megaplan.ru/API_Contractor_fields"""

        uri = '/BumsCrmApiV01/Contractor/listFields.api'
        data = {}

        return self.request(uri, data)

    def block(self, user_id, user_type):
        """See https://help.megaplan.ru/API_block_user"""

        if user_type not in ['user', 'client']:
            raise Exception('Error in user_type')

        uri = '/BumsCommonApiV01/UserAccount/block.api'

        if user_type == 'user':
            data = {'EmployeeId': user_id}
        else:
            data = {'ContractorId': user_id}

        return self.request(uri, data)
