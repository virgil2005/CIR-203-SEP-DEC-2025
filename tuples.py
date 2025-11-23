patient =("John Doe",45,"120/80",72)
print("Patient:",patient)
print("Age:",patient[1],"Heart Rate:",patient[3])
print("Tuples are suitable because they are immutable,ensuring data safety.")
patient_list=list(patient)
patient_list[3]=80
patient=tuple(patient_list)
print("updated patient:",patient)
patients=(
    ("John Doe",45,"120/80",80),
    ("Jane Smith",30,"110/70",75),
    ("Mike Lee",55,"140/90",85),
    ("Sara Kim",40,"115/75",70),
    ("Paul Wang",60,"135/88",78)
    )
names=[p[0] for p in patients
    ]
print("Patient Names:",names)