# coding:utf-8
import pandas as pd
import os
module_list_split = []  # 所属模块
catalogue_level_path=os.path.abspath(os.path.join('testlink用例层级.xlsx'))
#读取第0,1,2,3,4,5,6列
df = pd.read_excel(catalogue_level_path,sheet_name='Sheet1',usecols=[0,1,2,3,4,5,6])
data = df.values
for i in range(len(data)):
    try:
        clean_line = str(data[i])
        replace_character1 = clean_line.replace('nan', "").replace("code","").replace("{","").replace("}","")
        replace_character2=replace_character1.replace("' '","").replace("quot",'').replace("defaultTAB","")
        replace_character3=replace_character2.replace(" ","").replace("<br />",'').replace("nbsp;",'').replace("data",'')
        replace_character4=replace_character3.replace('[','').replace(']','').replace("'","").replace('\n','')
        module_list_split.append(replace_character4)

    except Exception as e:
            if 'list index out of range' in str(e):
                print('数据读取错误，请检查！')
            else:
                print(str(e))
print('填入用例层级数量：',len(data))

