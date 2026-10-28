# 2. Use Cases (P2 & P3)

## Use Case: Book Appointment
- **Actors:** Patient, Doctor
- **Preconditions:** Patient is logged into the system and has fewer than N = 3 upcoming appointments.
- **Main Flow:**
  1. Patient searches for available doctors by specialty.
  2. System displays available time slots for the selected doctor.
  3. Patient selects a time slot and confirms the booking.
  4. System verifies that the patient's upcoming appointments count is less than N = 3.
  5. System saves the appointment and displays a confirmation message to the patient.
- **Alternative Flow (Limit Exceeded):**
  4a. If the patient already has 3 upcoming appointments:
      1. System detects that the limit N = 3 has been reached.
      2. System displays an error message stating the maximum appointment limit has been reached.
      3. System prompts the patient to cancel an existing appointment before booking a new one.

---

## Use Case Diagram (Mermaid)
```mermaid
actor Patient
actor Doctor

rectangle "Clinic Appointment System" {
  Patient --> (Register / Login)
  Patient --> (Search & Book Appointment)
  Patient --> (Cancel Appointment)
  
  Doctor --> (View Schedule)
  Doctor --> (Cancel Appointment)
}