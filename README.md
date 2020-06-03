# pdf_information_extraction
提取非扫描版pdf表格信息的py3脚本

### 介绍
脚本使用[camelot](https://github.com/camelot-dev/camelot)完成，目前可以提取简单的表格信息，返回字典，并在脚本目录创建每页对应的json文件。

### 使用方式
脚本支持对单一文件或目录下所有pdf文件表格信息的提取，在运行脚本后根据提示输入pdf文件/目录所在路径。  
如果只需要提取某一页的pdf表格，需要在pdf文件名中增加`_数字`，数字代表需要提取表格的页码，会提取当前页的所有表格。  

下面的例子将提取pdf`12`，`125`页所包含的表格信息。  
  
    pdfname_12_125.pdf

如果需要提取所有表格信息，需要避免文件名包含`_数字`的形式。 

### 计划

1：解决对pdf文本信息的提取  

### 相关资料
[Camelot: PDF Table Extraction for Humans](https://camelot-py.readthedocs.io/en/master/)  
  ~~[python操作pdf]

### 开源许可
遵守[MIT](./LICENSE)开源许可

