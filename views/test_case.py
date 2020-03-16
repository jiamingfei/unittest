#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner_cn

import time
from views.my_case import getTableHeader,getItem,divide,login,getTemplateList
class CaseTest(unittest.TestCase):
    '''乐课网测试'''
    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')

    def setUp(self):
        print('this is setUp')

    def test_getTableHeader(self):
        print('getTableHeader',getTableHeader('request')[1])
        self.assertEqual("操作成功",getTableHeader('request')[0])

    def test_getItem(self):
        print('getItem',getItem('request')[1])
        self.assertEqual("操作成功",getItem('request')[0])

    def test_divide(self):
        print('divide')
        self.assertEqual(3,divide(6,2))
        self.assertNotEqual(3,divide(6,3))

    def test_login(self):
        '''登录接口测试'''
        print('login')
        self.assertEqual(200,login('request'))

    def test_getTemplateList(self):
        '''获取分组信息'''
        print('getTemplateList',getTemplateList('request')[1])
        self.assertEqual('操作成功',getTemplateList('request')[0])

    def tearDown(self):
        print('this is tearDown')

    @classmethod
    def tearDownClass(cls):
        print('this is tearDownClass')

if __name__ == '__main__':
    print('开始执行测试用例')
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    suite = unittest.TestSuite()
    # suite.addTest(CaseTest('test_divide'))
    # suite.addTest(CaseTest('test_add'))
    # suite.addTest(CaseTest('test_is_prime'))
    # suite.addTest(CaseTest('test_login'))
    # suite.addTest(CaseTest('test_getGroupDatas'))
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(CaseTest))
    html_file = 'F:\\Unittest\\report\\'+now+"Result.html"
    fp = open(html_file,'wb+')
    runner = HTMLTestRunner_cn.HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'用例执行情况:')
    runner.run(suite)
    print("生成测试报告")
    fp.close()