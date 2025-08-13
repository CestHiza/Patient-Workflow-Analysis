# generate_patient_flow_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(num_patients=100):
    """
    Generates a synthetic dataset simulating patient flow through a clinic.
    """
    print("--- Generating Synthetic Patient Flow Data ---")
    
    np.random.seed(42)
    
    data = []
    start_time = datetime(2025, 8, 6, 9, 0, 0) # Clinic opens at 9:00 AM
    
    for i in range(num_patients):
        patient_id = f"PAT{2000+i}"
        
        # Timestamps for each stage of the visit
        check_in_time = start_time + timedelta(minutes=np.random.randint(0, 420)) # Patients arrive throughout a 7-hour day
        
        # Wait time for nurse (5 to 20 minutes)
        nurse_triage_start = check_in_time + timedelta(minutes=np.random.randint(5, 20))
        
        # Time with nurse (3 to 10 minutes)
        nurse_triage_end = nurse_triage_start + timedelta(minutes=np.random.randint(3, 10))
        
        # Wait time for doctor - THIS IS OUR INTENTIONAL BOTTLENECK
        # We'll make this wait significantly longer (15 to 60 minutes)
        doctor_consult_start = nurse_triage_end + timedelta(minutes=np.random.randint(15, 60))
        
        # Time with doctor (10 to 25 minutes)
        doctor_consult_end = doctor_consult_start + timedelta(minutes=np.random.randint(10, 25))
        
        # Time to check-out (2 to 7 minutes)
        check_out_time = doctor_consult_end + timedelta(minutes=np.random.randint(2, 7))
        
        data.append({
            "PatientID": patient_id,
            "CheckInTime": check_in_time,
            "NurseTriageStart": nurse_triage_start,
            "DoctorConsultStart": doctor_consult_start,
            "CheckOutTime": doctor_consult_end # Note: Using consult end as a proxy for checkout start
        })
        
    df = pd.DataFrame(data)
    
    # Save to CSV
    try:
        df.to_csv("patient_flow_data.csv", index=False)
        print(f"Successfully generated 'patient_flow_data.csv' with {len(df)} patient records.")
    except Exception as e:
        print(f"Error saving file: {e}")
        
    print("--- Data Generation Complete ---")

if __name__ == "__main__":
    generate_data()