class OtherUtils:
    @classmethod
    def changeToD3(cls,List):
        listDirList = []
        for classDir in reversed(List):
            if len(classDir['content']) != 0:
                for i in range(len(classDir['content'])):
                    for dir in listDirList:
                        if dir['name'] == classDir['content'][i]:
                            classDir['content'][i] = dir
                            listDirList.append(classDir)
            else:
                listDirList.append(classDir)
        print(listDirList[-1])
        return listDirList[-1]
