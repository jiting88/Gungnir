import json
def tosql(name):
	obj=json.load(open(name))
	sqf=open(name+'.sql','w')
	for x in obj:
		sqf.write("insert into books values(NULL,'{}',{});\n".format(x['name'],x['price']))
	sqf.close()
