# Simple Exam Eligibility Checker
attendance = int(input("Enter attendance %: "))
has_medical_cause = input("Do you have a medical certificate? (yes/no): ").lower()

if attendance >= 75:
    print("Eligible.")
elif attendance >= 60 and has_medical_cause == "yes":
    print("Eligible due to medical reasons.")
else:
    print("Not Eligible.")
