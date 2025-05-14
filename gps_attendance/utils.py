
from geopy.distance import geodesic



def valid_distance_to_gps(origin, user_location,gps_distance):
	# frappe.errprint(f'distancd -- > {gps_distance}')
	d_meter =  geodesic(origin, user_location).meters
	return d_meter if d_meter <= gps_distance else -1
