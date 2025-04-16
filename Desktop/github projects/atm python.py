from colorama import init, Fore, Style

init(autoreset=True)  # Para que no se mantenga el color después de cada print

clave_correcta = "1245"
saldo = 1000000
intentos = 0
max_intentos = 3

print(Fore.CYAN + Style.BRIGHT + "🟡 BIENVENIDO AL CAJERO #2 DE BANCOLOMBIA 🟡")

while intentos < max_intentos:
    password = input(Fore.WHITE + "Ingrese su clave de 4 dígitos: ")
    
    if password == clave_correcta:
        print(Fore.GREEN + "✅ CLAVE CORRECTA. BIENVENIDO.\n")
        
        while True:
            print(Fore.CYAN + "\n--- MENÚ PRINCIPAL ---")
            print("1. Ver saldo")
            print("2. Retirar dinero")
            print("3. Transferir dinero")
            print("4. Cambiar clave")
            print("5. Salir")
            
            opcion = input(Fore.YELLOW + "Seleccione una opción (1-5): ")

            if opcion == "1":
                print(Fore.GREEN + f"💰 Su saldo actual es: ${saldo:,}")
            
            elif opcion == "2":
                retiro = int(input(Fore.WHITE + "Ingrese la cantidad a retirar: "))
                if retiro <= saldo:
                    saldo -= retiro
                    print(Fore.GREEN + f"✅ Retiro exitoso. Nuevo saldo: ${saldo:,}")
                else:
                    print(Fore.RED + "❌ Fondos insuficientes.")
            
            elif opcion == "3":
                cuenta = input(Fore.WHITE + "Ingrese número de cuenta destino: ")
                monto = int(input("Ingrese el monto a transferir: "))
                if monto <= saldo:
                    saldo -= monto
                    print(Fore.GREEN + f"✅ Transferencia de ${monto:,} a la cuenta {cuenta}.")
                else:
                    print(Fore.RED + "❌ Fondos insuficientes.")
            
            elif opcion == "4":
                nueva_clave = input(Fore.WHITE + "Ingrese su nueva clave de 4 dígitos: ")
                if len(nueva_clave) == 4 and nueva_clave.isdigit():
                    clave_correcta = nueva_clave
                    print(Fore.GREEN + "🔐 Clave actualizada con éxito.")
                else:
                    print(Fore.RED + "⚠️ Clave inválida. Debe tener 4 dígitos.")
            
            elif opcion == "5":
                print(Fore.CYAN + "👋 Gracias por usar nuestro cajero. ¡Hasta pronto!")
                break
            
            else:
                print(Fore.RED + "⚠️ Opción no válida. Intente de nuevo.")
        break

    else:
        intentos += 1
        intentos_restantes = max_intentos - intentos
        if intentos_restantes > 0:
            print(Fore.RED + f"❌ CLAVE INVÁLIDA. LE QUEDAN {intentos_restantes} INTENTO(S)\n")
        else:
            print(Fore.RED + "🚫 DEMASIADOS INTENTOS. TARJETA BLOQUEADA.")
