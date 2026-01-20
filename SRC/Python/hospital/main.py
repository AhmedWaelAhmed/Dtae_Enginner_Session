# main.py
from hospital import Hospital
from department import Department
from staff import Staff
from patiant import Patient

def main():
    # 1. Create Hospital (with unique ID)
    my_hospital = Hospital(name="City General", location="New York", hospital_id="H-101")

    # 2. Create Departments
    er = Department(name="Emergency Room")
    cardio = Department(name="Cardiology")

    # 3. Connect Departments to Hospital
    my_hospital.add_department(er)
    my_hospital.add_department(cardio)

    # 4. Create People
    nurse = Staff(name="Alice", age=30, position="Nurse")
    doctor = Staff(name="Dr. Bob", age=50, position="Surgeon")
    patient = Patient(name="John Doe", age=25, medical_record="Flu")

    # 5. Connect People to Department
    er.add_staff(nurse)
    er.add_staff(doctor)
    er.add_patient(patient)

    # 6. Verify Output
    print("\n--- Verification ---")
    print(nurse.view_info())       # Calls Staff.view_info()
    print(patient.view_record())   # Calls Patient.view_record()

if __name__ == "__main__":
    main()