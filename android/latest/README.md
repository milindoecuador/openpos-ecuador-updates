# KTEL POS para Android

**Versión actual: 1.2.8**

- [Descargar KTEL POS Android 1.2.8](./KTEL-POS-Android-1.2.8.apk)
- SHA-256: `ed42679f7a3171499dd8bdc4d5258623ab8bcd6a93e1fe5efa71d9cf71f4ded4`
- [Manifiesto firmado](./android-manifest.txt)

La versión 1.2.8 corrige el error `Cannot set properties of null (setting 'textContent')` al abrir Actualizaciones dentro de Android. Conserva ocultos los controles que necesita la página de escritorio mientras presenta los controles propios de actualización Android.

La actualización Android se comprueba al abrir y desde **Módulos → Actualizaciones → Buscar actualización Android**. Si hay una versión, se verifica antes de pedir a Android que confirme la instalación. También conserva la corrección del host de GitHub añadido en 1.2.7.

Incluye accesos nativos a **Cocina** y **Ventas**, con interfaz de cocina adaptada a teléfonos y tablets. Requiere servidor activo y licencia LAN vigente para operar; actualizar la APK no altera la base de datos del POS.
