def diagnostico():
    print("Sistema Experto: Diagnóstico de Fallas en Automóvil\n")
    
    arranca = input("¿El auto arranca? (si/no): ").strip().lower()
    
    if arranca == "no":
        luces = input("¿Las luces del tablero están encendidas? (si/no): ").strip().lower()
        if luces == "no":
            print("Posible causa: batería descargada.")
        elif luces == "si":
            print("Posible causa: fallo en el motor de arranque.")
        else:
            print("Respuesta no reconocida.")
        return

    apaga = input("¿El auto se apaga al acelerar? (si/no): ").strip().lower()
    if apaga == "si":
        print("Posible causa: problema en el suministro de combustible.")
        return

    humo = input("¿El auto tiene humo por el escape? (ninguno/negro/blanco): ").strip().lower()
    if humo == "negro":
        print("Posible causa: mezcla rica de combustible.")
    elif humo == "blanco":
        print("Posible causa: falla en la junta de culata.")
    elif humo == "ninguno":
        print("No se detecta una falla común según los síntomas.")
    else:
        print("Respuesta no reconocida.")

if __name__ == "__main__":
    diagnostico()