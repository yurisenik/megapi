#! /usr/bin/env python
# -*- coding: utf-8 -*-


import time

import base64
import hashlib
import hmac
import requests


class Request(object):

    url_prefix = 'https://'

    def __init__(self, hostname, login, password, use_sign=True):
        self.hostname = hostname
        self.date = time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime())
        self.use_sign = use_sign
        self.user_id = None
        self.secret_key = None
        self.access_id = None
        self.employee_id = None
        self.auth(login, password)

    def auth(self, login, password):
        """Auth user, store secret_key, user_id and access_id"""

        uri = '/BumsCommonApiV01/User/authorize.api'

        params = {'Login': login,
                  'Password': hashlib.md5(password.encode('utf-8')).hexdigest()}

        r = requests.post(self.url_prefix+self.hostname+uri,
                          params=params)

        if r.json()['status']['code'] != 'ok':
            raise ValueError(r.json()['status']['message'])
        else:
            self.access_id = r.json()['data']['AccessId']
            self.user_id = r.json()['data']['UserId']
            self.employee_id = r.json()['data']['EmployeeId']
            self.secret_key = r.json()['data']['SecretKey']

    def get_sign(self, uri):

        method = 'POST'
        content_type = 'application/x-www-form-urlencoded'
        sign_text = '\n'.join([method,
                               '',
                               content_type,
                               self.date,
                               self.hostname+uri])
        stext = sign_text.encode('utf-8')
        sign = base64.b64encode(hmac.new(self.secret_key.encode('utf-8'),
                                         stext, hashlib.sha1).hexdigest().encode('utf-8')).decode('utf-8')
        return sign

    def __call__(self, uri, data):

        if not self.secret_key and self.access_id:
            raise Exception('Auth first!')

        headers = {'Date': self.date,
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'}
        if self.use_sign:
            headers['X-Authorization'] = '{0}:{1}'.format(self.access_id,
                                                          self.get_sign(uri))

        r = requests.post(self.url_prefix+self.hostname+uri,
                          data=data,
                          headers=headers)
        if r.json()['status']['code'] != 'ok':
            raise ValueError(r.json()['status']['message'])
        else:
            return r.json()

    def __repr__(self):
        return '<Request by {}>'.format(self.user_id)
