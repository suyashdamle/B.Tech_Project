import pickle as pkl

file_dict = pkl.load(open("file_dict.pkl",'rb'))
arts_summs_dict = {}
for key,val in file_dict.items():
	data_art = open("all_stories_dataset_laptop/"+file_dict[key],'r').read()
	data_summ = open("fast_abs_rl/suyash_op/output/"+str(key)+'.dec','r').read()
	arts_summs_dict[file_dict[key]]=(data_art,data_summ)
pkl.dump(arts_summs_dict,open("arts_summs_dict.pkl","wb"))