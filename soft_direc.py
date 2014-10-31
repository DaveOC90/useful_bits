import os

def soft_direc(ipdirec,opdirec):
	ipdirec=os.path.abspath(ipdirec)
	opdirec=os.path.abspath(opdirec)
	for root,dirs,files in os.walk(ipdirec):
		if files:
		        for f in files:
				if not os.path.exists(root.replace(ipdirec,opdirec)):
					os.makedirs(root.replace(ipdirec,opdirec),0755)
					
				if os.path.isfile(root.replace(ipdirec,opdirec)+'/'+f):
					os.remove(root.replace(ipdirec,opdirec)+'/'+f)

				os.symlink(str(root+'/'+f), str(root.replace(ipdirec,opdirec)+'/'+f))
