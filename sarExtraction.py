import arcpy

#Loops over a folder and creates a jpeg image out of each tiff in the folder
import os, sys, cv2
from PIL import Image

base_path = "C:/Hackathon/"
for infile in os.listdir(base_path):
    print("file : " + infile)
    if infile[-4:] == "tiff":
        outfile = base_path + infile[:-4] + "jpeg"
        im = Image.open(base_path + infile)
        print("new filename :" + outfile)
        read = cv2.imread(base_path + infile)
        cv2.imwrite(outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 200])
        
        #calls the dlpx on the newly created jpeg file
        out_classified_raster = arcpy.ia.DetectObjectsUsingDeepLearning(outfile, r"C:/Users/cha12418/Documents/ArcGISProjects/Hackathon/Hackathon.gdb/" + infile + ".shp", r"C:/Hackathon/SARShipDetection.dlpk", "padding 56;threshold 0.5;nms_overlap 0.1;batch_size 64;exclude_pad_detections True", "NO_NMS", "Confidence", "Class", 0, "PROCESS_AS_MOSAICKED_IMAGE"); out_classified_raster.save(None)
