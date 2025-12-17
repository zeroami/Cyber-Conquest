# 🛡️ Bastión y Protocolo: Manual de Defensa de Red (Nivel Avanzado)

> **"La seguridad no es un producto que se compra, es un proceso de capas que se diseña y se mantiene."**

Este manual es tu guía integral para construir una red altamente segura desde cero. Aunque el título diga "nivel avanzado", ¡no te preocupes! Está diseñado para que cualquier persona con conocimientos básicos de redes y Linux pueda entenderlo, aplicarlo y crecer. Cada sección incluye explicaciones claras, ejemplos prácticos y recomendaciones para implementar defensas reales en tu entorno.

---

## 1. Arquitectura de Firewalls y Filtrado  
### ¿Por qué importa el control del tráfico en una red?

Imagina que tu red es una casa. Un firewall es como la puerta de entrada: decide quién puede entrar y salir. Si no controlas lo que entra, cualquiera (incluyendo atacantes) podría acceder a tus sistemas internos. Por eso, el **filtrado de red** es la **primera línea de defensa** contra escaneos, intrusiones y ataques automatizados.

### Tipos de filtrado de paquetes

#### 🔹 **Filtrado Estático (Stateless)**  
- **¿Qué hace?** Mira cada paquete por separado, como si no supiera nada sobre los demás.
- **¿Cómo decide?** Solo revisa la *cabecera* del paquete: origen, destino, protocolo (TCP/UDP), y puertos.
- **Ventaja:** Es muy rápido, ideal para bloquear grandes volúmenes de tráfico malicioso.
- **Desventaja:** No entiende el *contexto*. Por ejemplo, si un paquete finge ser parte de una conexión legítima, podría pasar.
- **Ejemplo:** Bloquear todo el tráfico entrante al puerto 22 (SSH) desde una IP sospechosa.

#### 🔹 **Filtrado con Estado (Stateful)**  
- **¿Qué hace?** Sí entiende el contexto. Usa una **tabla de estado** (a menudo llamada `conntrack`) para recordar qué conexiones están activas.
- **¿Cómo decide?** Solo permite paquetes que pertenezcan a una conexión ya iniciada (o relacionada con ella).
- **Ventaja:** Mucho más seguro. Bloquea paquetes "huérfanos" o falsos que no forman parte de una conversación real.
- **Desventaja:** Consume más recursos, ya que debe seguir el estado de cada conexión.
- **Ejemplo:** Si tú inicias una conexión al puerto 80 de un servidor web, el firewall permitirá la respuesta de ese servidor. Pero si un atacante envía un paquete al puerto 80 sin que tú lo hayas solicitado, será descartado.

#### 🔹 **Inspección de Capa de Aplicación (DPI: Deep Packet Inspection)**  
- **¿Qué hace?** Va más allá de la cabecera: examina el **contenido real del mensaje** (la "carga útil" o *payload*), es decir, qué dice la aplicación.
- **¿Dónde opera?** En la **Capa 7** del modelo OSI (la capa de aplicación).
- **¿Por qué es clave?** Muchos ataques se disfrazan dentro de tráfico legítimo. Por ejemplo, un atacante podría enviar código malicioso dentro de una petición HTTP a un sitio web.
- **Ejemplo:** Detectar una inyección SQL en una petición a una API, incluso si el tráfico HTTP parece normal.

> 💡 **Consejo para principiantes:** Comienza con firewalls *stateful* (como `iptables` o `nftables`). Son el equilibrio perfecto entre seguridad y rendimiento. Usa DPI solo cuando necesites inspeccionar tráfico específico (por ejemplo, en un proxy de seguridad).

---

## 2. Redes Privadas Virtuales (VPN) y Túneles  
### ¿Cómo mantener seguro el tráfico entre ubicaciones?

Imagina que necesitas enviar una carta confidencial por correo público. Si no está sellada, cualquiera puede leerla. Una **VPN (Red Privada Virtual)** es como un sobre sellado y cifrado: protege tu información mientras viaja por Internet (una red pública).

### ¿Por qué usar una VPN en defensa?

#### 🔒 **Reducción de la Superficie de Ataque**  
- **Sin VPN:** Abres servicios como SSH, bases de datos o paneles de administración directamente a Internet → muchos atacantes intentarán explotarlos.
- **Con VPN:** Cierras esos servicios al tráfico público. Solo los usuarios dentro del túnel cifrado pueden acceder → menos exposición, menos riesgo.

#### 🔐 **Protocolos Comunes de VPN**  
- **IPsec (Internet Protocol Security):** Ideal para conexiones fijas entre servidores o redes corporativas. Muy robusto y estándar.
- **SSL/TLS (como en OpenVPN o WireGuard):** Perfecto para usuarios remotos (ej. empleados desde casa). Usa certificados y cifrado de extremo a extremo.
- **WireGuard:** Moderno, rápido y simple. Cada vez más popular por su diseño minimalista y alto rendimiento.

> ✅ **Buena práctica:** Nunca expongas bases de datos, SSH o APIs administrativas directamente a Internet. ¡Haz que pasen por una VPN!

---

## 3. Evolución de Protocolos: IPv6 y Seguridad Local  
### ¿Por qué IPv6 cambia las reglas del juego?

IPv6 no es solo "más direcciones". Es un protocolo completamente renovado que elimina problemas antiguos… pero introduce nuevos desafíos de seguridad.

#### 🔹 **Neighbor Discovery Protocol (NDP)**  
- **¿Qué reemplaza?** El viejo **ARP** (Address Resolution Protocol) de IPv4.
- **¿Qué hace?** Permite a los dispositivos descubrir routers, resolver direcciones MAC y configurar vecindad en la red local.
- **¿Cómo funciona?** Usa mensajes **ICMPv6**, como *Router Solicitation* o *Neighbor Advertisement*.

#### ⚠️ **Riesgos de Redirección ICMPv6**  
- Un atacante en la misma red local puede enviar un **mensaje de redirección falso**.
- Esto puede engañar a un host para que envíe su tráfico a través del atacante → **ataque MITM (Man-in-the-Middle)**.
- A diferencia de IPv4, en IPv6 esto es más común porque NDP no tiene autenticación por defecto.

#### 🛡️ **Cómo defenderte**  
1. **Configura el kernel para ignorar redirecciones ICMP:**
   ```ini
   net.ipv6.conf.all.accept_redirects = 0
   net.ipv6.conf.default.accept_redirects = 0
   ```
2. **Usa switches con soporte para *NDP Inspection* (similar a DHCP Snooping en IPv4).**
3. **Implementa *Secure Neighbor Discovery* (SEND)** si tu entorno lo soporta (aunque es raro en la práctica).

> 🌐 **Nota:** ¡No ignores IPv6! Muchos sistemas lo tienen activado por defecto. Si no lo usas, desactívalo. Si lo usas, asegúralo.

---

## 4. Fortificación del Kernel (Hardening con Sysctl)  
### ¿Qué es el "hardening"?

Es el proceso de **endurecer** tu sistema: aplicar configuraciones que lo hagan más resistente a ataques. En Linux, gran parte de esto se hace modificando parámetros del kernel mediante el comando `sysctl`.

Estos ajustes actúan **antes** de que el tráfico llegue a tus aplicaciones, bloqueando amenazas a nivel de red.

### 🔧 Configuración recomendada para `/etc/sysctl.conf`

```ini
# --- SEGURIDAD DE RED Y MITIGACIÓN DE ATAQUES ---

# 1. Mitigación de SYN Flood
# Los atacantes envían muchos paquetes SYN para agotar recursos.
# Las "cookies SYN" permiten validar la conexión sin reservar memoria.
net.ipv4.tcp_syncookies = 1

# 2. Protección contra IP Spoofing (Reverse Path Forwarding - RPF)
# Verifica que un paquete entrante venga por la ruta esperada.
# Si no, es probable que la IP de origen sea falsa.
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# 3. Ignorar Redirecciones ICMP (protege contra MITM local)
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0

# 4. Deshabilitar Source Routing
# Evita que un atacante especifique la ruta de su paquete (técnica antigua de evasión).
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0

# 5. Ignorar Echo Broadcast (protección contra Smurf Attack)
# En los 90s, los atacantes usaban broadcasts ICMP para saturar redes.
net.ipv4.icmp_echo_ignore_broadcasts = 1

# 6. No aceptar peticiones ICMP maliciosas en IPv6
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
```

### 🔄 Cómo aplicar estos cambios
```bash
sudo sysctl -p
```
Este comando recarga la configuración desde `/etc/sysctl.conf`.

> ✅ **Tip:** Haz una copia de seguridad antes de modificar `sysctl.conf`. Y prueba los cambios en un entorno no crítico primero.

---

## 5. Inmutabilidad y Forense del Sistema de Archivos  
### ¿Por qué proteger archivos críticos?

Si un atacante logra entrar en tu sistema, lo primero que hará es:
- Borrar sus rastros (logs).
- Modificar archivos como `/etc/passwd` para crear nuevos usuarios.
- Alterar la configuración del sistema.

Para evitarlo, usamos **atributos extendidos de Linux** con el comando `chattr`.

### 🔒 Atributo Inmutable (`+i`)  
- **¿Qué hace?** Hace que un archivo sea **totalmente inmodificable**, incluso para `root`.
- **Archivos a proteger:**
  - `/etc/passwd` → lista de usuarios
  - `/etc/shadow` → contraseñas cifradas
  - `/etc/fstab` → montaje de discos
  - `/etc/ssh/sshd_config` → configuración de SSH

```bash
sudo chattr +i /etc/passwd
sudo chattr +i /etc/shadow
```

> ⚠️ **¡Cuidado!** Si pones `+i` en un archivo que tu sistema necesita modificar (como un log), ¡se romperá! Solo úsalo en archivos estáticos.

### 📝 Atributo Solo Anexión (`+a`)  
- **¿Qué hace?** Permite **añadir** datos al final del archivo, pero **no borrar ni editar** lo existente.
- **Ideal para:** Archivos de registro (*logs*).

```bash
sudo chattr +a /var/log/syslog
sudo chattr +a /var/log/auth.log
```

Así, un atacante no podrá borrar sus intentos de inicio de sesión fallidos.

> 🔁 Para modificar un archivo con `+i` o `+a`, primero hay que quitar el atributo:  
> `sudo chattr -i archivo` o `sudo chattr -a archivo`

---

## 6. Defensa Activa: Script de Honeyport  
### ¿Qué es un "honeyport"?

Es una **trampa de seguridad**: un puerto que **no debería tener ningún servicio**, pero que escuchamos activamente. Si alguien se conecta, ¡es un atacante!

### 🪤 Ejemplo: Detectar escaneos de Telnet (puerto 23)

El siguiente script escucha en el puerto 23. Si alguien se conecta, bloquea su IP inmediatamente.

```bash
#!/bin/bash
# Honeyport: Detección y Bloqueo Automatizado

HONEY_PORT="23"
IPTABLES_CHAIN="HONEYPOT_DROP"

# Crear cadena de bloqueo si no existe
iptables -N "$IPTABLES_CHAIN" 2>/dev/null
iptables -A INPUT -p tcp --dport "$HONEY_PORT" -j "$IPTABLES_CHAIN" 2>/dev/null

echo "[*] Honeyport activo en puerto $HONEY_PORT."

while true; do
    # Escucha la conexión y extrae la IP del origen
    IP=$(nc -l -n -v -p "$HONEY_PORT" 2>&1 | grep "Connection from" | awk '{print $3}' | cut -d':' -f1)
    
    if [[ "$IP" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "[!] Ataque detectado desde: $IP. Bloqueando..."
        iptables -I "$IPTABLES_CHAIN" -s "$IP" -j DROP
        echo "ALL: $IP" >> /etc/hosts.deny
    fi
done
```

### 🛠️ Cómo usarlo
1. Guarda el script como `honeyport.sh`
2. Dale permisos: `chmod +x honeyport.sh`
3. Ejecútalo en segundo plano: `nohup ./honeyport.sh &`

> 💡 **Mejora avanzada:** Integra este script con `fail2ban` o un SIEM para alertas centralizadas.

---

## 7. Auditoría de Comandos y Persistencia (Anti-Evasión)  
### ¿Cómo evitar que un atacante borre su historial?

Muchos intrusos borran el historial de comandos (`~/.bash_history`) para ocultar sus acciones. Aquí evitamos eso.

### 🔐 Proteger el historial con inmutabilidad
```bash
sudo chattr +a /root/.bash_history
```
Ahora, cualquier comando que ejecute `root` se **añadirá** al historial, pero nadie podrá borrarlo.

### 📜 Mejorar el registro de comandos
Edita `/etc/bash.bashrc` (para todos los usuarios) o `~/.bashrc` (para uno solo) y añade:

```bash
# Aumenta el tamaño del historial
HISTSIZE=50000
HISTFILESIZE=50000

# Añade marca de tiempo: fecha y hora exacta
HISTTIMEFORMAT="%F %T "

# No guardar comandos duplicados ni que empiecen con espacio
HISTCONTROL=ignoreboth:erasedups
```

### 📡 Envío de logs a un servidor remoto (Syslog)
Incluso si el atacante borra los logs locales, tendrás una copia remota.

Edita `/etc/rsyslog.conf` y añade:
```conf
# Enviar logs de autenticación a un servidor seguro
authpriv.* @10.1.1.5:514
```
- `@` = UDP (rápido, pero no fiable)
- `@@` = TCP (más seguro y fiable)

Luego reinicia rsyslog:
```bash
sudo systemctl restart rsyslog
```

> 🏢 **Ideal en entornos reales:** Usa un **servidor SIEM** o un **servidor de logs dedicado** al que solo los administradores puedan acceder.

---

## ✅ Conclusión: La Defensa es un Proceso Continuo

No existe una "solución mágica". La seguridad real se construye con:
- **Capas** (firewall, kernel, archivos, logs),
- **Monitoreo** (honeyports, syslog remoto),
- **Auditoría** (historial inmutable, atributos de archivo),
- **Actualización constante**.
