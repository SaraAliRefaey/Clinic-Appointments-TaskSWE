# 3. Candidate Classes (P4)

| Class | Evidence | Explicit / Inferred / Rejected | Why |
|---|---|---|---|
| Patient | R1, R2, R4 | Explicit | The word is in the requirements |
| Doctor | R1, R3 | Explicit | The word is in the requirements |
| Appointment | R2, R3, R4 | Explicit | R2 says "book an appointment" |
| TimeSlot | R1, R2 | Explicit | R2 says "available time slot" |
| AppointmentStatus | R3, R4 | Inferred | Never named, but accept/decline and the limit rule (Pending + Accepted) need a status |
| MedicalRecord, Staff | R5 | Rejected | R5 is non-functional and not implemented |
| Payment, Notification | none | Rejected | No requirement asks for them |