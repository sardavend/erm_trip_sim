import sys
import argparse
import os
from mapbox import Directions

os.environ["MAPBOX_ACCESS_TOKEN"] = "pk.eyJ1IjoibmltYnVzY2wiLCJhIjoiY2pmdTJzbnUzNDFwbzJ3cG9nc3c4aGhweiJ9.vkeNGrsjezxfRax2CEBuQg"
service = Directions()


def get_geojson(latlon):
    print("LATLON {0}".format(latlon))
    return {
        "type":"Feature",
        "properties":{"name", "Portland, OR"},
        "geometry":{
            "type":"Point",
            "coordinates":[latlon[1], latlon[0]]
        }
    }

def get_latlon(latlonstring):
    try:
        print("latlon string {0}".format(latlonstring))
        return list(map(float,latlonstring.split(',')))

    except Exception as e:
        print("an errar has ocurred while processing the latlonstring {0}".format(e))
        sys.exit(0)

def get_sim_trips(origin, destination):
    org = get_geojson(origin)
    dest = get_geojson(destination)
    response = service.directions([org, dest], 'mapbox.driving')
    if response.status_code == 200:
        driving_routes = response.geojson()
        print("driving routes {0}".format(driving_routes["features"]))
        print("Detected {0} routes between the origin and destination".format(len(driving_routes['features'])))
        return driving_routes
    return "Error!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin', type=get_latlon, help='lat and lon separated by comma')
    parser.add_argument('--destination', type=get_latlon, help='lat and lon separated by comma')
    args = vars(parser.parse_args())
    get_sim_trips(args["origin"], args["destination"])




