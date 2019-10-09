# Description: Aggregate each raster in a folder using a specified cell factor
# Author: Mutua John
# Date: 19/05/15

import os
import arcpy
from arcpy import env
from arcpy.sa import *


class RasterAggregator(object):
    """Get raster files and aggregate"""

    def __init__(self, s_dir):
        self.s_dir = s_dir

    def get_dir_paths(self):
        """Get file directory path"""
        tiff_dirs = []
        for root_path, dir_names, files in os.walk(self.s_dir):  # walk through root directory
            for dir_name in dir_names:
                if dir_name == "africa_crop_yield":
                    dir_join = os.path.join(root_path, dir_name).replace("\\","/")  # Join root to sub-directory
                    tiff_dirs.append(dir_join)
        print(tiff_dirs)
        return tiff_dirs

    def agg_ras(self):
        """Aggregate each raster as specified"""
        for source_path in self.get_dir_paths():
            for file in os.listdir(source_path):
                if file.startswith("africa_") & file.endswith(".tif"):  # Check if TIF file
                    file_path = os.path.join(source_path, file).replace("\\","/")
                    out_ras = "D:/Data/Projects/CSIRO_Suitability/africa_crop_yield_agg/" + file
                    print("AGGREGATING ...... " + file)
                    arcpy.gp.Aggregate_sa(file_path, out_ras, "10", "MEAN", "EXPAND", "NODATA")
        print("ALL RASTERS AGGREGATED SUCCESSFULLY!!!!!")


def main():
    """Main program"""
    # Check out any necessary licenses
    env.overwriteOutput = True
    arcpy.CheckOutExtension("spatial")
    ras_aggregator = RasterAggregator("D:/Data/Projects/CSIRO_Suitability")
    ras_aggregator.agg_ras()

if __name__ == "__main__":
    main()
