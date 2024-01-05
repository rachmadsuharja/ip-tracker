from geoip2 import database

def getLocation(ip_address):
    reader = database.Reader('GeoLite2-City_20240102/GeoLite2-City.mmdb')
    try:
        response = reader.city(ip_address)
        country = response.country.name
        city = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        timezone = response.location.time_zone
        radius = response.location.accuracy_radius

        print(f"IP Address : {ip_address}")
        print(f"Country : {country}")
        print(f"City : {city}")
        print(f"Latitude : {latitude}")
        print(f"Longitude : {longitude}")
        print(f"Time Zone : {timezone}")
        print(f"Accuracy Radius : {radius}")

        print(f"Success Tracking IP {ip_address}")

    except Exception as e:
        print(f"Failed fetch IP Address : {str(e)}")
    finally:
        reader.close

ip_address = input("Enter IP : ")
getLocation(ip_address)