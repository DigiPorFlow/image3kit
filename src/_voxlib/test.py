
import os; ''' ========== set up paths  =========== '''
if not ("msRoot" in os.environ):
  print("try again after running:\nsource .../src/bashrc"); exit(-1);
from msrc  import *


nErrs=0

with open("voxcylinder.mhd", 'w') as f1:
	f1.write("""DimSize = 20 20 20
		Offset =      0    0    0
		replaceRange 0 255 1
		reset  dx 1
		Paint cylinder 0 10 10   20 10 10  5
		reset  dx 1e-6
		""");#ElementDataFile = NO_READ

runSh('.', "voxelImageProcess voxcylinder.mhd voxcylinder.tif");
runSh('.', "voxelImageProcess voxcylinder.tif voxcylinder.mhd");
nErrs += fileFloatDiffersFrom("voxelImageProcess.log","total_porosity:",math.pi*5*5/(20*20),0.05)



with open("voxcylinderNoisy.mhd", 'w') as f1:
	f1.write(""" DimSize = 20 20 20 \n Offset =  0  0  0
		replaceRange 0 255 1
		reset  dx 1 	\n Paint cylinder 10 10 10   10 10 20  5 	\n reset  dx 1e-6
		sliceToPng z Zcylinder 10  0  1
		addSurfNoise 1 1  13   \n addSurfNoise 1 1  3
		operat    * 127 \n # resliceZ  20
		sliceToPng z ZcylRough13x2 0  0  127
		operat    / 64
		""");#ElementDataFile = NO_READ
runSh('.', "voxelImageProcess voxcylinderNoisy.mhd voxcylinderNoisy.tif");
nErrs += fileFloatDiffersFrom("voxelImageProcess.log","total_porosity:",math.pi*5*5/(20*20),0.1)


exit(nErrs)
