import numpy as np


class Calculation:
    """
    A utility class for calculation
    """

    @staticmethod
    def cal_great_circle_distance(lat1, long1, lat2, long2):
        """
        Calculate great circle distance between two point

        Parameters
        ----------
        lat1 : float[]
            Latitude of first point(s)
        long1 : float[]
            Longitude of first point(s)
        lat2 : float[]
            Latitude of second point(s)
        long2 : float[]
            Longitude of second point(s)

        Returns
        -------
        distance : float[]
            Great circle distance [km]

        Note
        ----
        Haversine distance https://en.wikipedia.org/wiki/Haversine_formula using mean Earth radius 6371.009 for the WGS84 ellipsoid
        """
        return 2.0 * 6371.0 * np.arcsin(np.sqrt(np.sin(np.deg2rad(lat2 - lat1)/2.0)**2.0 + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(np.deg2rad(long2 - long1)/2.0)**2.0))\

    
    @staticmethod
    def cal_great_circle_bearing(lat1, long1, lat2, long2):
        """
        Calculate bearing of two points following great circle path 

        Parameters
        ----------
        lat1 : float[]
            Latitude of first point(s)
        long1 : float[]
            Longitude of first point(s)
        lat2 : float[]
            Latitude of second point(s)
        long2 : float[]
            Longitude of second point(s)

        Returns
        -------
        bearing : float[]
            Bearing [deg]

        Note
        ----
        Forward azimuth https://www.movable-type.co.uk/scripts/latlong.html
        """
        return np.rad2deg(np.arctan2(np.sin(np.deg2rad(long2-long1)) * np.cos(np.deg2rad(lat2)), np.cos(np.deg2rad(lat1))*np.sin(np.deg2rad(lat2)) - np.sin(np.deg2rad(lat1))*np.cos(np.deg2rad(lat2))*np.cos(np.deg2rad(long2-long1))))
        # const brng = (θ*180/Math.PI + 360) % 360; // in degrees TODO: need?