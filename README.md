# VENEJUGOS · Dashboard de Evaluación de KPI's Nestlé

Dashboard interactivo estilo Power BI desarrollado para **Venejugos C.A.**, aliado comercial de Nestlé, para la evaluación de los KPI's entregables de cumplimiento y activación de clientes.

Todo el procesamiento ocurre **en el navegador del usuario**: el archivo de ventas nunca se sube a un servidor.

---

## Contenido del repositorio

```
index.html                      Panel de performance (vista pública, igual a performance.html)
performance.html                Panel de performance · solo lectura, con impresión
admin.html                      Panel administrativo · carga, cuotas y publicación
datos.js                        Datos publicados que alimentan el panel de performance
src/app.html                    Fuente única de la que se generan los tres paneles
build.py                        Regenera admin.html, performance.html e index.html
assets/logo-venejugos.jpg       Logotipo institucional
plantilla_datos_ejemplo.csv     Estructura mínima esperada del archivo de ventas
README.md
```

## Publicación en GitHub Pages

1. Crear un repositorio nuevo (por ejemplo `venejugos-kpi-nestle`).
2. Subir el contenido de este ZIP a la raíz del repositorio.
3. Ir a **Settings → Pages → Source: Deploy from a branch → main / (root)** y guardar.
4. A los pocos minutos el tablero queda disponible en:
   `https://<usuario>.github.io/<repositorio>/`

También funciona abriendo `index.html` directamente con doble clic (requiere conexión a internet la primera vez para cargar las librerías de gráficos).

---

## Cómo se actualiza la información (flujo mensual)

El panel visual **no recalcula nada por su cuenta**: muestra lo que contiene el archivo `datos.js`. Ese archivo es el puente entre el panel administrativo y la vista pública.

1. Abrir el tablero y entrar al **Panel Administrativo** con la llave `DIGIMARKET2026`.
2. Cargar el archivo de ventas del mes, verificar el mapeo y ajustar targets, cuota en kilos y días del período.
3. Presionar **PROCESAR Y GENERAR DASHBOARD**. El panel visual queda actualizado de inmediato en ese equipo.
4. Presionar **GENERAR datos.js PARA GITHUB** y guardar el archivo.
5. En GitHub: **Add file → Upload files**, subir `datos.js` en la raíz (junto a `index.html`) y **Commit changes**.
6. En 1 o 2 minutos el enlace de GitHub Pages muestra la información nueva a todos.

### Jerarquía de datos

| Origen | Cuándo se usa |
|---|---|
| `datos.js` del repositorio | Cuando es la versión más reciente. Es lo que ven todos los usuarios. |
| Copia local del navegador | Cuando el equipo procesó un archivo más nuevo que el publicado. |

La barra superior muestra siempre la fecha de los datos y su origen (*publicado en GitHub* o *carga local de este equipo*). El botón **Borrar datos de este equipo** descarta la copia local y vuelve a la versión publicada.

### Acceso

El **panel visual es público**: cualquiera que abra el enlace ve el reporte publicado sin clave. La llave solo protege el panel administrativo, es decir, la carga y actualización de la información.

---

## Llave de seguridad

| Elemento | Valor |
|---|---|
| Llave de seguridad | `DIGIMARKET2026` |

Para cambiarla, editar en `index.html` la línea:

```js
var CLAVE = "DIGIMARKET2026";
```

---

## Estructura de páginas

| Página | Para quién | Qué hace |
|---|---|---|
| `admin.html` | Uso interno | Pide la llave, carga el archivo, define cuotas y genera `datos.js`. |
| `performance.html` e `index.html` | Nestlé y el equipo comercial | Muestran el reporte publicado. Sin clave y sin opción de modificar datos. |

La clave `DIGIMARKET2026` existe solo dentro de `admin.html`; las páginas públicas no la contienen.

Para modificar el tablero se edita `src/app.html` y se ejecuta `python build.py`, que regenera las tres páginas.

## Los dos paneles

### 1. Panel Administrativo
- Carga del archivo de ventas (`.xlsx`, `.xls`, `.csv`) por arrastre o selección.
- Mapeo automático de columnas: **DescrSubCategoría (columna J)**, cliente, kilos, venta y fecha. Puede corregirse manualmente.
- Carga de cuotas: **Target Act %** por categoría y **cuota en kilos** del mes.
- Parámetros de proyección: días transcurridos, días del mes y universo de clientes.
- La configuración se guarda en el navegador para el siguiente uso.

### 2. Panel Visual
- KPI's principales, gráficos interactivos, tabla de detalle, activación total del portafolio, listado de clientes no activados y resumen ejecutivo escrito.
- Botón **Imprimir / Guardar PDF** con hoja A4 horizontal optimizada.

---

## Reglas de negocio aplicadas

- **Categorías foco del reporte detallado:** CALDOS, CHOCOLATES, CERELAC, LA CAMPESINA, LECHE CONDENSADA. El resto de sub-categorías se omite de ese análisis, pero sí se contabiliza en la activación total del portafolio.
- **Activación:** cliente con venta mayor a 0. Cliente no activado: venta igual a 0.
- **Activación %:** clientes activados ÷ universo de clientes × 100.
- **Cumplimiento de cuota:** activación % ÷ Target Act % × 100.
- **Faltante de clientes:** `techo(universo × target%) − activados`.
- **Faltante en kilos:** cuota kg − kg reales.
- **Proyección al cierre:** valor actual × (días del mes ÷ días transcurridos).

### Targets de cumplimiento (Nestlé)

| Categoría | Target Act |
|---|---|
| CALDOS | 75% |
| SOPAS | 75% |
| LECHE CONDENSADA | 20% |
| CHOCOLATES | 85% |
| GALLETAS | 70% |
| CERELAC | 40% |
| NESTEA | 25% |
| NESTUM | 30% |
| LA CAMPESINA | 20% |
| NUTRIRINDE | 20% |
| FORMULAS INFANTILES | 0% |

Los valores son editables desde el panel administrativo sin tocar el código.

---

## Estatus de semáforo

| Estatus | Rango de cumplimiento |
|---|---|
| CUMPLE | 100% o más |
| EN RIESGO | 70% – 99,9% |
| CRÍTICO | menos de 70% |

---

## Tecnología

HTML, CSS y JavaScript sin framework. Librerías por CDN: **SheetJS** (lectura de Excel) y **Chart.js** (gráficos).

Identidad visual Venejugos: azul `#1230A8`, rojo `#E30613`, blanco.
