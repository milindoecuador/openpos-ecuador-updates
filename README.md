# OpenPOS Ecuador — Instaladores

Canal de distribución del instalador Windows. El código fuente se mantiene por separado. No se publican datos de negocios, certificados ni claves privadas.

## Instalar
Descargue `OpenPOS-Setup-VERSION.exe` desde Releases. La instalación inicial de 3.7.0 es manual. El control local permite buscar actualizaciones y habilitar la instalación automática con todos los turnos cerrados.

Cada versión contiene `installer-manifest.txt`, firmado con RSA por el proveedor y con SHA256 del instalador. El cliente verifica con la clave pública incorporada. Esta firma de integridad no sustituye un certificado de editor Windows.

## Condiciones de operación
La licencia y sus adicionales se activan dentro del programa. La autorización SRI exige certificado real y validación en pruebas. La consulta externa de cédula necesita un proveedor autorizado configurado; no se incluyen credenciales. Conectar el escritorio a Online usa un único servidor HTTPS, sin sincronización de dos bases offline.

Se conservan los datos fuera de la carpeta de instalación. Respalde antes de actualizar. Los borradores y pre-releases no se aplican automáticamente.
