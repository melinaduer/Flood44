
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
import floodsystem.station




def run():
    stations = build_station_list()
    N = 9
    print(rivers_by_station_number(stations, N))

if __name__ == "__main__":
    print("\n *** Task 1E: rivers by number of stations *** \n")
    run()
