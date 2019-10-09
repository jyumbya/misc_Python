# Description: Project each raster in the folder
# Author: Mutua John
# Date: 09/06/15

import os
import arcpy
from arcpy import env
from arcpy.sa import *


class RasterProjector(object):
    """Get raster files and project"""

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

    def proj_ras(self):
        """Project each raster as specified"""
        for source_path in self.get_dir_paths():
            for file in os.listdir(source_path):
                if file.startswith("africa_") & file.endswith(".tif"):  # Check if TIF file
                    file_path = os.path.join(source_path, file).replace("\\","/")
                    out_ras = "E:/Omusati_covariates/ndvi/processed_data/" + file
                    print("PROJECTING ...... " + file)
                    arcpy.ProjectRaster_management(file_path, out_ras, "PROJCS['UTM_Zone_33S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',15.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "NEAREST", "250 250", "", "", "PROJCS['Sphere_Sinusoidal',GEOGCS['GCS_Sphere',DATUM['D_Sphere',SPHEROID['Sphere',6370997.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Sinusoidal'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',30.0],UNIT['Meter',1.0]]")
        print("ALL RASTERS PROJECTED SUCCESSFULLY!!!!!")


def main():
    """Main program"""
    # Check out any necessary licenses
    env.overwriteOutput = True
    arcpy.CheckOutExtension("spatial")
    ras_projector = RasterProjector("E:/Omusati_covariates/ndvi/data")
    ras_projector.proj_ras()

if __name__ == "__main__":
    main()
