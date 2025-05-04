# Symptom rules (simplified)
symptom_db = [
    {"keywords": ["fever", "headache", "sore throat"], "department": "General Medicine", "condition": "Viral Infection"},
    {"keywords": ["cough", "chest pain"], "department": "Pulmonology", "condition": "Bronchitis"},
    {"keywords": ["rash", "itching"], "department": "Dermatology", "condition": "Eczema"},
    {"keywords": ["abdominal pain", "nausea"], "department": "Gastroenterology", "condition": "Ulcer"},
    {"keywords": ["shortness of breath", "fatigue"], "department": "Cardiology", "condition": "Heart Problem"},
    {"keywords": ["joint pain", "swelling"], "department": "Orthopedics", "condition": "Arthritis"},
]

# Hospital info
hospitals = {
    "City Hospital": {"departments": ["General Medicine", "Cardiology"], "contact": "+91 12345 67890"},
    "Pulse Clinic": {"departments": ["Pulmonology"], "contact": "+91 23456 78901"},
    "Skin Care": {"departments": ["Dermatology"], "contact": "+91 34567 89012"},
    "Gastro Hub": {"departments": ["Gastroenterology"], "contact": "+91 45678 90123"},
}

# Predict department and condition
def predict(symptoms):
    symptoms = symptoms.lower()
    for rule in symptom_db:
        for word in rule["keywords"]:
            if word in symptoms:
                return rule["department"], rule["condition"]
    return "General Medicine", "General Checkup"

# Recommend hospitals based on department
def get_hospitals(department):
    return [f"{name} - {info['contact']}" for name, info in hospitals.items() if department in info["departments"]]

# Main program
def main():
    print("==== AI Expert System ====\n")

    name = input("Patient Name: ")
    age = input("Age: ")
    symptoms = input("Describe symptoms: ")

    dept, cond = predict(symptoms)
    nearby = get_hospitals(dept)

    print("\n--- Diagnosis Report ---")
    print(f"Name      : {name}")
    print(f"Age       : {age}")
    print(f"Symptoms  : {symptoms}")
    print(f"Condition : {cond}")
    print(f"Department: {dept}")

    print("\n--- Recommended Hospitals ---")
    if nearby:
        for hospital in nearby:
            print(hospital)
    else:
        print("No hospital available for this department.")

if __name__ == "__main__":
    main()
