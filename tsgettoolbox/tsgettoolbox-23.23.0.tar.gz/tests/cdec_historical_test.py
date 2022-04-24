import numpy as np
import pandas as pd
import test_util

from tsgettoolbox import tsgettoolbox

# def test_get_stations():
#     stations_file = "cdec/historical/all_stations.csv"
#     with test_util.mocked_urls(stations_file):
#         stations = ulmo.cdec.historical.get_stations()
#     assert 2000 < len(stations)
#     assert u"PRA" in stations.index
#
#
# def test_get_sensors():
#     sensors_file = "cdec/historical/sensors.htm"
#     with test_util.mocked_urls(sensors_file):
#         sensors = ulmo.cdec.historical.get_sensors()
#     assert 200 < len(sensors)
#     sensors.index = sensors["Sensor No"].astype(int)
#     assert u"FLOW, RIVER DISCHARGE" == sensors.xs(20)["Description"]
#
#
# def test_get_station_sensors():
#     test_sets = [("PRA", [6, 6, 15, 15, 22, 23, 76])]
#
#     for station_id, test_value in test_sets:
#
#         stations_file = "cdec/historical/%s.htm" % (station_id)
#         with test_util.mocked_urls(stations_file):
#             available_sensors = ulmo.cdec.historical.get_station_sensors([station_id])
#
#         assert set(available_sensors[station_id].sensor_id.to_dict().values()) <= set(
#             test_value
#         )


def test_get_station_data():
    # tsgettoolbox cdec [-h] [--dur_code DUR_CODE]
    #                       [--sensor_num SENSOR_NUM]
    #                       [--start_date START_DATE]
    #                       [--end_date END_DATE]
    #                       station_id
    test_sets = [(u"PRA", u"RESERVOIR ELEVATION", ["2000-01-01", "2000-01-02"])]

    for station_id, var_name, test_values in test_sets:
        # data_regex = 'http://cdec.water.ca.gov/cgi-progs/queryCSV?station_id.*'
        # data_file = 'cdec/historical/%s.csv' % station_id
        # sensors_regex = 'http://cdec.water.ca.gov/misc/senslist.html'
        # sensors_file = 'cdec/historical/sensors.htm'

        # url_files = {sensors_regex: sensors_file, data_regex: data_file}
        # with test_util.mocked_urls(url_files):
        station_data = tsgettoolbox.cdec(
            station_id,
            sensor_num=var_name,
            dur_code="daily",
            start_date=test_values[0],
            end_date=test_values[1],
        )

        test_timestamps = [pd.Timestamp(t) for t in test_values]
        assert np.all(test_timestamps == station_data[station_id][var_name].index)
