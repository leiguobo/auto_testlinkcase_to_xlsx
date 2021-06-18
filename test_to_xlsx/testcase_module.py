# coding:utf-8
import pandas as pd

from test_to_xlsx.module_split import module_list_split
from test_to_xlsx.gain_case_path import case_catalogue_path_last

error_list=[]
module_list=[]

#读取第一列、第二列、第四列
df = pd.read_excel(case_catalogue_path_last,sheet_name='Sheet1',usecols=[8])
data = df.values
# print(data)
# print(type(data))
print('download下载真实用例数',len(data))
for i in range(len(data)):
    try:
        clean_line = str(data[i])
        replace_character1 = clean_line.replace('nan', "")
        replace_character2=replace_character1.replace("' '","")
        replace_character3=replace_character2.replace(" ","")
        replace_character4=replace_character3.replace('[','').replace(']','').replace("'","")
        error_list.append(replace_character4)
    except Exception as e:
            if 'list index out of range' in str(e):
                print('数据读取错误，请检查！')
            else:
                print(str(e))

for m in range(len(error_list)):
    for j in module_list_split:
        if error_list[m] == j.split('/')[-1]:
            error_list[m]=j
print('最终用例层级数量：',len(error_list))
module_list=error_list
