from consultorio import ColaDePacientes
consultorio_medico = ColaDePacientes()

while True:
    print("-------Menu-------" "\n1.Ingresar paciente" "\n2.LLamar paciente" "\n3.Salir" "\n------------------")
    option = int(input())

    if option == 1:
        print("Ingrese nombre y apellido del paciente:")
        patient = str(input())
        consultorio_medico.new_patient(patient)

    elif option == 2:
        consultorio_medico.next_patient()

    elif option == 3:
        break

    elif option == 4:
        consultorio_medico.patient_queue()