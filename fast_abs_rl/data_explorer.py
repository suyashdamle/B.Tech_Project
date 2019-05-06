import pickle as pkl
import os
f = pkl.load(open("arts_summs_dict.pkl",'rb'))
for i,val in f.items():
	print("\n\n",i)
	print("ARTICLE: ",val[0])
	print("SUMMARY: ",val[1])
	input()
	os.system('clear')