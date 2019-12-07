import pandas as pd
def get_data():
    data_list = pd.read_excel(r"since.xls", encoding='utf-8',sheet_name=0)
    # headers = data_list.header.value.tolist()
    headers = data_list.columns.values.tolist()
    codes = data_list.values.tolist()
    results = []
    for header,code in zip(headers,codes):
        print(header, code[0])
        result = "AU={} AND FU={}".format(header,int(code[0]))
        results.append(result)
    # results.append('AU=王长峰')
    return results
 
# results = get_data()
# print(results)
#📚Believe it or not, knowledge costs money, but I can't afford bread.
# 这ways.py中的data_list.leader.values.tolist()的leader和data_list.code.tolist()的code分别指的是作者名字和基金。可是pandas的read_excel()没有leader和code属性(是因为版本不同?)，我改进了一下代码[我让 科学基金.xls中的内容第一行为作者姓名(下标从0开始)，第一列为基金(下标从1开始)]，博主辛苦，开源快乐😀
# [code=python]
# def get_data():
#     data_list = pd.read_excel(r"since.xls", encoding='utf-8',sheet_name=0)
#     # headers = data_list.header.value.tolist()
#     headers = data_list.columns.values.tolist()
#     codes = data_list.values.tolist()
#     results = []
#     for header,code in zip(headers,codes):
#         print(header, code[0])
#         result = "AU={} AND FU={}".format(header,int(code[0]))
#         results.append(result)
#
# [/code]