# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:51:21 2018

@author: Dr P.c rawat
"""

import numpy as np
import cv2
images=np.zeros((512,512,3),np.uint8)
myimage=cv2.line(images,(0,0),(511,511),(0,100,100),10)
cv2.imshow("mywindow",myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
