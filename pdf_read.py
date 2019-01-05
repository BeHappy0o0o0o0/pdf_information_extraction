import camelot
import re
import os
import json


def file_name_analysis(file_path):
    """
    解析pdf文件名称，判断获取全部表格/指定页码表格
    :return: pages_list页码组成的列表
    """

    pages_dict = {}
    for file_path, f_name in file_path.items():
        regex = r'\d+'
        if re.findall(regex, f_name):
            pages_dict[file_path] = re.findall(regex, f_name)
        else:
            pages_dict[file_path] = "all"

    return pages_dict


def is_file_or_dir(path):
    """
    判断输入是目录还是文件
    :return:
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


def load_pdf(page_dict):
    """
    读取pdf中的表格
    :param page_dict:
    :return: 输出json
    """

    for f_path, f_page in page_dict.items():
        tables = camelot.read_pdf(f_path, pages=str(34))

        for t in tables:
            # 绘制表格图像
            # plt = camelot.plot(t, kind='grid')
            # plt.show()
            # 转换为json
            temp = json.dumps(t.data)
            # 输出为excel
            # t.to_excel(str(t.page) + "页第" + str(t.order) + "张表" + '.xlsx')
            # 输出为csv
            # t.to_csv(str(t.page) + "页第" + str(t.order) + "张表" + '.json')
            # 输出为html
            # t.to_html(str(t.page) + "页第" + str(t.order) + "张表" + '.json')
            # 输出为json
            # t.to_json(str(t.page) + "页第" + str(t.order) + "张表" + '.json')


if __name__ == "__main__":
    path = input("请输入pdf文件路径或文件所在目录的路径:")
    file_path_dict = is_file_or_dir(path)
    page_dict = file_name_analysis(file_path_dict)
    load_pdf(page_dict)
