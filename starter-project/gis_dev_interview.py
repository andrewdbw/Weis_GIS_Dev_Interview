from usfs import *

def main():

    api = usfs_api()

    # Question 1: 
    # Find all the Map Services at our USFS public facing EDW ArcGIS REST API
    # Output should be in format: {‘service name': {'type': service type, 'layers': [info from layer attribute]}}

    print("Question #1\n")
    
    # Get All Services and Output All Services to JSON file: starter-project/output/edw_services_{date}.
    
    print("Starting EDW Service Extraction")
    edw_services = api.get_all_services()
    api.export_loaded_services()


    #######################################################

    # Question 2:
    # From the EDW_ForestSystemBoundaries_01 service use Python to 
    #   - Get an array of all the National Forests whose name starts with the letter S.
    #   - Get the count, as an integer, of all the National forests greater than 100,000 acres.

    print("\n\nQuestion #2\n")

    array_result = api.get_forests_startswith_s()
    print("\nNational Forests whose name starts with the letter 'S'")
    [print("\t" + i) for i in array_result]

    integer_result = api.get_num_forests_larger_than_100k()
    print("\nNumber of National Forests greater than 100,000 acres: {0}".format(integer_result))
    
    



if __name__ == "__main__":
    main()