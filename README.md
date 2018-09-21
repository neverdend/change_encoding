# change_encoding

## 功能
遍历「指定目录」下的所有文件，如果文件的后缀名是「指定后缀名」、并且文件的编码是「指定原始编码」，则将文件的编码修改为「指定目标编码」。

## 准备工作
```shell
brew install python
pip2 install chardet
```

## 使用方式
1. git clone。
2. 移动到项目目录。
3. 修改 change_encoding.py 中的变量值。
   1. ROOT_PATH：「指定目录」。
   2. SUFFIX_LIST：「指定后缀名」列表。
   3. SOURCE_ENCODING_LIST：「指定原始编码」列表。
   4. TARGET_ENCODING：「指定目标编码」。
4. python2 change_encoding.py

