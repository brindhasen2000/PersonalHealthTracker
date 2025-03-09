# PersonalHealthTracker
PersonalHealthTracker is a software that collects health metrics from wearable device; classifies the data under normal and abnormal health metrics, and eventually plots it on a map and showcases the interaction and spread of abnormal (infected) data.

--------------Overview--------------

This project visualizes patient health data on an interactive map using the Folium library in Python. Each patient is represented as a node on the map, with colors indicating their health status:

Green nodes: Patients with normal health metrics.

Red nodes: Patients with at least one abnormal health metric.

The data is read from a CSV file containing patient health metrics and location data. The program processes this data, classifies patients as normal or abnormal, and generates an HTML file displaying the interactive map.

--------------Features--------------

Reads patient health data from a CSV file.

Classifies patients as normal or abnormal based on predefined health metric ranges.

Plots patients on a Folium map as circle markers.

Uses different colors to indicate normal (green) and abnormal (red) health status.

Saves the interactive map as an HTML file for viewing in a web browser.

--------------Installation Prerequisites--------------

Ensure you have Python installed on your system. You will also need the following Python libraries:

- pandas

- numpy

- folium

You can install the required dependencies using pip:

pip install pandas numpy folium

--------------Instruction to run the python:--------------

Step 1 : Run PackageInstaller.py -> this installed all the necessary .py packages

Step 2: Run Spreading.py -> be patient, this will take a while. Finally it will generate the "health_simulation.html" to view the map.

--------------CSV File Format--------------

The input CSV file should contain the following columns:

Patient ID: Unique identifier for each patient.

Latitude: Geographical latitude of the patient.

Longitude: Geographical longitude of the patient.

Heart Rate: Heart rate measurement.

Respiratory Rate: Breathing rate measurement.

Body Temperature: Body temperature measurement.

Oxygen Saturation: Oxygen saturation level.

Systolic Blood Pressure: Systolic blood pressure measurement.

Diastolic Blood Pressure: Diastolic blood pressure measurement.

Example:

Patient ID,Latitude,Longitude,Heart Rate,Respiratory Rate,Body Temperature,Oxygen Saturation,Systolic Blood Pressure,Diastolic Blood Pressure
1,37.7749,-122.4194,75,16,36.5,98,110,70
2,34.0522,-118.2437,55,22,38.0,92,130,85
