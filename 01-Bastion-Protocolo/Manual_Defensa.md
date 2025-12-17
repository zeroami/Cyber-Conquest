```markdown
# 🛡️ Bastión y Protocolo: Manual de Defensa de Red

> [!IMPORTANT]
> **"La seguridad no es un producto que se compra, es un proceso de capas que se diseña y se mantiene."**  
> Este manual es una guía integral para construir una red segura. Está diseñado para ser accesible: partimos de conceptos básicos y escalamos hasta la implementación técnica profesional.

---

## 🗺️ Mapa de Ruta del Manual
1. **Perímetro:** Arquitectura de Firewalls y filtrado de tráfico.  
2. **Conectividad:** Túneles VPN para comunicación segura.  
3. **Protocolos:** Seguridad en IPv6 y redes locales.  
4. **Fortificación (Hardening):** Configuración del Kernel Linux.  
5. **Integridad:** Inmutabilidad de archivos y logs.  
6. **Detección:** Honeyports y auditoría anti-evasión.

---

## 1. Arquitectura de Firewalls: El Guardián de la Puerta
Un firewall decide quién entra y sale de tu red. Es tu primera línea de defensa contra intrusiones.

### 🔍 Tipos de Filtrado de Paquetes
Existen tres niveles de "inteligencia" en un firewall:

| Nivel | Tipo | Cómo funciona | Analogía |
| :--- | :--- | :--- | :--- |
| **Básico** | **Stateless** | Mira paquetes de forma aislada (IP/Puerto). | Un portero que solo mira el DNI. |
| **Medio** | **Stateful** | Recuerda el contexto de la conversación. | Un portero que sabe si tú habías salido antes. |
| **Avanzado** | **DPI (Capa 7)** | Inspecciona el mensaje real dentro del paquete. | Un portero que revisa qué llevas dentro de la maleta. |

> [!TIP]
> **Recomendación:** Para empezar, domina los firewalls **Stateful** (como `iptables` o `ufw`). Son el estándar de oro en seguridad y rendimiento.

---

## 2. Redes Privadas Virtuales (VPN): El Túnel Invisible
Una VPN crea un "pasadizo secreto" y cifrado a través de Internet (una red pública e insegura).

### 🛡️ Beneficios Estratégicos
- **Ocultación de Servicios:** Al usar una VPN, puedes cerrar los puertos de tus servidores (SSH, bases de datos) al mundo exterior. Solo son visibles para quienes están "dentro" del túnel.  
- **Cifrado de Extremo a Extremo:** Protege tus datos de ser interceptados en redes Wi-Fi públicas o por proveedores de Internet.

### 🔑 Protocolos Principales
- **WireGuard:** El más moderno, rápido y fácil de configurar. Recomendado para nuevos proyectos.  
- **OpenVPN:** Muy versátil y compatible con casi cualquier dispositivo.  
- **IPsec:** Estándar corporativo para unir dos oficinas de forma permanente.

---

## 3. Seguridad en IPv6: El Nuevo Estándar
IPv6 no solo añade más direcciones, cambia cómo se hablan los dispositivos en tu red local.

### 🚨 El Peligro del Neighbor Discovery (NDP)
En IPv4 usábamos ARP; en IPv6 usamos **NDP**. El problema es que un atacante puede enviar "mensajes de redirección" falsos para que todo el tráfico pase por su equipo, realizando un ataque **Man-in-the-Middle (MITM)**.

### 🛠️ Configuración de Defensa
Para evitar que un atacante local secuestre tu tráfico, configura el kernel para ignorar estas órdenes:

```ini
# Desactivar aceptación de redirecciones ICMPv6
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
```

> 💡 **Consejo:** Si no usas IPv6, desactívalo completamente (`sysctl net.ipv6.conf.all.disable_ipv6=1`). Si lo usas, asegúralo.

---

## 4. Fortificación del Kernel (Hardening con Sysctl)
El *hardening* es el proceso de cerrar puertas innecesarias en el sistema operativo antes de que un ataque llegue a tus aplicaciones.

### 🔧 Configuración Maestra (`/etc/sysctl.conf`)
Copia estas líneas para protegerte contra ataques clásicos de red:

```ini
# 1. Mitigación de SYN Flood (Agotamiento de recursos)
net.ipv4.tcp_syncookies = 1

# 2. Protección contra IP Spoofing (Suplantación de identidad)
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# 3. Ignorar Redirecciones ICMP (Previene Man-in-the-Middle)
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0

# 4. Deshabilitar Source Routing (Evita rutas manipuladas)
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0

# 5. Protección contra ataques Smurf
net.ipv4.icmp_echo_ignore_broadcasts = 1
```

### 🔄 Aplicar los cambios
```bash
sudo sysctl -p
```

> ✅ **Práctica profesional:** Incluye esta configuración en tus plantillas de despliegue de servidores.

---

## 5. Inmutabilidad: Archivos "A Prueba de Balas"
Si un atacante entra como `root`, su primer paso es borrar los logs. Con el comando `chattr`, podemos impedirlo.

### 💎 Atributo Inmutable (`+i`)
Hace que un archivo **no se pueda borrar, renombrar ni editar**, ni siquiera por el administrador.

- **Uso:** Archivos que casi nunca cambian: `/etc/passwd`, `/etc/shadow`, `/etc/fstab`.
- **Comando:**
  ```bash
  sudo chattr +i /etc/passwd
  sudo chattr +i /etc/shadow
  ```

### 📝 Atributo Solo Anexión (`+a`)
Permite escribir datos nuevos al final, pero **prohíbe borrar o modificar** lo existente.

- **Uso:** Archivos de log. Un atacante podrá entrar, pero no podrá borrar el registro de su entrada.
- **Comando:**
  ```bash
  sudo chattr +a /var/log/auth.log
  sudo chattr +a /var/log/syslog
  ```

> ⚠️ **¡Cuidado!** Para modificar un archivo con estos atributos, primero debes quitarlos con `chattr -i` o `chattr -a`.

---

## 6. Defensa Activa: El Honeyport (Trampa)
Un Honeyport es un puerto falso que no ofrece ningún servicio real. Si alguien intenta conectar con él, sabemos con certeza que es un escaneo malicioso.

### 🪤 Script de Bloqueo Automatizado
Este script escucha en el puerto 23 (Telnet) y, si detecta una conexión, bloquea la IP del atacante en el firewall permanentemente.

```bash
#!/bin/bash
HONEY_PORT="23"
LOG_FILE="/var/log/honeyport.log"

echo "[*] Trampa activada en puerto $HONEY_PORT..."

while true; do
    # Captura la IP de quien intente conectar
    IP=$(nc -l -n -v -p "$HONEY_PORT" 2>&1 | grep "Connection from" | awk '{print $3}' | cut -d':' -f1)
    
    if [[ "$IP" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "[!] Ataque desde $IP. Bloqueando..." | tee -a "$LOG_FILE"
        iptables -I INPUT -s "$IP" -j DROP
    fi
done
```

### ▶️ Cómo usarlo
1. Guarda el script como `/opt/honeyport.sh`
2. Dale permisos: `chmod +x /opt/honeyport.sh`
3. Ejecútalo en segundo plano: `nohup /opt/honeyport.sh > /dev/null 2>&1 &`

> 🔍 **Ampliación:** Puedes usar varios puertos (21, 23, 1433, 3389) y enviar alertas por correo o a un SIEM.

---

## 7. Anti-Evasión: Auditoría de Comandos
Evita que un intruso limpie sus huellas borrando el historial de la terminal (`~/.bash_history`).

### 📜 Histórico a Prueba de Manipulación
- **Historial de solo anexión:**
  ```bash
  sudo chattr +a ~/.bash_history
  ```
- **Mejorar el historial global** (añade a `/etc/bash.bashrc`):
  ```bash
  HISTSIZE=50000
  HISTFILESIZE=50000
  HISTTIMEFORMAT="%F %T "
  HISTCONTROL=ignoreboth:erasedups
  ```

### 📡 Registro Remoto (Syslog)
Envía tus logs a otro servidor en tiempo real. Si el atacante borra tu máquina, las pruebas estarán a salvo en el servidor remoto.

En `/etc/rsyslog.conf`:
```conf
# Enviar logs de autenticación a un servidor remoto (TCP)
authpriv.* @@IP_SERVIDOR_REMOTO:514
```

Luego reinicia el servicio:
```bash
sudo systemctl restart rsyslog
```

> 🏢 **Mejor práctica:** Usa un servidor de logs dedicado, aislado y con acceso restringido.

---

## 🏁 Conclusión
La defensa efectiva no depende de una herramienta mágica, sino de la suma de **capas coordinadas**:

- ✅ Un kernel configurado contra ataques de red.  
- ✅ Archivos críticos e inmutables, incluso para `root`.  
- ✅ Un firewall que entienda el contexto de las conexiones.  
- ✅ Una monitorización activa (honeyports) y pasiva (syslog remoto).  
- ✅ Auditoría persistente que el atacante no pueda borrar.

**¡La seguridad es un proceso, no un destino!** Construye tu bastión, capa por capa.
```
