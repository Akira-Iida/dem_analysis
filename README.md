# DEM Analysis

This repository contains code to analyze the SRTM 90m Digital Elevation Model for a specific tile.

## How to run the code

1. Install the required libraries:

  pip install rasterio matplotlib numpy

2. Run the Python script:

  python dem_analysis.py

## Summary
This code retrieves the SRTM 90m Digital Elevation Model for the northern area of Japan, creates an overview image, and plots the altitude profile between two specified image coordinates.

* Overview Image
The overview image shows the elevation data with water bodies set to 0m.

* Altitude Profile
The altitude profile is plotted between the following image coordinates:

  Start point: (row, col) = (3600, 1200)
  End point: (row, col) = (1200, 4800)
