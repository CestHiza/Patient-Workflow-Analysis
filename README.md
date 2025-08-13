# Patient Wait Time & Workflow Analysis

This project is a hypothesis-driven analysis of clinical patient flow data, designed to identify operational bottlenecks and support a process re-design initiative. The entire analysis is conducted using Python for data generation and Microsoft Excel for data manipulation, interpretation, and visualization, culminating in a persuasive, data-driven proposal for change management.

This project directly showcases the skills required for a **Healthcare Data Analyst**, including data analysis, process optimization, and stakeholder communication.

## Project Workflow

1.  **Hypothesis Formulation:** The project begins with a clear, testable hypothesis: "The longest wait times for patients occur between seeing the nurse and seeing the doctor."
2.  **Data Collection:** A Python script (`generate_patient_flow_data.py`) generates a synthetic dataset (`patient_flow_data.csv`) that simulates patient timestamps at various stages of a clinic visit (Check-in, Nurse Triage, Doctor Consult, Check-out).
3.  **Data Manipulation & Interpretation (Excel):**
    * The raw data is imported into Excel.
    * **Excel formulas** are used to calculate the duration of each wait time and the total visit time in minutes for every patient.
    * Summary statistics (e.g., `AVERAGE`) are used to analyze the results and test the initial hypothesis.
4.  **Presentation of Findings (Excel Dashboard & Proposal):**
    * A simple dashboard is created in Excel using **PivotTables and PivotCharts** to visually compare the different wait time stages.
    * A **persuasive proposal** is written directly within the dashboard. This report summarizes the data-driven findings and recommends a specific process re-design initiative to address the identified bottleneck.

## Skills Demonstrated

* **Hypothesis-Driven Analysis:** The project follows a structured analytical approach, starting with a hypothesis and using data to prove or disprove it.
* **Data Collection, Manipulation & Interpretation:** Demonstrates the ability to work with complex data, calculate new metrics, and interpret the results to find patterns and opportunities.
* **Process Re-design & Change Management:** The analysis directly supports a process re-design initiative, showcasing an understanding of how data can be used to improve operational efficiency.
* **Dissemination of Findings:** The final output is a clear, structured, and persuasive proposal tailored for stakeholders, demonstrating strong written communication skills.
* **Proficiency with Excel:** The entire analysis, from calculation to visualization, is performed using advanced Excel capabilities, a key skill mentioned in the job description.

## How to Run This Project

### Prerequisites

* Python 3.9+
* Microsoft Excel (2016 or newer / Microsoft 365)

### Steps

1.  **Generate the Source Data:**
    * (Optional) Set up a Python virtual environment and install pandas: `pip install pandas`.
    * Run the data generation script from your terminal:
        ```bash
        python generate_patient_flow_data.py
        ```
2.  **Conduct the Analysis in Excel:**
    * Open the generated `patient_flow_data.csv` file in Microsoft Excel (or import it into a new workbook).
    * Follow the detailed steps in the **"Excel Analysis Guide for Patient Flow Data"** to calculate wait times, create the summary table, and build the dashboard.
3.  **Review the Proposal:**
    * Read the **"Patient Flow Analysis: Proposal for Change Management"** to see the final, persuasive report based on the data.