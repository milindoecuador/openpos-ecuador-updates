# KTEL POS para Android

**Versión actual: 1.2.7**

- [Descargar KTEL POS Android 1.2.7](./KTEL-POS-Android-1.2.7.apk)
- SHA-256: `c260d773d8bfbea1386070c4b2f11f0eb1eec3f86dbc5a3df6c125290614735b`
- [Manifiesto firmado para el actualizador](./android-manifest.txt)

La versión 1.2.7 corrige el actualizador: autoriza la descarga HTTPS desde `raw.githubusercontent.com`, dominio donde GitHub sirve el manifiesto firmado y la APK. La versión 1.2.6 ya corrigió la acción dentro de la pantalla para que el teléfono consulte actualizaciones Android y no el instalador Windows. Si una instalación anterior no puede actualizarse por sí sola, instala esta APK una vez manualmente; en adelante podrá comprobar el canal al abrir y desde el botón Android.

En **Módulos → Actualizaciones**, Android muestra su versión instalada y un botón **Buscar actualización Android**. Informa si no hay conexión, si está al día o si existe una versión nueva. La APK se verifica antes de instalar y Android solicita confirmar.

Incluye accesos a **Cocina** y **Ventas**. Cocina organiza las etapas en lista vertical en teléfono y tres columnas en tablet; refresca pedidos cada 15 segundos y guarda cambios en el servidor.

Mantiene la firma Android de versiones previas. Requiere que el servidor local esté encendido y licencia LAN vigente para operar. Actualizar la APK no modifica la base de datos del POS.
