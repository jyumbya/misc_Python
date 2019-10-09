# Description: Resample each raster in a folder using a specified cell factor
# Author: Mutua John
# Date: 06/06/15

import os
import arcpy
from arcpy import env
from arcpy.sa import *


class RasterResampler(object):
    """Get raster files and resample"""

    def __init__(self, s_dir):
        self.s_dir = s_dir

    def get_dir_paths(self):
        """Get file directory path"""
        tiff_dirs = []
        for root_path, dir_names, files in os.walk(self.s_dir):  # walk through root directory
            for dir_name in dir_names:
                if dir_name == "data":
                    dir_join = os.path.join(root_path, dir_name).replace("\\","/")  # Join root to sub-directory
                    tiff_dirs.append(dir_join)
        print(tiff_dirs)
        return tiff_dirs

    def res_ras(self):
        """Resample each raster as specified"""
        for source_path in self.get_dir_paths():
            for file in os.listdir(source_path):
                if file.startswith("af_") & file.endswith(".tif"):  # Check if TIF file
                    file_path = os.path.join(source_path, file).replace("\\","/")
                    out_ras = "D:/ToBackup/Data/Projects/Water_Fund/ThikaChania/CropSyst_Script/data_resampled1/" + file
                    print("RESAMPLING ...... " + file)
                    arcpy.Resample_management(file_path, out_ras, "92.53767284", "NEAREST")
        print("ALL RASTERS RESAMPLED SUCCESSFULLY!!!!!")


def main():
    """Main program"""
    # Check out any necessary licenses
    env.overwriteOutput = True
    arcpy.CheckOutExtension("spatial")
    ras_resampler = RasterResampler("D:/ToBackup/Data/Projects/Water_Fund/ThikaChania/CropSyst_Script")
    arcpy.env.snapRaster = "D:/ToBackup/Data/Projects/Water_Fund/ThikaChania/CropSyst_Script/data/Sasumua_Slope90m.tif"
    ras_resampler.res_ras()

if __name__ == "__main__":
    main()
