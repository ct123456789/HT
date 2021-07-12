import os
import yaml


class HandleInit:

    def readFile(self, filePath):
        # 获取当前文件的父目录的父目录
        current_load = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 将路径拼接好
        file = yaml.load(open(current_load+filePath, encoding='UTF-8'))
        return file

