import pickle as pkl

class dict_handler:

	def __init__(self):
		self.article_summ_dict={}
		self.file_dict=pkl.load(open("file_dict.pkl",'rb'))

	def change_dict(self,i,key):
	    self.article_summ_dict[self.file_dict[i]][1]=key
	
	def change_dict_art(self,i,art):
	    self.article_summ_dict[self.file_dict[i]]=[art,'']

	def dump_dict(self):
	    pkl.dump(self.article_summ_dict,open("article_summ_dict.pkl",'wb'))

