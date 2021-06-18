## 背景
阅读次文档前，先阅读run_readme.md，原因：此工具是在run_readme.md中介绍的工具中进行改造，来满足我们将testlink上用例转为metersphere平台可导入的xlsx格式文件。
## 功能说明
1.原始用例层级需按照testlink上手动填入，填入规则详见testlink用例层级.xlsx（忽略此步骤）

2.test_xlsx_metersphere.py顶部相关testlink项目数据需重新配置

3.将testlink上导出的xml格式用例放入TestCase2Testlink目录下

4.转化文件存储在metersphere_testcase和tapd_testcase下

## 操作
一切准备就绪后，执行test_xlsx_metersphere.py即可