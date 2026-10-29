from enum import Enum
from datetime import date, timedelta


# 1. Appointment Status
class AppointmentStatus(Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"


# 2. TimeSlot
class TimeSlot:
    def __init__(self, day, startTime):
        self.day = day
        self.startTime = startTime
        self.reserved = False

    def isAvailable(self):
        return not self.reserved

    def reserve(self):
        if self.isAvailable():
            self.reserved = True

    def release(self):
        self.reserved = False


# 3. Appointment
class Appointment:
    def __init__(self, patient, doctor, slot):
        self.patient = patient
        self.doctor = doctor
        self.slot = slot
        self.status = AppointmentStatus.PENDING

    def accept(self):
        self.status = AppointmentStatus.ACCEPTED

    def decline(self):
        self.status = AppointmentStatus.DECLINED
        self.slot.release()

    def isUpcoming(self):
        appointment_date = date.fromisoformat(self.slot.day)
        return appointment_date >= date.today()

    def countsTowardLimit(self):
        return (
            self.isUpcoming()
            and self.status in [
                AppointmentStatus.PENDING,
                AppointmentStatus.ACCEPTED
            ]
        )


# 4. Doctor
class Doctor:
    def __init__(self, doctorId, name, slots):
        self.doctorId = doctorId
        self.name = name
        self.slots = slots

    def getAvailableSlots(self):
        return [slot for slot in self.slots if slot.isAvailable()]

    def acceptAppointment(self, appointment):
        appointment.accept()
        print("Appointment accepted by doctor.")

    def declineAppointment(self, appointment):
        appointment.decline()
        print("Appointment declined by doctor.")
        print("Time slot is now available again.")


# 5. Patient
class Patient:
    N = 3

    def __init__(self, patientId, name):
        self.patientId = patientId
        self.name = name
        self.appointments = []

    def countUpcoming(self):
        return sum(
            1 for appointment in self.appointments
            if appointment.countsTowardLimit()
        )

    def viewAvailability(self, doctor):
        return doctor.getAvailableSlots()

    def bookAppointment(self, slot, doctor):

        # Check appointment limit
        if self.countUpcoming() >= self.N:
            print("LIMIT_REACHED: Maximum upcoming appointments reached.")
            return None

        # Check slot availability
        if not slot.isAvailable():
            print("SLOT_TAKEN: This time slot is not available.")
            return None

        # Create appointment
        slot.reserve()

        appointment = Appointment(self, doctor, slot)
        self.appointments.append(appointment)

        print("Booking successful!")
        print("Appointment status:", appointment.status.value)

        return appointment


# Main function
def main():

    print("===== Clinic Appointment System =====\n")

    # Create a future date
    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    # Create available time slots
    slots = [
        TimeSlot(tomorrow, "09:00"),
        TimeSlot(tomorrow, "10:00"),
        TimeSlot(tomorrow, "11:00"),
        TimeSlot(tomorrow, "12:00")
    ]

    # Create doctor and patient
    doctor = Doctor("D01", "Dr. Ahmed", slots)
    patient = Patient("P01", "Mariem")

    # Scenario 1: Successful Booking
    print("Scenario 1: Successful Booking")

    available = patient.viewAvailability(doctor)

    print("Available slots:", len(available))

    appointment1 = patient.bookAppointment(slots[0], doctor)

    print("Upcoming appointments:", patient.countUpcoming())
    print()

    # Scenario 2: Appointment Limit Reached
    print("Scenario 2: Appointment Limit Reached")

    patient.bookAppointment(slots[1], doctor)
    patient.bookAppointment(slots[2], doctor)

    print("Current appointments:", patient.countUpcoming())

    # Trying to book a fourth appointment
    appointment4 = patient.bookAppointment(slots[3], doctor)

    print("Fourth appointment:", appointment4)
    print()

    # Scenario 3: Doctor Declines Appointment
    print("Scenario 3: Doctor Declines Appointment")

    doctor.declineAppointment(appointment1)

    print("Current appointments:", patient.countUpcoming())

    # Rebook the released slot
    print("\nTrying to book the released slot again:")

    new_appointment = patient.bookAppointment(slots[0], doctor)

    print("New appointment status:", new_appointment.status.value)

    print("\n===== Program Finished =====")


if __name__ == "__main__":
    main()