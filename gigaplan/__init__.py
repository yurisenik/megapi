#! /usr/bin/env python
# -*- coding: utf-8 -*-


from .clients import Clients
from .comments import Comments
from .deals import Deals
from .payers import Payers
from .projects import Projects
from .request import Request
from .tags import Tags
from .tasks import Tasks
from .users import Users


class Megaplan(object):
    def __init__(self, hostname, login, password):
        self.request = Request(hostname, login, password)
        self.tasks = Tasks(self.request)
        self.projects = Projects(self.request)
        self.comments = Comments(self.request)
        self.tags = Tags(self.request)
        self.clients = Clients(self.request)
        self.users = Users(self.request)
        self.deals = Deals(self.request)
        self.payers = Payers(self.request)
