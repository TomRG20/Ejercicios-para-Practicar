'''
Programa para generar claves y comparar el uso del módulo random y el módulo secrets

El módulo secrets se utiliza para generar números aleatorios criptográficamente fuertes, adecuados
para administrar datos como contraseñas, autenticación de usuarios, tokens de seguridad y secretos relacionados

En particular, secrets debe ser usado preferentemente frente a la generación de números pseudoaleatorios
empleando el módulo random, que está diseñado para el modelado y la simulación, no para la seguridad
o la criptografía

'''

import secrets

# Número aleatorios:






# token_hex ([nbytes])
# La cadena de caracteres tiene nbytes bytes aleatorios como parametro, cada byte convertido a dos dígitos hexadecimales
# Desde 2015 se cree que 32 bytes (256 bits) de aleatoriedad son considerados suficientes para mantenerse seguro de los
# ataques de fuerza bruta, pero con el tiempo iran aumentando.

claveSecretaH = secrets.token_hex()  #genera un token con 64 elementos alfanuméricos hexadecimal
print(f"La clave secreta es: {claveSecretaH}")

claveSecretaH = secrets.token_hex(16)  #genera un token con 32 elementos alfanuméricos hexadecimal
print(f"La clave secreta es: {claveSecretaH}")

claveSecretaH = secrets.token_hex(4)  #genera un token con 8 elementos alfanuméricos hexadecimal
print(f"La clave secreta es: {claveSecretaH}")

claveSecretaH = secrets.token_hex(64)  #genera un token con 128 elementos alfanuméricos hexadecimal
print(f"La clave secreta es: {claveSecretaH}")



