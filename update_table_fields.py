#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Simon Walker
#
# Created:     08/10/2017
# Copyright:   (c) Simon Walker 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

fc = 'C:\\PhD\\junk\Mary_subcatchments_mgaz56.shp'
fields = ['FID']

# Create update cursor for feature class
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    # For each row, evaluate the WELL_YIELD value (index position
    # of 0), and update WELL_CLASS (index position of 1)
    for row in cursor:
        if row[0] == 0:
            row[0] = 1
        # Update the cursor with the updated list
        cursor.updateRow(row)
        print row

