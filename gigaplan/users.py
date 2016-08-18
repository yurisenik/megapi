#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Users(object):

    def __init__(self, request):
        self.request = request

    def as_list(self, department=-1, order_by='name', name=''):
        """See https://help.megaplan.ru/API_employee_list"""

        uri = '/BumsStaffApiV01/Employee/list.api'
        data = {'Department': department}
        if order_by in ['name', 'department', 'position']:
            data['OrderBy'] = order_by
        else:
            data['OrderBy'] = 'name'
        if name:
            data['Name'] = name
        return self.request(uri, data)

    def get(self, employee_id):
        """See https://help.megaplan.ru/API_employee_card"""

        uri = '/BumsStaffApiV01/Employee/card.api'
        data = {'Id': employee_id}
        return self.request(uri, data)

    def create(self, data):
        """See https://help.megaplan.ru/API_employee_create"""

        uri = '/BumsStaffApiV01/Employee/create.api'
        return NotImplemented
        # return self.request(uri, data)

    def edit(self, data):
        """See https://help.megaplan.ru/API_employee_edit"""

        uri = '/BumsStaffApiV01/Employee/edit.api'
        # return self.request(uri, data)
        return NotImplemented

    def get_user_actions(self, user_id):
        """See https://help.megaplan.ru/API_employee_available_actions"""

        uri = '/BumsStaffApiV01/Employee/availableActions.api'
        data = {'Id': user_id}

        return self.request(uri, data)

    def block_user(self, user_id=None, employee_id=None, client_id=None,
                   unblock=False):
        """See https://help.megaplan.ru/API_block_user"""

        uri_block = '/BumsCommonApiV01/UserAccount/block.api'
        uri_unblock = '/BumsCommonApiV01/UserAccount/unblock.api'
        data = {}

        if unblock:
            uri_use = uri_unblock
        else:
            uri_use = uri_block

        if not any([user_id, employee_id, client_id]):
            raise Exception('Provide one of ID\'s')

        if user_id:
            data['UserId'] = user_id

        if employee_id:
            data['EmployeeId'] = employee_id

        if client_id:
            data['ContractorId'] = client_id

        return self.request(uri_use, data)

    def list_departments(self):
        """See https://help.megaplan.ru/API_department_list"""

        uri = '/BumsStaffApiV01/Department/list.api'
        data = {}
        return self.request(uri, data)

    def get_phone_types(self):
        """See https://help.megaplan.ru/API_phone_types_list"""

        uri = '/BumsStaffApiV01/Employee/phoneTypes.api'
        data = {}
        return self.request(uri, data)

    def can_create_user(self):
        """See https://help.megaplan.ru/API_employee_can_create"""

        uri = '/BumsStaffApiV01/Employee/canCreate.api'
        data = {}
        return self.request(uri, data)

    def who_online(self):
        """See https://help.megaplan.ru/API_employee_online"""

        uri = '/BumsStaffApiV01/Employee/employeesOnline.api'
        data = {}
        return self.request(uri, data)

    def list_phone_types(self):
        """See https://help.megaplan.ru/API_phone_types_list"""

        uri = '/BumsStaffApiV01/Employee/phoneTypes.api'
        data = {}
        return self.request(uri, data)
