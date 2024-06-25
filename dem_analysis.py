import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Specify the path of the downloaded GeoTIFF file
dem_file_path = 'srtm_65_04.tif'

def get_altitude(dem_file_path, longitude, latitude):
    with rasterio.open(dem_file_path) as src:
        row, col = rasterio.transform.rowcol(src.transform, longitude, latitude)
        band = src.read(1)
        hgt = band[row, col]
        return hgt

def create_overview_image(dem_file_path):
    with rasterio.open(dem_file_path) as src:
        band = src.read(1)
        band[band == -32768] = 0  # Replace no data values ​​for water bodies with 0
        plt.imshow(band, cmap='jet')
        plt.colorbar(label='Elevation (m)')
        plt.title('Overview of DEM')
        plt.xlabel('Column')
        plt.ylabel('Row')
        plt.show()

def plot_altitude_profile(dem_file_path, start, end):
    with rasterio.open(dem_file_path) as src:
        band = src.read(1)
        band[band == -32768] = 0  # Replace no data values ​​for water bodies with 0
        
        start_row, start_col = start
        end_row, end_col = end

        num_samples = 500  # Any number of samples
        rows = np.linspace(start_row, end_row, num_samples)
        cols = np.linspace(start_col, end_col, num_samples)

        altitudes = [band[int(row), int(col)] for row, col in zip(rows, cols)]

        plt.plot(altitudes)
        plt.title('Altitude Profile')
        plt.xlabel('Sample')
        plt.ylabel('Elevation (m)')
        plt.show()

# Running the demo
create_overview_image(dem_file_path)
plot_altitude_profile(dem_file_path, (3600, 1200), (1200, 4800))
