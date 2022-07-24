import arcpy

#Convert csv AIS to point class
arcpy.management.XYTableToPoint("unique_ship.csv", r"C:\Users\cha12418\Documents\ArcGIS\Projects\Hackathon\Hackathon.gdb\unique_ship_XYTableToPoint1", "LON", "LAT", None, 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision')

#Intersect AIS point class with detected ships
arcpy.analysis.Intersect("unique_ship_XYTableToPoint #;ships #", r"C:\Users\cha12418\Documents\ArcGIS\Projects\Hackathon\Hackathon.gdb\known_ships", "ALL", None, "INPUT")
