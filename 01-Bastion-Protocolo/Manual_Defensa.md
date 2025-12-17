# 🛡️ Manual de Defensa de Red (Network Defense)

Este documento resume los pilares de la seguridad en redes, basado en la bibliografía del curso.

## 1. Firewalls: La Primera Línea de Defensa
La seguridad perimetral depende de cómo filtramos el tráfico. Existen dos enfoques principales:

* **Filtrado Estático (Stateless):** Inspecciona los paquetes de forma aislada sin considerar su contexto histórico. Es más rápido pero menos seguro.
* **Filtrado Con Estado (Stateful):** Inspecciona los paquetes basándose en el contexto de la conexión (si es nueva, establecida, o relacionada). Es la norma actual para firewalls efectivos.

## 2. Redes Privadas Virtuales (VPN)
Para conectar sedes a través de redes inseguras (WAN/Internet), utilizamos VPNs.
* **Definición:** Tecnología que proporciona un túnel seguro y cifrado para las comunicaciones.
* **Ventajas:** Ofrece una base sólida de seguridad para WANs porque su configuración es simple, segura y de bajo costo operativo en comparación con líneas dedicadas.

## 3. La Evolución a IPv6
Con el agotamiento de IPv4, IPv6 introduce cambios en la gestión de la red local.
* **Neighbor Discovery (ND):** Protocolo clave en IPv6 que reemplaza funciones que en IPv4 realizaban ARP e ICMP por separado.
* **Funciones:** Descubrimiento de routers, resolución de direcciones y redirección de mensajes.


## 4. Fortificación del Kernel y Sistema
La fortificación avanzada de un sistema Linux requiere una comprensión profunda de los mecanismos del núcleo (kernel) y el sistema de archivos (filesystem), con el objetivo de elevar la resiliencia del entorno más allá de las protecciones de capa de aplicación estándar.

1. Inmutabilidad Forense: Protección de Logs y Configuraciones Críticas
El uso de atributos extendidos de archivo (chattr) permite establecer controles inmutables y de solo anexión a nivel de sistema de archivos (ext2, ext3, ext4), protegiendo la integridad de archivos críticos incluso frente al usuario root y amenazas avanzadas como el ransomware, que busca activamente borrar o cifrar logs para ocultar su rastro.
Uso de chattr +i (Inmutable)

El atributo i (inmutable) prohíbe cualquier modificación, eliminación o renombrado del archivo. Técnicamente, solo el superusuario puede establecer o borrar este atributo, pero su utilidad reside en que previene la eliminación accidental o maliciosa por parte de procesos de usuario comprometidos, incluso si operan con privilegios de root (si no están diseñados para llamar explícitamente a chattr -i).
Ejemplos de Código para Inmutabilidad de Configuración:

# Instalar chattr para proteger la tabla de particiones y las configuraciones esenciales.
# Solo el superusuario puede establecer o limpiar este atributo.
chattr +i /etc/fstab
chattr +i /etc/passwd
chattr +i /etc/group
chattr +i /etc/shadow
chattr +i /etc/sudoers
Uso de chattr +a (Solo Anexión)
El atributo a (append-only) es crucial para la integridad forense, ya que permite que los datos se escriban solo al final del archivo, impidiendo que el contenido existente sea modificado o eliminado. Este atributo es indispensable para los archivos de registro (log files).
Ejemplos de Código para Logs Inmutables:
# Aplicar el atributo 'a' a logs críticos para asegurar
# que los atacantes no puedan borrar entradas, solo añadir nuevas.
chattr +a /var/log/syslog
chattr +a /var/log/messages
chattr +a /var/log/secure
chattr +a /var/log/auth.log
Para verificar los atributos aplicados, use el comando lsattr. Si el atributo i está presente, se mostrará como ----i-----------.
2. Hardening del Kernel mediante Sysctl
La interfaz sysctl permite modificar parámetros del núcleo en tiempo de ejecución, generalmente a través de archivos en /proc/sys o de manera persistente en /etc/sysctl.conf. La siguiente configuración endurece el sistema operativo frente a ataques comunes de red (spoofing, inundación SYN, y redirecciones ICMP):
Configuración /etc/sysctl.conf (Lista para Copiar):
# Deshabilitar redireccionamientos ICMP para prevenir ataques de suplantación de ruta (ICMP Redirects)
# Explicación: Los atacantes pueden usar mensajes ICMP de redireccionamiento para modificar
# la tabla de enrutamiento de un host, manipulando el flujo de tráfico [11, 12].
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.lo.accept_redirects = 0

# Mitigación de IP Spoofing mediante el filtro de ruta inversa (Reverse Path Filtering - RPF)
# Explicación: RPF verifica si el paquete entrante tiene una ruta de respuesta válida
# en la tabla de enrutamiento. Si la dirección de origen no es local, el paquete es descartado,
# protegiendo contra la suplantación de direcciones IP de origen [13, 14].
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Deshabilitar el enrutamiento de origen (Source Routing)
# Explicación: Impide que atacantes puedan especificar la ruta que un paquete debe tomar,
# un vector común en ataques de spoofing y manipulación de red [11, 15, 16].
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0

# Mitigación de Ataques SYN Flood
# Explicación: Habilitar SYN Cookies. Cuando la cola de conexiones a medio abrir se llena
# (durante un ataque SYN Flood), el kernel utiliza un mecanismo criptográfico (SYN Cookies)
# para autenticar la conexión sin consumir recursos, permitiendo conexiones legítimas [17-19].
net.ipv4.tcp_syncookies = 1

# Ignorar peticiones de echo ICMP dirigidas a direcciones de broadcast (Ataque Smurf)
# Explicación: El ataque Smurf utiliza direcciones de broadcast para amplificar el tráfico
# ICMP Echo Request, inundando a la víctima [20, 21]. Esto previene que el host sea
# usado como amplificador.
net.ipv4.icmp_echo_ignore_broadcasts = 1
Para aplicar los cambios inmediatamente sin reiniciar, ejecute: sysctl -p.
3. Defensa Activa: Script Honeyports con Iptables
La técnica de Honeyports (puertos trampa) implica escuchar en puertos conocidos por ser escaneados o atacados (como el puerto Telnet 23, o un puerto HTTPS falso como el 443 o 8080) y bloquear automáticamente al origen que intente conectarse, frustrando la fase de reconocimiento activo.
El siguiente script en Bash utiliza netcat (nc) en modo de escucha para simular un servicio abierto en el puerto 23/TCP y usa iptables para bloquear la IP atacante de forma persistente.
#!/bin/bash

# Configuración
HONEY_PORT="23"
LOG_FILE="/var/log/honeyport_${HONEY_PORT}.log"
IPTABLES_CHAIN="HONEYPOT_DROP"
HOSTS_DENY="/etc/hosts.deny"

# 1. Preparación del registro y la cadena de IPTables
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Servicio Honeyport iniciado en el puerto ${HONEY_PORT}." >> "$LOG_FILE"

# Crear o verificar la cadena de IPTables si no existe
/sbin/iptables -L "$IPTABLES_CHAIN" &> /dev/null
if [ $? -ne 0 ]; then
    /sbin/iptables -N "$IPTABLES_CHAIN"
    # Redirigir el tráfico entrante al puerto HONEY_PORT a nuestra trampa (Netcat)
    /sbin/iptables -A INPUT -p tcp --dport ${HONEY_PORT} -j "$IPTABLES_CHAIN"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cadena IPTables ${IPTABLES_CHAIN} creada y enrutada." >> "$LOG_FILE"
fi

# 2. Función de bloqueo
function block_attacker {
    local IP=$1
    
    # 2.1. Bloquear inmediatamente con IPTables (Drop)
    # Se añade la regla al inicio (-I) de la cadena HONEYPOT_DROP para priorizar el bloqueo.
    # El bloqueo con DROP asegura que no se envíe respuesta (modo stealth) [26].
    /sbin/iptables -A ${IPTABLES_CHAIN} -s "$IP" -j DROP
    
    # 2.2. Bloquear a nivel de aplicación (para servicios controlados por TCP Wrappers)
    # Se añade la IP a /etc/hosts.deny. Esto es relevante para servicios legados 
    # que utilizan tcpd (como telnet, ftp) si el puerto no estuviese enrutado previamente [27, 28].
    echo "ALL: $IP" >> "$HOSTS_DENY"
    
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ATAQUE DETECTADO: IP ${IP} bloqueada en IPTables y hosts.deny." >> "$LOG_FILE"
    
    # Hacer persistentes las reglas de IPTables
    # Guardar las reglas inmediatamente para sobrevivir a reinicios [29].
    /sbin/iptables-save > /etc/iptables/rules.v4
}

# 3. Función de escucha con Netcat
while true; do
    # Usar nc en modo de escucha (-l) en el puerto HONEY_PORT, con el indicador numérico (-n) 
    # y verbosidad (-v). Espera una conexión y, al recibir datos, sale [30].
    # El timeout (-w 10) asegura que no se cuelgue infinitamente.
    # Se usa la salida de netcat (conexión de origen) para identificar al atacante.
    ATTACK_SOURCE=$(/bin/nc -l -n -v -w 10 -p ${HONEY_PORT} -c 'echo "Invalid Service"') 2>&1
    
    # Extraer la IP de la línea de conexión (ej: "Connection from 192.168.1.5:54321 received")
    IP=$(echo "$ATTACK_SOURCE" | grep "Connection from" | awk '{print $3}' | cut -d':' -f1)
    
    if [[ "$IP" =~ ^[31-39]{1,3}\.[31-39]{1,3}\.[31-39]{1,3}\.[31-39]{1,3}$ ]]; then
        block_attacker "$IP"
    fi
done
4. Auditoría de Comandos y Anti-Evasión (Bash History)
Para frustrar los intentos de un atacante de borrar su rastro (.bash_history), implementamos mecanismos de persistencia de comandos y centralización de registros.
Protección de .bash_history (Inmutabilidad)
La principal técnica para evitar que un atacante borre o sobrescriba su historial de comandos es utilizar el atributo solo anexión (+a) del sistema de archivos. Si un atacante intenta borrar o hacer un symlink a /dev/null para ocultar su actividad (una táctica común), el sistema lo impedirá, asegurando que cada comando ejecutado quede registrado.
# Para el usuario root
chattr +a /root/.bash_history

# Para otros usuarios administrativos (ej: 'sysadmin')
chattr +a /home/sysadmin/.bash_history
El atributo +a permite al shell seguir escribiendo nuevos comandos al final, cumpliendo con la necesidad de registro continuo.
Variables de Entorno y Logs
Aunque los atacantes a menudo anulan variables como HISTFILE para evitar el registro, forzar la rotación del historial y configurar el entorno es una defensa en profundidad. El bash utiliza variables como HISTSIZE (máximo de líneas guardadas) y HISTFILESIZE para gestionar el historial.
Configuración para Bash (Añadir a /etc/profile o /etc/bash.bashrc):
# 1. Aumentar el tamaño del historial para evitar la sobrescritura rápida
# Almacena hasta 50000 comandos en la memoria de la sesión y en el archivo.
HISTSIZE=50000
HISTFILESIZE=50000

# 2. Registrar el timestamp del comando
# Esto permite saber cuándo se ejecutó cada comando, crítico para análisis forense.
HISTTIMEFORMAT="%F %T "

# 3. Evitar duplicados y entradas obvias que buscan evadir la auditoría
# 'erasedups' elimina duplicados, 'ignorespace' ignora comandos precedidos de espacio.
HISTCONTROL=ignoreboth:erasedups
Envío de Logs a Servidor Remoto (Syslog)
La medida de seguridad más efectiva contra la alteración de logs es la centralización. La integridad de los logs en el sistema comprometido no puede garantizarse. Por lo tanto, los logs de autenticación (auth.log o secure) y del sistema deben ser enviados en tiempo real a un servidor de log endurecido (syslog-ng o rsyslog).
Configuración de Rsyslog para Envío Remoto Seguro:
Modifique /etc/rsyslog.conf en el host local. Esta configuración asume que el servidor remoto (loghost.example.com o 10.1.1.5) acepta logs a través del puerto UDP/514 (un protocolo simple) o TCP/6514 (recomendado por su fiabilidad y para futuras implementaciones TLS).
# Definir el host remoto de logs y el protocolo.
# Usando '@' para UDP (menos fiable) o '@@' para TCP (más fiable) [46].

# *Ejemplo usando TCP (Puerto 6514 - recomendado):*
# *.* @@@loghost.example.com:6514

# *Ejemplo usando UDP (Puerto 514):*
# authpriv.* @loghost.example.com
# *.err;kern.debug;daemon.err @loghost.example.com

# Nota: La facilidad 'authpriv' es crítica, ya que registra los eventos de SSH, su, y sudo [47].
authpriv.*                                              @10.1.1.5:514

# Reiniciar el servicio Rsyslog para aplicar los cambios
systemctl restart rsyslog
