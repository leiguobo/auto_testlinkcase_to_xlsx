# coding:utf-8
import xlrd,time
import os,json
import testlink
from xlutils import copy
from test_testlinkcase_to_xlsx.TestCase2Testlink.common import logger


def download_testcase():
    """
    获取（下载）testlink上面指定用例集的数据
    :return:
    """
    datas = []
    for data in tlc.getTestCasesForTestSuite(father_id, True, 'full'):
        # print(data)
        actions = []
        expected_results = []
        tsuite_name=data["tsuite_name"]
        name = data["name"]
        summary = data["summary"]
        preconditions = data["preconditions"]
        importance = data["importance"]
        execution_type = data["execution_type"]
        author = data["author_id"]
        print(json.dumps(data, indent=4))
        for i in range(len(data["steps"])):
            actions.append(data["steps"][i]["actions"])
            expected_results.append(data["steps"][i]["expected_results"])
        datas.append((tsuite_name,name, preconditions, '\n'.join(actions), '\n'.join(expected_results), format_execution_type(execution_type), format_auth(author), format_importance(importance), summary))

def format_execution_type(source_data):
    """
    转换执行方式
    :param source_data:
    :return:
    """
    switcher = {
        '2': "自动化",
        '1': "手工"
    }
    return switcher.get(source_data, "Param not defind")

def format_importance(source_data):
    """
    转换优先级
    :param source_data:
    :return:
    """
    switcher = {
        '1': "低",
        '2': "中",
        '3': "高"
    }
    return switcher.get(source_data, "Param not defind")

def format_auth(source_data):
    """
    转换作者：可以通过testlink的user表查询到对应id->name对
    :param source_data:
    :return:
    """
    switcher = {
        '100': "tester_name",
    }
    return switcher.get(source_data, "Param not defind")


def save_suits(file_path, datas):
    """
    保存用例
    :param file_path: 保存路径
    :param datas:
    :return:
    """
    book = xlrd.open_workbook(file_path, formatting_info=True)  # 读取Excel
    new_book = copy.copy(book)  # 复制读取的Excel
    sheet = new_book.get_sheet(0)  # 取第一个sheet页
    line_num = 1
    for i in range(0, len(datas)):
        tsuite_name,name, preconditions, actions, expected_results, execution_type, author, importance, summary = datas[i]
        sheet.write(line_num, 0, u'%s' % name)
        sheet.write(line_num, 1, u'%s' % preconditions)
        sheet.write(line_num, 2, u'%s' % actions)
        sheet.write(line_num, 3, u'%s' % expected_results)
        sheet.write(line_num, 4, u'%s' % execution_type)
        sheet.write(line_num, 5, u'%s' % author)
        sheet.write(line_num, 6, u'%s' % importance)
        sheet.write(line_num, 7, u'%s' % summary)
        sheet.write(line_num, 8, u'%s' % tsuite_name)
        line_num += 1
    report_path = os.path.abspath(os.path.join('download'))
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    suits_name = get_suites(father_id)["name"]
    new_book.save(os.path.abspath(
        os.path.join(report_path, '用例集_{}@{}.xlsx'.format(suits_name, time.strftime('%Y.%m.%d@%H%M%S')))))


def get_suites(suite_id):
    """
    获取用例集信息
    :return:
    """
    try:
        suites = tlc.getTestSuiteByID(suite_id)
        return suites
    except testlink.testlinkerrors.TLResponseError as e:
        # traceback.print_exc()
        logger.warning(str(e).split('\n')[1])
        logger.warning(str(e).split('\n')[0])
        return

if __name__ == "__main__":
    url = "http://10.0.10.64/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
    key = "4f7f501a221dd77a426511c7a80b3ddf"  # 这个key是错误的key
    tlc = testlink.TestlinkAPIClient(url, key)
    father_id = "96015"   # 想要下载的用例集的ID，可通过在testlink界面选取用例集，然后点击右键获取
    download_testcase()