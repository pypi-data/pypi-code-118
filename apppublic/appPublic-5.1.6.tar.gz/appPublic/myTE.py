import os
import sys
try:
	import ujson as json
except:
	import json
from jinja2 import Environment,FileSystemLoader, BaseLoader
import codecs
from appPublic.argsConvert import ArgsConvert
from appPublic.dictObject import DictObject
def isNone(obj):
	return obj is None


def string_template_render(tmp_string, data):
	rtemplate = Environment(loader=BaseLoader()).from_string(tmp_string)
	return rtemplate.render(**data)

class MyTemplateEngine:
	def __init__(self,pathList,file_coding='utf-8',out_coding='utf-8'):
		self.file_coding = file_coding
		self.out_coding = out_coding
		loader = FileSystemLoader(pathList, encoding=self.file_coding)
		self.env = Environment(loader=loader, enable_async=False)	
		denv={
			'json':json,
			'hasattr':hasattr,
			'int':int,
			'float':float,
			'str':str,
			'type':type,
			'isNone':isNone,
			'len':len,
			'render':self.render,
			'renders':self.renders,
			'ArgsConvert':ArgsConvert,
			'renderJsonFile':self.renderJsonFile,
			'ospath':lambda x:os.path.sep.join(x.split(os.altsep)),
			'basename':lambda x:os.path.basename(x),
			'basenameWithoutExt':lambda x:os.path.splitext(os.path.basename(x))[0],
			'extname':lambda x:os.path.splitext(x)[-1],
		}
		self.env.globals.update(denv)

	def set(self,k,v):
		self.env.globals.update({k:v})
		
	def _render(self,template,data):
		# print('**********template=',template,'**data=',data,'type_data=',type(data),'************')
		uRet = template.render(**data)
		return uRet
		
	def renders(self,tmplstring,data):
		def getGlobal():
			return data
		self.set('global',getGlobal)
		template = self.env.from_string(tmplstring)
		return self._render(template,data)

	def render(self,tmplfile,data):
		def getGlobal():
			return data
		self.set('global',getGlobal)
		template = self.env.get_template(tmplfile)
		return self._render(template,data)

	def renderJsonFile(self,tmplfile,jsonfile):
		with codecs.open(jsonfile,"r",self.file_coding) as f:
			data = json.load(f)
			return self.render(tmplfile,data)
