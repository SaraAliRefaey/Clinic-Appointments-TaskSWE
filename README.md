# Clinic Appointments System

## Team Details
| Student ID | Full name | Assigned task | Branch | PR link |
|---|---|---|---|---|
| 20242333 | Mariem Mostafa Ahmed | Use Cases | mariam-usecases | https://github.com/SaraAliRefaey/Clinic-Appointments-TaskSWE/pull/6 |
| 20242148 | Mariem Mostafa Ahmed | Requirements | Mariem-Mostafa-patch-2 | https://github.com/SaraAliRefaey/Clinic-Appointments-TaskSWE/pull/5 |
| 20242333 | Mariem Mostafa Ahmed | Class Diagram | mariem-class-diagram | https://github.com/SaraAliRefaey/Clinic-Appointments-TaskSWE/pull/7 |
| 20242148 | Sara Ali Refaey | Sequence Diagram | sequence_diagram | https://github.com/SaraAliRefaey/Clinic-Appointments-TaskSWE/pull/8 |
| 20242333 | Sara Ali Refaey | Implementation | implementation | https://github.com/SaraAliRefaey/Clinic-Appointments-TaskSWE/pull/9 |

## System Parameters
- N (max upcoming appointments per patient): 3

Conflict Drill: Sara Ali Refaey, Mariem Mostafa Ahmed

## How to run
python main.py

## Non-functional requirements (design notes, not implemented)
- R5: only authenticated, authorized staff roles can read medical data; patients see only their own data; keep medical data separate from the booking data.
- R6: keep availability in a simple indexed structure (or cache the next days' slots) so the list is returned in under 2 seconds.
- R7: mobile-first responsive layout (single column, large tap targets); a console app is acceptable for this assignment.
