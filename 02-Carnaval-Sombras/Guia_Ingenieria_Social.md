
# 🎭 Manual de Ingeniería Social y Seguridad Física (Master Class)

> [!IMPORTANT]
> **"El amateur ataca los servidores; el profesional ataca a las personas."**
> La tecnología se puede parchear; la psicología humana, no. Este manual es la guía definitiva sobre cómo los atacantes manipulan la mente ("Human Hacking"), eluden controles biométricos y burlan las barreras físicas.

---

## 1. Fase de Reconocimiento: Inteligencia Profunda (OSINT)

Antes de interactuar con el objetivo, el atacante debe conocerlo mejor que él mismo. El 80% del éxito de un ataque reside en esta fase pasiva: saber quién es quién, qué software usan y cuándo toman café.

### 🕵️ 1.1. Inteligencia de Fuentes Abiertas (OSINT)

No es magia, es la correlación de datos públicos dispersos.

* **Google Dorks (Hacking con buscadores):**
El uso de operadores avanzados para encontrar lo que la empresa "olvidó" ocultar.
* `site:trello.com "password"`: Busca tableros de gestión de proyectos públicos que contienen claves.
* `site:pastebin.com "empresa.com"`: Busca código fuente o configuraciones filtradas por desarrolladores descuidados.
* `filetype:pdf "manual de empleado"`: Encuentra la guía de bienvenida, revelando la estructura interna y los teléfonos de soporte.


* **SOCMINT (Social Media Intelligence):**
* **El peligro de LinkedIn:** Es el menú del atacante. Si un empleado publica *"Feliz de certificarme en Firewall Palo Alto"*, le está diciendo al hacker exactamente qué vulnerabilidad buscar en el perímetro.
* **Análisis de Fotos (Metadatos):** Una foto de un "cumpleaños en la oficina" subida a Instagram puede revelar en el fondo:
* Tipo de tarjetas de identificación (para clonarlas).
* Antivirus utilizado (icono en la pantalla).
* Post-its con contraseñas pegados al monitor.




* **Infraestructura (Shodan & Maltego):**
* **Shodan:** El "Google de los dispositivos". Permite encontrar cámaras de seguridad de la empresa que no tienen contraseña o impresoras abiertas a internet.



---

## 2. Pretexting: El Arte del Disfraz

El *Pretexting* es la creación de un escenario inventado para obligar a la víctima a entregar información. No es una mentira simple; es una actuación respaldada por datos.

### 🎭 2.1. Anatomía de un Ataque de Vishing (Voz)

> **Escenario Real: "El Técnico Estresado"**
> 1. **Spoofing:** El atacante falsifica su número para que en la pantalla del teléfono aparezca "Soporte TI Interno".
> 2. **Audio de Fondo:** Reproduce un sonido de fondo de centro de datos (ventiladores ruidosos) para dar contexto.
> 3. **El Gancho:** *"Hola María (nombre real), soy Carlos de Redes. Estamos migrando el servidor de correo y tu cuenta está bloqueando el proceso. Tengo al Director (nombre real) aquí al lado esperando para enviar un informe urgente. Necesito que me leas el código SMS que te acaba de llegar para no tener que borrar tu cuenta."*
> 4. **Resultado:** La víctima, bajo presión de autoridad y ruido técnico, entrega el código de doble factor (2FA).
> 
> 

---

## 3. Seguridad Física: Rompiendo el Perímetro

Las barreras digitales (Firewalls) son irrelevantes si el atacante logra acceso físico a la sala de servidores o conecta un dispositivo a la red interna.

### 🏃 3.1. Bypass de Acceso Humano (Tailgating)

* **El Truco del Café (Piggybacking):** El atacante espera en la puerta cargado con cuatro vasos de café y finge estar haciendo malabarismos para no tirarlos.
* *Reacción Humana:* El empleado autorizado, por pura cortesía ("Efecto Ben Franklin"), le abre la puerta y la sostiene. El atacante entra sonriendo y dando las gracias.


* **Defensa:** Implementación de torniquetes de suelo a techo y cultura de "No Tailgating" (cada persona debe pasar su tarjeta, sin excepciones).

### 💳 3.2. Clonación de Tarjetas (RFID/NFC)

Muchas empresas usan tarjetas antiguas (125kHz) que son inseguras por diseño.

* **La Herramienta (Proxmark3 / Flipper Zero):** Dispositivos del tamaño de un paquete de chicles que pueden leer y emular tarjetas.
* **El Ataque:**
1. El atacante se acerca a la víctima en un ascensor o en la cola del comedor.
2. Aproxima el dispositivo a 5-10 cm del bolsillo/bolso de la víctima.
3. En **0.5 segundos**, el dispositivo copia el ID de la tarjeta.
4. El atacante clona ese ID en una tarjeta en blanco y entra al edificio por la noche.


* **Mitigación:** Usar tarjetas cifradas **MIFARE DESFire EV2/EV3** que resisten la clonación simple.

### 🔌 3.3. USB Drop (El "Road Apple")

Dejar memorias USB infectadas con etiquetas tentadoras ("Nóminas 2024", "Fotos Fiesta", "Despidos").

* **Ejemplo Real (Stuxnet):** Así fue como se atacó la planta nuclear de Irán.
* **Mecanismo:** La curiosidad humana es irresistible. Al conectar el USB, un script (**Rubber Ducky**) se ejecuta en milisegundos, simulando ser un teclado que escribe comandos para abrir una puerta trasera en el PC.

---

## 4. Psicología del Engaño: Neuro-Hacking

El objetivo es desactivar el **"Sistema 2"** (pensamiento lento, lógico y crítico) y forzar a la víctima a usar el **"Sistema 3"** (rápido, emocional, automático).

### 🧠 Los 6 Principios de Influencia (Cialdini)

| Icono | Principio | Cómo funciona el ataque | Ejemplo de frase |
| --- | --- | --- | --- |
| 👮 | **Autoridad** | Obediencia ciega a la jerarquía o uniformes. | *"Soy el VP de Finanzas, haz la transferencia o estás despedido."* |
| ⏳ | **Urgencia** | El miedo a perder algo bloquea el análisis. | *"Tu cuenta se eliminará en 10 minutos si no verificas aquí."* |
| 🎁 | **Reciprocidad** | Deuda moral por un favor no pedido. | *"Ya te he arreglado el PC, ¿me podrías hacer un favor rápido?"* |
| 🐑 | **Validación Social** | Comportamiento de rebaño ("Si todos lo hacen..."). | *"El 95% de tu departamento ya ha rellenado la encuesta salarial."* |
| 🤝 | **Simpatía** | Confiamos en quien se parece a nosotros (hobbies). | *"¿Tú también eres del Real Madrid? Oye, pásame ese archivo..."* |
| 🔗 | **Compromiso** | Coherencia interna con lo dicho antes. | *"¿Te consideras una persona servicial? Entonces ayúdame con esto."* |

### 🧩 Sesgos Cognitivos Explotables

* **Efecto Halo:** Asumimos que una persona bien vestida (traje) o con uniforme (repartidor, técnico) es honesta y tiene derecho a estar ahí. Un chaleco reflectante y una escalera son el "pase universal" a casi cualquier edificio.
* **Difusión de la Responsabilidad:** *"No voy a detener a ese desconocido que entra; seguro que alguien más lo hace o seguridad ya lo ha visto."*

---

## 5. Defensa en Profundidad y Cultura

La tecnología es una herramienta; la seguridad real es un estado mental de la organización.

### 🛡️ 5.1. Contramedidas Físicas y Lógicas

* **Política de Escritorio Limpio:** Prohibición absoluta de dejar documentos sensibles o post-its con contraseñas a la vista. Las pantallas deben bloquearse automáticamente tras 2 minutos.
* **Destrucción Segura (Shredding):**
* *Mal:* Tirar documentos a la papelera (vulnerable al *Dumpster Diving* o robo de basura).
* *Bien:* Usar destructoras de **corte cruzado (P-4 o superior)** que convierten el papel en confeti imposible de reconstruir.



### 🧬 5.2. Procedimientos de Verificación

* **"Trust but Verify" (Confía pero verifica):** Si recibes una llamada inusual pidiendo datos o dinero, **cuelga**. Busca el número oficial de esa persona en el directorio interno y llama tú mismo.
* **Palabras de Coacción (Duress Code):** Establecer una palabra clave secreta (ej. "Tengo un problema con el *archivo rojo*") que un empleado pueda decir por teléfono para alertar a seguridad de que está siendo coaccionado sin que el atacante se dé cuenta.

### 🔐 5.3. Autenticación Multifactor (MFA)

La única defensa real contra el robo de credenciales.

* **Llaves Físicas (FIDO2/YubiKey):** Aunque el usuario sea engañado y entre en una web de phishing perfecta, el ataque falla porque el dominio web no coincide con la criptografía de la llave física.
* **Evitar SMS:** Los códigos por SMS son interceptables mediante ataques de *SIM Swapping*.

---

*Manual basado en estándares de PTES (Penetration Testing Execution Standard) y psicología conductual aplicada.*

