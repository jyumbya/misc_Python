import arcpy
import csv

arcpy.env.workspace = r"E:\CIATFINAL2_check"

headers = ["RNAME", "ROWCOUNT", "COLUMNCOUNT", "CELLSIZEX", "CELLSIZEY","TOP", "LEFT", "RIGHT", "BOTTOM","SPATIALREF"]

outputCSV = r"E:\CIATFINAL2_check\tzRasterProperties.csv"
wfile  = open(outputCSV, 'wb')
csvwriter = csv.writer(wfile)
csvwriter.writerow(headers)

for f in arcpy.ListRasters():
    
    try:
        ROWCOUNT = arcpy.GetRasterProperties_management(f,"ROWCOUNT")
        COLUMNCOUNT = arcpy.GetRasterProperties_management(f,"COLUMNCOUNT")
        CELLX = arcpy.GetRasterProperties_management(f,"CELLSIZEX")
        CELLY = arcpy.GetRasterProperties_management(f,"CELLSIZEY")
        TOP = arcpy.GetRasterProperties_management(f,"TOP")
        LEFT = arcpy.GetRasterProperties_management(f,"LEFT")
        RIGHT = arcpy.GetRasterProperties_management(f,"RIGHT")
        BOTTOM = arcpy.GetRasterProperties_management(f,"BOTTOM")
        SPATIALREF = arcpy.Describe(f).spatialReference
    except:
        print("had a problem getting stats for   {0} ".format(f))

    csvwriter.writerow([f, ROWCOUNT, COLUMNCOUNT, CELLX, CELLY, TOP, LEFT, RIGHT, BOTTOM,SPATIALREF])
