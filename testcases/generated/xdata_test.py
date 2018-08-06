# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import unittest
import os
import json


class XdataTest(unittest.TestCase):

    def test_list_database_info(self):
        cmd = """python ../../main.py xdata list-database-info  --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_database_info(self):
        cmd = """python ../../main.py xdata get-database-info  --database-name 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_database(self):
        cmd = """python ../../main.py xdata create-database  --database-name 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_database(self):
        cmd = """python ../../main.py xdata delete-database  --database-name 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_instance_info(self):
        cmd = """python ../../main.py xdata list-instance-info """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_execute_ras_query(self):
        cmd = """python ../../main.py xdata execute-ras-query  --sql 'xxx' --user-name 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_execute_py_spark_query(self):
        cmd = """python ../../main.py xdata execute-py-spark-query  --script 'xxx' --user-name 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_ras_query_state(self):
        cmd = """python ../../main.py xdata get-ras-query-state  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_py_spark_execute_state(self):
        cmd = """python ../../main.py xdata get-py-spark-execute-state  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_ras_query_log(self):
        cmd = """python ../../main.py xdata get-ras-query-log  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_ras_query_result(self):
        cmd = """python ../../main.py xdata get-ras-query-result  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_py_spark_execute_result(self):
        cmd = """python ../../main.py xdata get-py-spark-execute-result  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_cancel_ras_query(self):
        cmd = """python ../../main.py xdata cancel-ras-query  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_cancel_py_spark_job(self):
        cmd = """python ../../main.py xdata cancel-py-spark-job  --user-name 'xxx' --query-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_table_info(self):
        cmd = """python ../../main.py xdata list-table-info  --instance-name 'xxx' --database-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_table(self):
        cmd = """python ../../main.py xdata create-table  --instance-name 'xxx' --db-model-dbtable '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_table_info(self):
        cmd = """python ../../main.py xdata get-table-info  --table-name 'xxx' --instance-name 'xxx' --database-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_table(self):
        cmd = """python ../../main.py xdata delete-table  --table-name 'xxx' --instance-name 'xxx' --database-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

