class ColaDePacientes:
    def __init__(self):
        self.patients = []

    def new_patient(self, patient):
        self.patients.append(patient)
        print(self.patients)

    def patient_queue(self):
        print(self.patients)

    def next_patient(self):
        if len(self.patients) > 0:
            try:
                print("Llamar a " + self.patients.pop(0))
                if len(self.patients) > 0:
                    print("Paciente en espera: " + self.patients[0])
            except IndexError:
                print(ValueError("No hay pacientes"))
        else:
            print("No hay pacientes")