# KTEL POS para Android

**Versión actual: 1.2.6**

- [Descargar KTEL POS Android 1.2.6](./KTEL-POS-Android-1.2.6.apk)
- SHA-256: `2a30f553f84c25830ad900da4bb962570b3850bce6f9bd2329eb51fa38557dfa`
- [Manifiesto firmado para el actualizador](./android-manifest.txt)

La APK revisa actualizaciones al iniciar. También puedes buscarla desde **Módulos → Actualizaciones → Buscar actualización Android**. Si no hay conexión, muestra que no pudo comprobar; si está al día, lo informa; si hay una versión, la descarga verificada y Android solicita confirmar la instalación.

La versión 1.2.6 repara el botón manual que antes mostraba el actualizador del escritorio Windows y podía aparecer deshabilitado desde el teléfono. La búsqueda ahora consulta el canal Android firmado. El botón ↻ de Cocina refresca las comandas del servidor sin reiniciar la sesión.

Incluye accesos nativos a **Cocina** y **Ventas**. En teléfono, Cocina organiza las etapas en una lista vertical con controles táctiles amplios; en tablet las presenta en tres columnas. Los cambios de estado se guardan en el servidor y la lista se actualiza cada 15 segundos.

La instalación conserva la firma de Android 1.2.5 para permitir actualizar sobre ella. El servidor local debe estar encendido y la terminal necesita licencia LAN vigente para operar. La actualización de la APK no modifica la base de datos del POS.
