import camelot
import re
import os
import json


# 解析pdf文件名称，判断获取全部表格/指定页码表格
def file_name_analysis(file_path):
    """
    :return: pages_list页码组成的列表
    """

    pages_dict = {}
    for f_path, f_name in file_path.items():
        regex = r'_(\d+)+'
        re_result = re.findall(regex, f_name)
        if re_result:
            pages_dict[f_path] = re_result
        else:
            pages_dict[f_path] = "all"

    return pages_dict


# 判断输入是目录还是文件
def is_file_or_dir(path):
    """
    :return: 返回由文件路径与文件名组成的字典
    """
    files_path_dict = {}
    # 判断文件或目录是否存在
    if os.path.exists(path):
        if os.path.isdir(path):
            # root, dirs, files = os.walk(path)
            for files in os.listdir(path):
                if os.path.splitext(files)[1] == '.pdf':
                    files_path_dict[path+files] = files
        else:
            if os.path.splitext(path)[1] == '.pdf':
                files_path_dict[path] = os.path.split(path)[1]

    return files_path_dict


# 读取pdf中的表格
def load_pdf(page_dict):
    """
    :param page_dict:
    :return: 返回一个存储表格数据的字典
    """

    data_dict = {}
    for f_path, f_page in page_dict.items():
        if f_page == "all":
            tables = camelot.read_pdf(f_path, pages="all")
        else:
            for p in f_page:
                tables = camelot.read_pdf(f_path, pages=str(p))

        for t in tables:
            # 绘制表格图像
            # plt = camelot.plot(t, kind='grid')
            # plt.show()

            # 转换为json
            data = json.dumps(t.data)
            str_key = str(t.page) + "页第" + str(t.order) + "张表"
            data_dict[str_key] = data
            # 输出为excel
            # t.to_excel(str(t.page) + "页第" + str(t.order) + "张表" + '.xlsx')
            # 输出为csv
            # t.to_csv(str(t.page) + "页第" + str(t.order) + "张表" + '.cvs')
            # 输出为html
            # t.to_html(str(t.page) + "页第" + str(t.order) + "张表" + '.html')
            # 输出为json
            t.to_json(str(t.page) + "页第" + str(t.order) + "张表" + '.json')

    return data_dict


if __name__ == "__main__":
    path = input("请输入pdf文件/目录所在在路径:")
    file_path_dict = is_file_or_dir(path)
    page_dict = file_name_analysis(file_path_dict)
    pdf_data = load_pdf(page_dict)
