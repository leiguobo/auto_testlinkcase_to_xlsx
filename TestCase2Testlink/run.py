#! /usr/bin/python
# coding:utf-8 
""" 
@author:Bingo.he 
@file: run.py 
@time: 2018/12/05
"""
from TestCase2Testlink.common.common1 import TestLinkOperate

if __name__ == "__main__":
    """
    使用方法：查看readme.md
    """
    server = "http://xxxx/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    api_key = "xxxxxx"  # 这个是错误的
    file_name = "testCase_Example.xlsx"  # 用例文件名
    project_id = "xx"
    father_id = "xxx"

    TO = TestLinkOperate(server, api_key)
    '''
    # 上传用例至指定用例集
    TO.upload(project_id, father_id, file_name, sheet_num=0)  # sheet_num 指定上传第几个sheet页的数据
    '''
    # 获取项目project_id
    # print(TO.get_projects_info())

    # 下载指定用例集数据
    TO.download("xxxx")



