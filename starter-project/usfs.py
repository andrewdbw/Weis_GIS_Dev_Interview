import json
import os

from datetime import datetime
from urllib import parse
from urllib import request


class usfs_api:

    def __init__(self):

        self.edw_rest_api = "https://apps.fs.usda.gov/arcx/rest/services/EDW/?f=pjson"
        self.edw_service_api = "https://apps.fs.usda.gov/arcx/rest/services/{0}/MapServer?f=pjson"
        self.nf_boundaries_query_api = "https://apps.fs.usda.gov/arcx/rest/services/EDW/EDW_ForestSystemBoundaries_01/MapServer/0/query?"

        self.loaded_services = None
        

    def get_all_services(self):

        all_services_json = []

        # Get USFS EDW ArcGIS Api response
        api_response = request.urlopen(self.edw_rest_api)

        # Transform Response to Json
        edw_json = json.loads(api_response.read())

        # Iterate over All Map Services and Retrieve Layer Results
        for map_service in edw_json["services"]:

            service_dictionary = self.get_map_service(map_service)

            all_services_json.append(service_dictionary)
            
        # Set Loaded Services and return json
        self.loaded_services = all_services_json

        return all_services_json


    def get_map_service(self, map_service_json):

        # Get API Repsonse & Load to Json
        service_api_response = request.urlopen(self.edw_service_api.format(map_service_json["name"]))
        service_json = json.loads(service_api_response.read())

        # Transform to Dictionary
        service_dictionary = self.transform_map_service_to_dictionary(service_json, map_service_json["type"])

        return service_dictionary


    def transform_map_service_to_dictionary(self, edw_service_json, service_type):

        map_service_dictionary = {
            edw_service_json["mapName"] : {
                'type' : service_type,
                'layers': edw_service_json["layers"]
            }
        }
        
        return map_service_dictionary
    
    def export_loaded_services(self):

        output_folder = os.path.join(os.path.dirname(__file__), "output")

        filename = "edw_services_{0}.json".format(datetime.now().strftime("%m_%d_%Y__%H_%M_%S"))

        if self.loaded_services != None:

            # Attempt creation of output directory
            try:
                os.mkdir(output_folder)
            except FileExistsError:
                # Directory Already Exists
                pass

            with open(os.path.join(output_folder, filename), "w") as outfile:
                outfile.write(json.dumps(self.loaded_services, indent=2))

            print("Exported to {0}".format(os.path.join(output_folder, filename)))
        else:
            print("No Services Loaded")


    def query_forest_system_boundaries(self, params):

        query_url = self.nf_boundaries_query_api + parse.urlencode(params)
        result = json.loads(request.urlopen(query_url).read())

        return result


    def get_forests_startswith_s(self):

        startswith_s_params = {
            'where' : "FORESTNAME LIKE 'S%'",
            'outFields' : "['FORESTNAME', 'GIS_ACRES']",
            'returnGeometry' : 'false',
            'f' : 'pjson'
        }

        query_result = self.query_forest_system_boundaries(startswith_s_params)

        return_list = []

        for feature in query_result["features"]:
            return_list.append(feature["attributes"]["FORESTNAME"])

        return return_list


    def get_num_forests_larger_than_100k(self):

        larger_than_100k_params = {
            'where' : 'GIS_ACRES > 100000',
            'returnCountOnly' : 'true',
            'f' : 'pjson'
        }

        query_result = self.query_forest_system_boundaries(larger_than_100k_params)

        forest_count_larger_than_100k = int(query_result["count"])

        return forest_count_larger_than_100k

