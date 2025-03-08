import pandas as pd

# Define ranges for categorization
normal_range = {
    'Heart Rate': (60, 100),  # Normal Heart Rate (BPM)
    'Respiratory Rate': (12, 20),  # Normal Respiratory Rate (breaths per min)
    'Blood Pressure': [(90, 60), (120, 80)],  # Normal BP: 90/60 - 120/80 mmHg
    'Body Temperature': (35.6, 37.3),  # Normal Body Temperature (°C)
    'Oxygen Saturation': (96, 100),  # Normal SpO2 (%)
    'Age': (18, 65),  # Normal Age Range for adults (years)
    'Gender': ['Male', 'Female'],  # Normal Gender Categories
    'Weight (kg)': (45, 80),  # Normal weight range (kg)
    'Height (m)': (1.5, 1.9),  # Normal height range (m)
    'Derived_HRV': (40, 100),  # Normal HRV (ms, general range)
    'Derived_Pulse_Pressure': (30, 40),  # Normal Pulse Pressure (mmHg)
    'Derived_BMI': (18.5, 24.9),  # Normal BMI range (kg/m^2)
    'Derived_MAP': (70, 105),  # Normal Mean Arterial Pressure (mmHg)
}

semi_normal_range = {
    'Blood Pressure': [(130, 80), (139, 89)],  # High BP Stage 1: 130/80 - 139/89 mmHg
    'Blood Pressure Stage 2': (140, 90),  # High BP Stage 2: >140/90 mmHg
    'Low Blood Pressure': (90, 60),  # Low BP: <90/60 mmHg
    'Body Temperature Low Grade': (37.3, 38),  # Low Grade Fever: 37.3°C to 38°C
    'Body Temperature Moderate Grade': (38.1, 39),  # Moderate Grade Fever: 38.1°C to 39°C
    'Age': (65, 80),  # Older Age Range (years)
    'Weight (kg)': (35, 45),  # Underweight (kg)
    'Height (m)': (1.3, 1.5),  # Shorter than normal height (m)
    'Derived_HRV': (30, 40),  # Low HRV (ms)
    'Derived_Pulse_Pressure': (20, 30),  # Low Pulse Pressure (mmHg)
    'Derived_BMI': (25, 29.9),  # Overweight BMI range (kg/m^2)
    'Derived_MAP': (50, 70),  # Low Mean Arterial Pressure (mmHg)
}

abnormal_range = {
    'Blood Pressure': (180, 90),  # Hypertensive Crisis: >180/90 mmHg
    'Body Temperature Hypothermia': (39.1, 41),  # Hypothermia: 39.1°C to 41°C
    'Oxygen Saturation': (0, 90),  # Hypoxia: <90% oxygen saturation
    'Age': (80, 100),  # Very old age range (years)
    'Weight (kg)': (5, 35),  # Severe underweight (kg)
    'Height (m)': (0, 1.3),  # Extremely short height (m)
    'Derived_HRV': (0, 30),  # Very low HRV (ms)
    'Derived_Pulse_Pressure': (0, 20),  # Very low Pulse Pressure (mmHg)
    'Derived_BMI': (30, 50),  # Obese BMI range (kg/m^2)
    'Derived_MAP': (0, 50),  # Extremely low Mean Arterial Pressure (mmHg)
}

# Function to categorize BMI
def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize BMI according to standard ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def categorize_data(row):
    """Categorize a single data entry as normal, semi-normal, or abnormal."""
    category = 'Normal'

    # BMI Calculation
    bmi = calculate_bmi(row['Weight (kg)'], row['Height (m)'])
    bmi_category = categorize_bmi(bmi)
    row['Derived_BMI'] = bmi
    row['BMI Category'] = bmi_category
    
    # Check Heart Rate, Respiratory Rate, Blood Pressure, etc.
    if row['Heart Rate'] < normal_range['Heart Rate'][0] or row['Heart Rate'] > normal_range['Heart Rate'][1]:
        category = 'Semi-Normal'
    if row['Respiratory Rate'] < normal_range['Respiratory Rate'][0] or row['Respiratory Rate'] > normal_range['Respiratory Rate'][1]:
        category = 'Semi-Normal'
    if (row['Systolic Blood Pressure'] < normal_range['Blood Pressure'][0][0] or row['Systolic Blood Pressure'] > normal_range['Blood Pressure'][1][0] or 
        row['Diastolic Blood Pressure'] < normal_range['Blood Pressure'][0][1] or row['Diastolic Blood Pressure'] > normal_range['Blood Pressure'][1][1]):
        category = 'Semi-Normal'
    if row['Body Temperature'] < normal_range['Body Temperature'][0] or row['Body Temperature'] > normal_range['Body Temperature'][1]:
        category = 'Semi-Normal'
    if row['Oxygen Saturation'] < normal_range['Oxygen Saturation'][0] or row['Oxygen Saturation'] > normal_range['Oxygen Saturation'][1]:
        category = 'Semi-Normal'
    
    # Check for Semi-Normal conditions
    if row['Systolic Blood Pressure'] >= semi_normal_range['Blood Pressure'][0][0] and row['Systolic Blood Pressure'] <= semi_normal_range['Blood Pressure'][1][0] and \
       row['Diastolic Blood Pressure'] >= semi_normal_range['Blood Pressure'][0][1] and row['Diastolic Blood Pressure'] <= semi_normal_range['Blood Pressure'][1][1]:
        category = 'Semi-Normal'
    elif row['Systolic Blood Pressure'] > semi_normal_range['Blood Pressure Stage 2'][0] and row['Diastolic Blood Pressure'] > semi_normal_range['Blood Pressure Stage 2'][1]:
        category = 'Semi-Normal'
    elif row['Body Temperature'] >= semi_normal_range['Body Temperature Low Grade'][0] and row['Body Temperature'] <= semi_normal_range['Body Temperature Low Grade'][1]:
        category = 'Semi-Normal'
    elif row['Body Temperature'] >= semi_normal_range['Body Temperature Moderate Grade'][0] and row['Body Temperature'] <= semi_normal_range['Body Temperature Moderate Grade'][1]:
        category = 'Semi-Normal'

    # Check for Abnormal conditions
    if row['Systolic Blood Pressure'] > abnormal_range['Blood Pressure'][0] and row['Diastolic Blood Pressure'] > abnormal_range['Blood Pressure'][1]:
        category = 'Abnormal'
    elif row['Body Temperature'] >= abnormal_range['Body Temperature Hypothermia'][0] and row['Body Temperature'] <= abnormal_range['Body Temperature Hypothermia'][1]:
        category = 'Abnormal'
    elif row['Oxygen Saturation'] < abnormal_range['Oxygen Saturation'][0]:
        category = 'Abnormal'
    elif row['Weight (kg)'] < abnormal_range['Weight (kg)'][0]:
        category = 'Abnormal'
    elif row['Height (m)'] < abnormal_range['Height (m)'][0]:
        category = 'Abnormal'
    elif row['Derived_HRV'] < abnormal_range['Derived_HRV'][0]:
        category = 'Abnormal'
    elif row['Derived_Pulse_Pressure'] < abnormal_range['Derived_Pulse_Pressure'][0]:
        category = 'Abnormal'
    elif row['Derived_BMI'] > abnormal_range['Derived_BMI'][0]:
        category = 'Abnormal'
    elif row['Derived_MAP'] < abnormal_range['Derived_MAP'][0]:
        category = 'Abnormal'

    return category

# Load the dataset
file_path = "data/human_vitals_with_location.csv"  # Add path to your dataset
df = pd.read_csv(file_path)
print("read file successfully")

# Apply the categorization function to each row
df['Risk Category'] = df.apply(categorize_data, axis=1)

# Save the categorized dataset to a new file (optional)
output_path = "[your_output_path_here]"  # Add path for output
df.to_csv(output_path, index=False)

# print("Categorization complete. Output saved at:", output_path)
