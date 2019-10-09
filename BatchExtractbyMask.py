__author__ = 'jmutua'

import os
import arcpy
from arcpy import env
from arcpy.sa import *


class RasterExtractor(object):
    """Get raster files and extract as specified"""

    def __init__(self, s_dir):
        self.s_dir = s_dir

    def get_dir_paths(self):
        """Get file directory path"""
        tiff_dirs = []
        for root_path, dir_names, files in os.walk(self.s_dir):  # walk through root directory
            for dir_name in dir_names:
                if dir_name == "ISRIC_250m":
                    dir_join = os.path.join(root_path, dir_name).replace("\\","/")  # Join root to sub-directory
                    tiff_dirs.append(dir_join)
        print(tiff_dirs)
        return tiff_dirs

    def extract_ras(self):
        """Extract all rasters in the directory"""
        for source_path in self.get_dir_paths():
            for file in os.listdir(source_path):
                if file.startswith("af_") & file.endswith(".tif"):  # Check if TIF file
                    file_path = os.path.join(source_path, file).replace("\\","/")
                    out_ras = "D:/ToBackup/Projects/SWAT/ArcSWAT_Projects/Sasumua_data/Extra_info/New_simulation/Tana_soil_clustering/Soil_rasters/" + file
                    print("EXTRACTING ...... " + file)
                    arcpy.gp.ExtractByMask_sa(file_path, "C:/Users/jymutua/Documents/QSWAT_Projects/Sasumua_data/Boundaries/Sasumua_outline.shp", out_ras)
        print("ALL RASTERS EXTRACTED SUCCESSFULLY!!!!!")


def main():
    """Main program"""
    # Check out any necessary licenses
    env.overwriteOutput = True
    arcpy.CheckOutExtension("spatial")
    ras_extractor = RasterExtractor("Z:/CIAT GIS DATASETS/Regional Level/Africa")
    ras_extractor.extract_ras()

if __name__ == "__main__":
    main()
