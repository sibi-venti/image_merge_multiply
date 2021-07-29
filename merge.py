import numpy as np
import cv2
import datetime
current_date = datetime.datetime.now()
src1 = cv2.imread('TB_TO_TC.png')
src1[np.where((src1==[0,0,0]).all(axis=2))] = [0,0,255]


src2 = cv2.imread('PPT_TB_TC_updated_with_VF.png')
src2[np.where((src2==[0,0,0]).all(axis=2))] = [255,0,0]

dst = cv2.addWeighted(src1,0.7,src2,0.3,0) 
filename = str(current_date.day)+str("_")+str(current_date.month)+str("_")+str(current_date.year)+str("_")+str(current_date.hour)+str("_")+str(current_date.minute)+str("_")+str(current_date.second) 

cv2.imwrite("merge_image_"+ filename + ".png" , dst)
