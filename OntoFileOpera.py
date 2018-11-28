"""
本体文件的存储、读取
"""
from owlready2 import *

class OntoFileOpera():
    # 1 读取本体文件、本体标识
    @classmethod
    def readOwl(cls, fileName):
        filePath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filePath).load()
        print('read owlfile success')
        return onto.base_iri

    # 2 存储本体文件
    @classmethod
    def saveOwl(cls, fileName):
        filePath = "../owl/%s.owl" % (fileName)
        onto = get_ontology("http://test.org/onto.owl")
        onto.save(file=filePath)
        print('save owlfile success')

## 测试
if __name__=='__main__':
    iri= OntoFileOpera.readOwl('贫血')
    print(iri)
