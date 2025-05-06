def evaluate_patient():
    print("=== Expert System: Patient Health Evaluation ===")
    
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    
    symptoms = ["Fever", "Cough", "Headache", "Fatigue", "Shortness of Breath", "Sore Throat"]
    ratings = [int(input(f"Rate {symptom} (1-5): ")) for symptom in symptoms]
    
    avg_score = sum(ratings) / len(ratings)

    if avg_score >= 4.5:
        health_status, recommendation = "Excellent", "No significant health concerns. Maintain a healthy lifestyle."
    elif avg_score >= 3.5:
        health_status, recommendation = "Good", "Minor symptoms. Rest and stay hydrated."
    elif avg_score >= 2.5:
        health_status, recommendation = "Moderate", "Symptoms suggest possible illness. Seek medical attention."
    else:
        health_status, recommendation = "Critical", "Severe symptoms detected. Immediate medical consultation required."

    print(f"\nPatient Name: {name}, Age: {age}")
    print(f"Health Status: {health_status}, Average Score: {avg_score:.2f}/5")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    evaluate_patient()
