# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Landsat_processing.py
# Created on: 2017-08-17 10:56:30.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Landsat_processing <Use_Input_Features_for_Clipping_Geometry> <Don_50_shp> <LS8_OLI_TIRS_NBAR_P54_GANBAR01_032_094_074_20160610_B4_tif> <LS8_OLI_TIRS_NBAR_P54_GANBAR_tif>
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os
import time
t0 = time.time()
#Data

clip_shape = "C:\PhD\junk\mary_shape.shp"
out_folder = r"C:\PhD\junk"
band_1 = 'B4'
band_2 = 'B5'
band_3 = 'B6'
rgb_inputs = os.path.join(out_folder, clip_shape[-10:-4] + '_' + band_1 + '.tif') +';' + os.path.join(out_folder, clip_shape[-10:-4] + '_' + band_2 + '.tif') + ';' + os.path.join(out_folder, clip_shape[-10:-4] + '_' + band_3 + '.tif')
rgb_out = clip_shape[-10:-4] + '_' + str(band_1[-1:]) + str(band_2[-1:]) + str(band_3[-1:]) + '.tif'
rgb_file = os.path.join(out_folder, rgb_out)
Use_Input_Features_for_Clipping_Geometry = "true"
root = r"C:\PhD\junk\LS8_OLI_TIRS_NBAR_P54_GANBAR01-032_090_078_20140726\scene01"
os.chdir(root)

for (dirpath, dirnames, filenames) in os.walk('.'):
    for file in filenames:
        if file.endswith('.tif'):
            image_raster = arcpy.sa.Raster(file)
            left = int(image_raster.extent.XMin)
            right = int(image_raster.extent.XMax)
            top = int(image_raster.extent.YMax)
            bottom = int(image_raster.extent.YMin)
            new = os.path.join(out_folder, clip_shape[-10:-4] + file[-7:])
            extent = str(left) + ' ' + str(bottom) + ' ' + str(right) + ' ' + str(top)
            arcpy.Clip_management(file, extent, new, clip_shape, "-999", Use_Input_Features_for_Clipping_Geometry, "NO_MAINTAIN_EXTENT")
            print new

arcpy.CompositeBands_management(rgb_inputs, rgb_file)


print ""
print "Time taken:"
print "hours: %i, minutes: %i, seconds: %i" %(int((time.time()-t0)/3600), int(((time.time()-t0)%3600)/60), int((time.time()-t0)%60))





