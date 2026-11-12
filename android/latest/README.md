# KTEL POS para Android

**Versión actual: 1.3.0**

- [Descargar KTEL POS Android 1.3.0](./KTEL-POS-Android-1.3.0.apk)
- SHA-256: `3916a034529ef1291ae8e6b23762c530dee361aaccf1f653c42ad075a93e3bb3`
- [Manifiesto firmado de actualización](./android-manifest.txt)
- [Historial y hashes](./SHA256SUMS.txt)

Incluye punto de venta móvil, acceso a comandas de cocina, vistas adaptables para teléfono/tablet, búsqueda y verificación automática de actualizaciones, y asistente de acceso remoto privado con Tailscale Serve. Conserva el certificado Android del canal anterior; la actualización se instala encima y no modifica la base de datos del servidor.

Para acceso remoto, instala Tailscale oficial en Android y PC, incorpóralos al mismo tailnet, habilita HTTPS privado con `tailscale serve 8000` en la PC y configura en la app la dirección `.ts.net`. La PC debe estar encendida; no se expone el puerto con Funnel. La licencia adicional de terminal sigue siendo obligatoria.

Compilación de evaluación con certificado Android del canal existente; no es una publicación de Play Store.
