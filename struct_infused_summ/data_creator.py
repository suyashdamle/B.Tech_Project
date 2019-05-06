import os
import pickle as pkl
IN_DIR = './test_data/files/'
OUT_DIR = './test_data/files/'
struct_infused_dict={}
for f_in in os.listdir(IN_DIR):
	if not f_in.endswith('.story'):
		continue
	with open(IN_DIR+f_in,'r') as f:
		art = f.read()
	with open(OUT_DIR+f_in+'.result.summary','r') as f:
		summ = f.read()			
	struct_infused_dict[f_in]=(art,summ)

pkl.dump(struct_infused_dict,open('struct_infused_dict.pkl','wb'))