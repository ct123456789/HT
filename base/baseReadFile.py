import os
import yaml


class BaseReadFile:

    def __init__(self, filePath):
        self.filePath = filePath

    def readFile(self):
        # 获取当前文件的父目录的父目录
        load = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 将路径拼接好
        file = yaml.load(open(load+self.filePath))
        return file

