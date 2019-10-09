#Author = John Mutua

import os
import arcpy
from arcpy import env
from arcpy.sa import *


class ZonalExtractor(object):
    """Get zonal stats from rasters"""

    def __init__(self, s_dir):
        self.s_dir = s_dir

    def get_dir_paths(self):
        """Get file directory path"""
        tiff_dirs = []
        for root_path, dir_names, files in os.walk(self.s_dir):  # walk through root directory
            for dir_name in dir_names:
                if dir_name == "Unzipped":
                    dir_join = os.path.join(root_path, dir_name).replace("\\","/")  # Join root to sub-directory
                    tiff_dirs.append(dir_join)
        print(tiff_dirs)
        return tiff_dirs

    def extract_stats(self):
        """Extract stats"""
        for source_path in self.get_dir_paths():
            for file in os.listdir(source_path):
                if file.startswith("af_") & file.endswith(".tif"):  # Check if TIF file
                    file_path = os.path.join(source_path, file).replace("\\","/")
                    out_ras = "D:/ToBackup/Projects/SWAT/ArcSWAT_Projects/Sasumua_data/Extra_info/New_simulation/Tana_soil_clustering/Soil_rasters/" + file
                    print("ZONAL STATS EXTRACTION ONGOING ...... " + file)
                    arcpy.gp.ZonalStatistics_sa("D:/ToBackup/Projects/SWAT/ArcSWAT_Projects/Sasumua_data/Extra_info/New_simulation/Tana_soil_clustering/250m_soil_clusters.shp", "SS_GROUP", file_path, out_ras, "MEDIAN", "DATA")
        print("ALL ZONAL STATS EXTRACTED SUCCESSFULLY!!!!!")


def main():
    """Main program"""
    # Check out any necessary licenses
    env.overwriteOutput = True
    arcpy.CheckOutExtension("spatial")
    zonal_extract = ZonalExtractor("E:/Data/Regional/Soil properties")
    zonal_extract.extract_stats()

if __name__ == "__main__":
    main()
