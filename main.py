from PIL import Image, ExifTags

img = Image.open("IMG_0854.JPG")
exifData = img._getexif()

if exifData:
    exif = {ExifTags.TAGS[k]: v for k, v in exifData.items() if k in ExifTags.TAGS}
    print(exif)
else:
    exif = {}

if "GPSInfo" in exif:
    def gpsInfoConverting(gpsInfo):
        latDegrees, latMinutes, latSeconds = gpsInfo[2]
        latDirection = gpsInfo[1]

        lonDegrees, lonMinutes, lonSeconds = gpsInfo[4]
        lonDirection = gpsInfo[3]

        latitudeStr = f"{int(latDegrees)}°{int(latMinutes)}'{float(latSeconds):.2f}\" "
        longitudeStr = f"{int(lonDegrees)}°{int(lonMinutes)}'{float(lonSeconds):.2f}\" "

        decimalLat = int(latDegrees) + float(latMinutes)/60 + float(latSeconds)/3600
        decimalLong = int(lonDegrees) + float(lonMinutes) / 60 + float(lonSeconds) / 3600

        return decimalLat, decimalLong, latitudeStr, longitudeStr, latDirection, lonDirection

    gpsInfo = gpsInfoConverting(exif["GPSInfo"])
    decimalLat, decimalLong, sexagesimalLat, sexagesimalLong, latDirection, longDirection = gpsInfo
    print(f'''
███████████████████████████████████████

Десятичные координаты:
{decimalLong} {longDirection}
{decimalLat} {latDirection}

███████████████████████████████████████

Шестидесятиричные координаты:
{sexagesimalLong} {longDirection}
{sexagesimalLat} {latDirection}

███████████████████████████████████████

Ссылка на яндекс картах:
https://yandex.ru/maps/213/moscow/?ll={decimalLong}%2C{decimalLat}&mode=whatshere&whatshere%5Bpoint%5D={decimalLong}%2C{decimalLat}
    ''')
else:
    print("Файл не содержит метаданных о геопозиции, или произошла ошибка")
