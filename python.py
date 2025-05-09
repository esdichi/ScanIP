import subprocess
import platform

def validar_ip(red):
    partes = red.split('.')
    if len(partes) != 3:
        return False
    for parte in partes:
        if not parte.isdigit() or int(parte) < 0 or int(parte) > 255:
            return False
    return True

def obtener_rango():
    while True:
        entrada = input("\nIngrese el rango de red (ej: 192.168.1): ").strip().rstrip('.')
        if validar_ip(entrada):
            return entrada
        print("⚠️ Formato inválido. Debe ser: XXX.XXX.XXX (cada XXX entre 0-255)")

def escanear_red(red):
    sistema = platform.system().lower()
    print(f"\n🔍 Escaneando {red}.1-254...\n")
    
    for i in range(1, 255):
        ip = f"{red}.{i}"
        
        try:
            parametros = ['-n', '1', '-w', '150', ip] if sistema == "windows" else ['-c', '1', '-W', '0.2', ip]
            
            resultado = subprocess.run(
                ['ping'] + parametros,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=0.3
            )
            
            if resultado.returncode == 0:
                print(f"✅ {ip.ljust(15)} - Dispositivo activo")
                
        except subprocess.TimeoutExpired:
            continue

if __name__ == "__main__":
    print("""
    *************************************
    *  Escáner de Red de Esdichi        *
    *************************************
    """)
    
    red = obtener_rango()
    escanear_red(red)
    
    print("\n🎯 Escaneo completado. Dispositivos encontrados mostrados.")
