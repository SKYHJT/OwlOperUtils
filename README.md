# 本体操作类 OntoOperUtils
+ 基于https://pythonhosted.org/Owlready2
+ 本体文件存放路径 filepath = "../owl/%s.owl" % (fileName) 根据情况自行安排
## 一、本体文件存储、读取 OntoFileOpera
读取本体文件
- 
	类方法:
		readOwl(cls, fileName)
	参数：
		fileName（文件名）
	返回： 
		onto 本体对象
	实例：
		onto = OntoFileOpera.readOwl('贫血')
	

存储本体文件
-  
	类方法:
		saveOwl(cls, fileName)
	参数：
		fileName（文件名）
	返回： 
		print('save owlfile success')
	实例：
		OntoFileOpera.saveOwl('贫血')


	
## 二、本体内容创建 OntoContentCreat
本体文件创建:
-  
	类方法:
		creatOwl(cls, fileName)
	参数：
		fileName（文件名）
	返回： 
		print("creat owlfile success")
	实例：
		OntoFileOpera.creatOwl('贫血')

本体对象创建:
-  
	类方法:
		creatOwlClass(cls, fileName, Name, proOwlName)
	参数：
		fileName（文件名）
		Name (本体对象名)
		ProOwlName (父对象名)
	返回： 
		print('creat owlclass success')
	实例：
		OntoContentCreat.creatOwlClass('高血压','检查','超类')

本体关系创建
-  
	类方法:
		creatOwlRelat(cls, fileName, relationName, proRelatName, domainName, rangeName)
	参数：
		fileName（文件名）
		relationName (本体关系名)
		proRelatName (父关系名)
		domainName （领域对象名）
		rangeName （子集对象名）
		
	返回： 
		print('creat owlrelat success')
	实例：
		 OntoContentCreat.creatOwlRelat('高血压','isMemberOf','超关系','疾病','症状')
本体备注创建
-  
	类方法:
		creatOwlAnno(cls, fileName, className, property, value)
	参数：
		fileName（文件名）
		className (本体对象名)
		property (备注编号)
		value （备注信息）
		
	返回： 
		print('creat owlanno success')
	实例：
		 OntoContentCreat.creatOwlAnno('高血压', '疾病', '哈哈哈', '1')
## 三、本体内容查询 OntoContentSearch

查询本体库内所有对象
-  
	类方法:
		searchOwlClass(cls, fileName)
	参数：
		fileName（文件名）
		
	返回： 
		本体库内所有对象信息、无层级关系
		['道法术', '认知', '认知1', '认知2', '能力', '能力1', '能力2', '不足', '不足1', '不足2']
	实例：
		 OntoContentSearch.searchOwlClass('高血压')

查询获取本体库对象的层级关系
-  
	类方法:
		searchOwlClassLayer(cls, fileName)
	参数：
		fileName（文件名）
	返回： 
		表现本体库内层级关系
		以字典形式表现
		[{'name': '道法术', 'content': ['认知']}, {'name': '认知', 'content': ['能力']}, {'name': '能力', 'content': ['不足']}, {'name': '不足', 'content': []}]
	实例：
		 OntoContentSearch.searchOwlClassLayer('高血压')
按照关键字进行查询
-  
	类方法:
		getClassInfo(cls, fileName, ClassName)
	参数：
		fileName（文件名）
		className (本体对象名)
	返回： 
		查询到的本体对象信息
		以字典形式表现
	实例：
		 OntoContentSearch.getClassInfo('高血压'，'检查')
查询本体库内所有关系
-  
	类方法:
		searchOwlRelat(fileName)
	参数：
		fileName（文件名）
	返回： 
		查询到的本体关系信息
		以字典形式表现
	实例：
		 OntoContentSearch.searchOwlRelat('高血压')
查询本体对象备注信息
-  
	类方法:
		searchOwlAnno(cls, fileName, className)
	参数：
		fileName（文件名）
		className (本体对象名)
	返回： 
		查询到的本体备注信息
		以字典形式表现
	实例：
		 OntoContentSearch.searchOwlAnno('高血压'，'疾病')
## 四、本体内容删除 OntoContentDelete
查询本体对象备注信息
-  
	类方法:
		delOwlClass(cls, fileName, className)
	参数：
		fileName（文件名）
		className (本体对象名)
	返回： 
		print('delete owlclass success')
	实例：
		 OntoContentDelete.delOwlClass('高血压'，'疾病')
未完待续
-
