# 🔐 Cámara Enigma: Fundamentos de Criptografía

> "En la era digital, la criptografía es lo que separa tus secretos del dominio público."

Este módulo explora las matemáticas que protegen la confidencialidad y la integridad de la información.

## 1. Tipos de Cifrado
No todos los candados funcionan igual. Existen dos familias principales:

### A. Cifrado Simétrico (La Llave Única)
* **Concepto:** Se usa la **misma clave** tanto para cifrar como para descifrar.
* **Ejemplo:** AES (Advanced Encryption Standard).
* **Problema:** ¿Cómo le paso la clave a mi amigo de forma segura sin que nadie la intercepte?
* **Uso:** Cifrado de discos duros, archivos locales, WiFi (WPA2).

### B. Cifrado Asimétrico (La Doble Llave)
* **Concepto:** Se usa un par de claves matemáticas.
    * **Clave Pública:** Se comparte con todo el mundo. Sirve para **cifrar**.
    * **Clave Privada:** Se guarda bajo siete llaves. Sirve para **descifrar**.
* **Ejemplo:** RSA, ECC (Curva Elíptica).
* **Uso:** HTTPS (el candado del navegador), Bitcoin, firmas digitales.



## 2. Hashing vs. Cifrado
Es un error común confundirlos.
* **Cifrado:** Es reversible. Si tienes la clave, recuperas el mensaje original.
* **Hashing:** Es de **una sola vía** (irreversible). Convierte cualquier dato en una cadena alfanumérica de longitud fija (digest).
    * *Uso:* Almacenar contraseñas en bases de datos. Si un hacker roba la base de datos, solo ve hashes (ej. `5e884898da...`), no las contraseñas reales ("123456").

## 3. Esteganografía
El arte de ocultar la existencia del mensaje. A diferencia del cifrado, que hace el mensaje ilegible, la esteganografía esconde el mensaje dentro de una imagen, audio o video para que nadie sospeche que hay información secreta.

## 4. Laboratorio: El Cifrado César (Python)
Uno de los métodos más antiguos (usado por Julio César). Desplaza cada letra del alfabeto un número fijo de posiciones.

```python
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    # Recorremos cada caracter del texto
    for char in texto:
        if char.isalpha():
            # Definir si es mayúscula o minúscula para mantener el caso
            ascii_offset = 65 if char.isupper() else 97
            
            # Fórmula matemática del desplazamiento
            codigo = (ord(char) - ascii_offset + desplazamiento) % 26 + ascii_offset
            resultado += chr(codigo)
        else:
            # Si no es letra (espacio, número), lo dejamos igual
            resultado += char
    return resultado

# Prueba
mensaje = "Zeroami te saluda"
secreto = cifrado_cesar(mensaje, 3)
print(f"Original: {mensaje}")
print(f"Cifrado:  {secreto}") # Salida: KROD PXQGR
