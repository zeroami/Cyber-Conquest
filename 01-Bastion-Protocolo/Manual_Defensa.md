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
