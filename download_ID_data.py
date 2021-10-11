
from products import products_gdf
from function_download_ID_data import Download_Random_ProductID_Sentinel2_Data
from param import path_geojson_file, start_date, end_date


products_gdf_uuid = products_gdf.uuid


def main():

    Download_Random_ProductID_Sentinel2_Data(path_geojson_file, start_date, end_date)



if __name__ == "__main__":
    main()
