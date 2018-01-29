import arcpy
import os

class Toolbox(object):
    def __init__(self):
        self.label =  "NewSeptic"
        self.alias  = "NewSeptic"

        # List of tool classes associated with this toolbox
        self.tools = [GetViableContours]

class GetViableContours(object):
    def __init__(self):
        self.label       = "Get Contour Lines"
        self.description = "Get all contours within a polygon parcel."

    def getParameterInfo(self):
        #Define parameter definitions

        # Contour Features parameter
        contour_lines = arcpy.Parameter(
            displayName="Contour Features",
            name="contour_lines",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        contour_lines.filter.list = ["Polyline"]

        # Contour Features parameter
        parcel_polygon = arcpy.Parameter(
            displayName="Parcel Features",
            name="parcel_polygon",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        parcel_polygon.filter.list = ["Polygon"]

        # Parcel Number Features parameter
        parcel_number = arcpy.Parameter(
            displayName="Parcel Number",
            name="parcel_number",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        # Derived Output Features parameter
        out_features = arcpy.Parameter(
            displayName="Contour Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")

        out_features.parameterDependencies = [contour_lines.name]
        out_features.schema.clone = True

        parameters = [contour_lines, parcel_polygon, parcel_number, out_features]

        return parameters

    def isLicensed(self): #This will verify the license is valid
        #if license is not valid
        return True

    #def updateParameters(self, parameters): #optional
    #    if parameters[0].altered:
    #        parameters[1].value = arcpy.ValidateFieldName(parameters[1].value,
    #                                                      parameters[0].value)
    #    return

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, messages):
    
        arcpy.env.overwriteOutput = True
        #contourLines = parameters[0].valueAsText
        parcelPolygon = r'C:\Users\crpge\Desktop\Medina\ParcelLines\parcelp.shp' #parameters[1].valueAsText
        parcelId = parameters[2].valueAsText  
        
        #parcelShape = arcpy.Describe(parcelPolygon).shapeFieldName

        mxd = arcpy.mapping.MapDocument(r"C:\Users\crpge\Desktop\Medina\Medina.mxd")
        df = arcpy.mapping.ListDataFrames(mxd)
        
        #input = parcelPolygon
        #in_path = arcpy.Describe(input).catalogPath
        out_path = r'C:\Users\crpge\Desktop\Medina\CreatedData'
        #output_Layer = "ourFoundParcel" 
        whereClause = '"PPNUMBER"' + " = '" + str(parcelId) + "'"
        arcpy.MakeFeatureLayer_management(parcelPolygon, "parcelOutput", whereClause)
        #arcpy.SelectLayerByAttribute_management ('parcelOutput', 'NEW_SELECTION', '"PPNUMBER" = "03608A08027"')
        #arcpy.SelectLayerByAttribute_management ('lyr', 'NEW_SELECTION', '"PPNUMBER" =  {}'.format(parcelId))
        #arcpy.CopyFeatures_management("parcelOutput", outLayer)
        #addLayer = arcpy.mapping.Layer("parcelOutput")
        arcpy.FeatureClassToShapefile_conversion('parcelOutput', out_path)
        #arcpy.mapping.AddLayer(df, "myParcels", "BOTTOM")
        #arcpy.RefreshTOC()
