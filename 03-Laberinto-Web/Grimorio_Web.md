# 🏛️ El Grimorio Web: SQL Injection & XSS

> "Las aplicaciones web son las puertas de la ciudad; si no validas quién entra, dejas pasar al enemigo."

Este módulo cubre dos de las vulnerabilidades más críticas del OWASP Top 10.

## 1. Inyección SQL Ciega (Blind SQL Injection)
A diferencia de la inyección normal, aquí el servidor no muestra errores. El atacante debe "jugar a las adivinanzas".

* **Definición:** Técnica usada cuando la aplicación no da retroalimentación directa (no ves el error en pantalla).
* **Mecánica del Ataque:** El atacante extrae información haciendo preguntas de Verdadero/Falso a la base de datos y observando:
    * **Retrasos de tiempo:** (Ej: "Si el usuario es admin, espera 10 segundos").
    * **Cambios sutiles:** Diferencias en la respuesta HTML o DNS.

## 2. Cross-Site Scripting (XSS)
El ataque contra los usuarios de la aplicación.

* **El fallo:** Ocurre cuando una aplicación toma datos de entrada (input) y los devuelve al navegador sin validarlos ni limpiarlos.
* **El impacto:** Permite al atacante ejecutar scripts maliciosos (Javascript) en el navegador de la víctima para robar cookies de sesión o redirigir a sitios falsos.

## 3. Comparativa de Ataques
| Ataque | Objetivo Principal | Mecanismo |
| :--- | :--- | :--- |
| **SQL Injection** | Base de Datos (Backend) | Manipular consultas SQL |
| **XSS** | Usuario (Frontend) | Ejecutar scripts en el navegador |
| **Buffer Overflow** | Memoria del Sistema | Sobrescribir la pila/stack |
