"""
本体内容查询
对象、关系、备注
"""

from owlready2 import *

from app.operautils.OtherUtils import OtherUtils


class OntoContentSearch:
    # 1 查询本体库内所有对象
    @classmethod
    def searchOwlClass(cls, fileName):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        owlClass = list(onto.classes())
        owlClassList = []
        for owl in owlClass:
            owlClassList.append(owl.name)
        return owlClassList[1:]

    # 4.2 查询获取本体库对象的层级关系
    ## 例：[{'name':'检查'，'children':['宫高曲线','子宫张力','妊娠期检测','血糖检查']},{}]
    @classmethod
    def searchOwlClassLayer(cls, fileName):
        classesContent = []
        dictLists = []
        contentList = []
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        for owlclass in list(onto.classes()):
            sets = owlclass.descendants()
            sets.remove(owlclass)
            for set in sets:
                # 子对象信息存入classesContent列表中
                classesContent.append(set.name)
            dict_Content = {'name': owlclass.name, 'content': classesContent}
            classesContent = []
            dictLists.append(dict_Content)
        #过滤
        classLayerList = dictLists[1:]
        for classLayer in reversed(classLayerList):
            if len(classLayer['content']) != 0:
                if len(contentList) == 0:
                    # 如果conteneList为空，直接加入
                    for i in range(len(classLayer['content'])):
                        contentList.append(classLayer['content'][i])
                else:
                    # 否则，求conteneList与 classLayer的差集,再加入求conteneList中
                    ret_list = [item for item in classLayer['content'] if item not in contentList]
                    classLayer['content'] = ret_list
                    for i in range(len(ret_list)):
                        contentList.append(ret_list[i])
        return classLayerList


    # 4.3 按照关键字进行查询
    # 输出 例：{'Name': 'FPG', 'Children': []}  （字典）
    @classmethod
    def getClassInfo(cls, fileName, ClassName):
        ContentList = OntoContentSearch.searchOwlClassLayer(fileName)
        for ClassDir in ContentList:
            if ClassDir['name'] == ClassName:
                return ClassDir

    # 4 查询本体库内所有关系
    @classmethod
    def searchOwlRelat(cls, fileName):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        owlRelat = list(onto.properties())
        owlRelatList = []
        for owl in owlRelat:
            owlRelatList.append(owl.name)
        return owlRelatList[1:]

    # 4.5 查询本体对象备注信息
    @classmethod
    def searchOwlAnno(cls, fileName, className):
        filepath = "../owl/%s.owl" % (fileName)
        onto = get_ontology(filepath).load()
        owlClass = onto[className]
        annoList = owlClass.comment
        return annoList

## 测试
if __name__=='__main__':
    # print(OntoContentSearch.searchOwlClass('老板'))
    classLayerList = OntoContentSearch.searchOwlClassLayer('老板')
    OtherUtils.changeToD3(classLayerList)