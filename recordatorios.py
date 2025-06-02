recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

def insertar_evento(lista_eventos, nuevo_evento):
    fecha_nueva = nuevo_evento[0]
    hora_nueva = nuevo_evento[1]

    for i, evento_existente in enumerate(lista_eventos):
        fecha_existente = evento_existente[0]
        hora_existente = evento_existente[1]

        if fecha_nueva < fecha_existente or (fecha_nueva == fecha_existente and hora_nueva <= hora_existente):
            lista_eventos.insert(i, nuevo_evento)
            return
    lista_eventos.append(nuevo_evento)

evento_inicio_anio = ['2021-02-02', '06:00', 'Empezar el año']
insertar_evento(recordatorios, evento_inicio_anio)

for evento in recordatorios:
    if evento[0] == '2021-07-15' and evento[2] == 'No hacer nada es feriado':
        evento[0] = '2021-07-16'
        break

recordatorios = [evento for evento in recordatorios if not (evento[0] == '2021-05-01' and evento[2] == 'No trabajar')]

cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad']
cena_anio_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']

insertar_evento(recordatorios, cena_navidad)
insertar_evento(recordatorios, cena_anio_nuevo)

for i, recordatorio in enumerate(recordatorios):
    # Imprime la representación de la sub-lista
    # La coma al final indica que hay más elementos en la lista principal, excepto el último
    print(f' {recordatorio}{"," if i < len(recordatorios) - 1 else ""}')

