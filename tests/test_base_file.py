from __future__ import unicode_literals

import datetime

from os.path import dirname, abspath, join

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.db import connection


class SquealyTestCases(TestCase):

    def create_mock_user(self):
        user = User.objects.create(username="foo")
        user.set_password('baz')
        user.save()

    def create_mock_client(self):
        self.client = Client()
        self.client.login(username="foo", password="baz")

    def create_schema(self):
        '''
        This method creates an employee table which has four columns:
        name, experience, datae of joining and salary
        After creating the table, we populate it with
        '''
        c = connection.cursor()
        query = 'CREATE TABLE employee_db (name VARCHAR(5), experience INT,\
                 date_of_joining DATE, salary INT)'
        values_list = [
                     ["test1", 2, "2016-01-01", 4],
                     ["test2", 4, "2016-02-01", 3],
                     ["test2", 6, "2016-02-03", 1],
                     ["test3", 4, "2016-01-01", 7],
                     ["test3", 2, "2016-03-04", 2],
                     ["test1", 3, "2016-03-06", 7],
                     ["test5", 6, "2016-03-01", 3],
                     ["test4", 7, "2016-02-01", 5],
                     ["test4", 8, "2016-02-01", 2],
                     ["test5", 9, "2016-01-04", 7]
                    ]
        c.execute(query)
        for value in values_list:
            query1 = 'INSERT INTO employee_db VALUES('+`str(value[0])`+','+`value[1]`+','+`str(value[2])`+','+`value[3]`+')'
            c.execute(query1)

    def delete_schema(self):
        c = connection.cursor()
        query3 = "DROP TABLE employee_db"
        c.execute(query3)