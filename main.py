from PIL import Image, ExifTags

img = Image.open("img.jpg")
exif_data = img._getexif()

if exif_data:
    exif = {ExifTags.TAGS[k]: v for k, v in exif_data.items() if k in ExifTags.TAGS}
    print(exif)
else:
    exif = {}

if "GPSInfo" in exif:
    def gps_info_to_string(gps_info):
        lat_degrees, lat_minutes, lat_seconds = gps_info[2]
        lat_direction = gps_info[1]

        lon_degrees, lon_minutes, lon_seconds = gps_info[4]
        lon_direction = gps_info[3]

        latitude_str = f"{int(lat_degrees)}°{int(lat_minutes)}'{float(lat_seconds):.2f}\" {lat_direction}"
        longitude_str = f"{int(lon_degrees)}°{int(lon_minutes)}'{float(lon_seconds):.2f}\" {lon_direction}"

        return f"{latitude_str}, {longitude_str}"

    gps_string = gps_info_to_string(exif["GPSInfo"])
    print(gps_string)
else:
    print("No info found")
