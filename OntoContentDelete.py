"""
本体内容删除
对象、关系、备注
"""

from owlready2 import *

class OntoContentDelete:
    @classmethod
    def delOwlClass(cls, fileName, className):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        owlClasses = list(onto.classes())
        for owlClass in owlClasses:
            print(type(owlClass.name),owlClass)
            if owlClass.name == className:
                close_world(owlClass)
        ## 数据库删除未完成
        #delete from table where colname = classname
        ##
        print('delete owlclass success')

## 测试
if __name__=='__main__':
    OntoContentDelete.delOwlClass('高血压','症状')