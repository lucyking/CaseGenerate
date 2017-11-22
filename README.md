## args
generateCSV(*filename*, *amount*)  

- **filename**
	- 生成的文件名 需要给出后缀   
- **amount**
	- 生成用例行数   


## run
### 生成随机用例 ###
	$ git clone https://github.com/lucyking/CaseGenerate.git
	$ cd CaseGenerate
	$ python
	>>> import gen
	>>> gen.GenRandomData().generateCSV("test.csv", 100)
	>>>
	
### 条件添加后缀 ###
	>>> import switchAppend
	>>> switchAppend.SW().fx("testdata1000.csv", "result.csv", 13, "2C00010001", 13, "2F00020001")
	                          (输入文件, 输出文件, 1条件所在列, 为1时后缀, 2条件所在列, 为2时后缀)
>row[13]为第14列

 