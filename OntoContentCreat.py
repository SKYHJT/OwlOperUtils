"""
本体库内容的创建
文件、对象、关系、备注
"""
import builtins

from owlready2 import *


class OntoContentCreat:
    # 1 创建本体文件
    @classmethod
    #def creatOwl(cls, fileName, Owner, Des, state):
    def creatOwl(cls, fileName):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology("http://test.org/onto.owl")
        with onto:
            class 超类(Thing): pass
            class 超关系(ObjectProperty): pass
        onto.save(file=filepath)
        print("creat owlfile success")

    # 3.2 创建本体对象
    @classmethod
    def creatOwlClass(cls, fileName, Name, proOwlName):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        print(list(onto.classes()))
        proClass = onto[proOwlName]
        owlClass = builtins.type(Name, (proClass,), {})
        print(owlClass)
        onto.save(filepath)
        print('creat owlclass success')

    # 3 创建本体关系（数据库部分待完善）
    @classmethod
    def creatOwlRelat(cls, fileName, relationName, proRelatName, domainName, rangeName):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        print(list(onto.classes()))
        proRelat = onto[proRelatName]
        domain = onto[domainName]
        range = onto[rangeName]
        owlRelat = builtins.type(relationName, (proRelat,), {'domain': [domain], 'range': [range]})
        onto.save(filepath)
        ####数据库部分
        ####
        print('creat owlrelat success')

    # 4 创建本体Annotations（数据库部分待完善）
    @classmethod
    def creatOwlAnno(cls, fileName, className, property, value):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        print(list(onto.classes()))
        owlClass = onto[className]
        owlClass.comment.append(locstr(property, lang=value))
        onto.save(file=filepath)
        ####数据库部分
        ####

## 测试
if __name__=='__main__':
    #OntoContentCreat.creatOwl('高')
    OntoContentCreat.creatOwlClass('高','检查','超类')
    OntoContentCreat.creatOwlClass('高', '症状', '超类')
    # OntoContentCreat.creatOwlRelat('高血','isMemberOf','超关系','疾病','症状')
    # OntoContentCreat.creatOwlAnno('高血', '疾病', '哈哈哈', '1')