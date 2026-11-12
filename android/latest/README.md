# KTEL POS para Android

**Versión actual: 1.2.9**

- [Descargar KTEL POS Android 1.2.9](./KTEL-POS-Android-1.2.9.apk)
- SHA-256: `be14f8803756654f82d47248c889306be8ffff96e2adb799f5850d61917a0c99`
- [Manifiesto firmado de actualización](./android-manifest.txt)
- [Historial y hashes](./SHA256SUMS.txt)

La APK permite configurar una URL LAN y una URL HTTPS privada (por ejemplo Tailscale Serve), conserva la licencia y los servidores si no hay conexión e intenta primero la LAN y después el endpoint remoto. Requiere que Tailscale esté conectado aparte en Android y en la PC, el servidor esté encendido y la licencia adicional de terminal sea válida.

La comprobación de actualización está disponible al abrir **Actualizaciones** y desde su botón. Descarga el APK, verifica manifiesto, firma/hash e identidad de paquete antes de pedir a Android que confirme la instalación. Android requiere permitir instalar actualizaciones desde la aplicación que descarga el archivo.

Incluye accesos de **Cocina** y **Ventas**, y vistas adaptables para teléfonos y tablets. Actualizar la APK no altera la base de datos de KTEL POS.

Build local: `assembleDebug`, con la misma firma Android del canal 1.2.8. No es una compilación de tienda Play Store.
