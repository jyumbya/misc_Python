import arcpy
import csv

arcpy.env.workspace = r"E:\Final_check"

#headers = ["RNAME", "ROWCOUNT", "COLUMNCOUNT", "CELLSIZEX", "CELLSIZEY","TOP", "LEFT", "RIGHT", "BOTTOM"]

#outputCSV = r"E:\Final_check\tzRasterProperties.csv"
#wfile  = open(outputCSV, 'wb')
#csvwriter = csv.writer(wfile)

#csvwriter.writerow(headers)

ras_properties = ["ROWCOUNT", "COLUMNCOUNT", "CELLSIZEX", "CELLSIZEY","TOP", "LEFT", "RIGHT", "BOTTOM"]
for f in arcpy.ListRasters():
    for p in ras_properties:
        print(arcpy.Describe(f).spatialReference.name)
        ras_prop = arcpy.GetRasterProperties_management(f, p)
        print('{0}  -   {1}'.format(p, ras_prop))
        
    



##    try:
##        ROWCOUNT = arcpy.GetRasterProperties_management(f,"ROWCOUNT")
##        COLUMNCOUNT = arcpy.GetRasterProperties_management(f,"COLUMNCOUNT")
##        CELLX = arcpy.GetRasterProperties_management(f,"CELLSIZEX")
##        CELLY = arcpy.GetRasterProperties_management(f,"CELLSIZEY")
##        TOP = arcpy.GetRasterProperties_management(f,"TOP")
##        LEFT = arcpy.GetRasterProperties_management(f,"LEFT")
##        RIGHT = arcpy.GetRasterProperties_management(f,"RIGHT")
##        BOTTOM = arcpy.GetRasterProperties_management(f,"BOTTOM")
##    except:
##        print("had a problem getting stats for   {0} ".format(f))
##
##    csvwriter.writerow([f, ROWCOUNT, COLUMNCOUNT, CELLSIZEX, CELLSIZEY,TOP, LEFT, RIGHT, BOTTOM])
