# GLOBAL KPI · Venejugos

![GLOBAL KPI](logo/global-kpi-logo-claro.png)

Tablero de cumplimiento por marca de todo el portafolio.

Réplica a escala macro del tablero de cumplimiento de KPI Nestlé. Usa la misma arquitectura
(tres páginas HTML autocontenidas, un `dataset.json` y publicación en GitHub Pages), pero evalúa
**todo el portafolio** y toma como dimensión la **marca** (columna `DescrMarca` del Reporte General)
en lugar de la subcategoría Nestlé.

| Archivo | Para qué sirve |
|---|---|
| `admin.html` | **Panel admin**. Llave, carga del Excel, targets y cuotas por marca, estructura comercial. |
| `index.html` | **Estadístico general**: cobertura, volumen, proyección, Pareto de marcas y mix por categoría. |
| `performance.html` | **Performance vendedores por marca**: activación por marca, por supervisor y vendedor. |
| `dataset.json` | Datos del último reporte procesado, con los parámetros incluidos. |
| `logo/` | Logo GLOBAL KPI en SVG y PNG (ícono redondeado, ícono cuadrado del encabezado, versión clara y oscura). |
| `reporte.html` | **Resumen personalizado por asesor**: documento de seguimiento por supervisión, generado con el último reporte cargado. |
| `historial.json` | Cierres diarios congelados. Lo crea el panel administrativo al publicar. |

Chart.js y SheetJS van incrustados: no requiere instalación ni conexión a internet.

---

## Qué cambia frente al modelo Nestlé

| Modelo Nestlé | Modelo macro |
|---|---|
| Solo filas Nestlé (las demás se descartan) | Todas las filas del archivo |
| Dimensión: `DescrSubCategoría` | Dimensión: `DescrMarca` (respaldo: `CodMarca`) |
| 5 categorías foco fijas en el código | Marcas foco elegidas en el panel; por defecto las 5 de mayor venta |
| Targets fijos por categoría | Target por marca editable; las marcas sin target usan el target por defecto (25%) |
| Cuotas de kilos fijas | Cuotas por marca y por asesor en US$ y en kilos, editables |
| Maestros general, Confites y base Nestlé | Un maestro de clientes de todo el portafolio |
| Volumen en kilos | Volumen en US$ por defecto, conmutable a kilos en cada página |
| Parámetros solo en el navegador del administrador | Los parámetros viajan dentro de `dataset.json` |

Visuales nuevas propias de la vista macro: marcas con venta, profundidad (marcas promedio por
cliente activo), venta por cliente activo, concentración (cuántas marcas hacen el 80% de la venta),
curva de Pareto por marca, mix por categoría (`DescrCategoría`) y rolling por marca.

## 1. Panel admin (`admin.html`)

1. Abra `admin.html` e introduzca la llave: **DIGIMARKET2026**
2. Cargue el `.xlsx` del Reporte General (botón o arrastrando el archivo).
3. **Parámetros generales**: maestro de clientes (por defecto 1.562, la suma de las carteras),
   target por defecto, medida de volumen con la que abren las páginas y fecha de corte.
4. **Marcas del portafolio**: una fila por marca encontrada, ordenada por venta.
   - Marque las marcas foco. Sin ninguna marcada se toman las cinco de mayor venta.
   - Escriba el target de activación y las cuotas en US$ y kilos.
   - **Precargar cuotas vacías con la proyección** propone como cuota la proyección de cierre
     al ritmo actual; úsela como punto de partida y ajuste.
5. **Estructura comercial**: supervisor, cartera y cuotas por asesor. Viene precargada con la
   estructura del modelo Nestlé; los asesores del archivo sin cartera aparecen marcados.
6. Pulse **Guardar parámetros** y luego **Publicar dataset.json** o **Descargar dataset.json**.

## 2. Estadístico general (`index.html`)

Filtros de zona, vendedor, categoría y medida de volumen.

- **Paso 1**: activación de las marcas foco contra su target, y su volumen contra cuota.
- **Paso 2**: activación de todas las marcas y cuadro de cumplimiento con participación.
- **Paso 3**: clientes activados y no activados sobre el maestro.
- Pareto de participación, mix por categoría, zonas y vendedores con mayor aporte, resumen ejecutivo.

## 3. Performance vendedores por marca (`performance.html`)

Selector de **marca de activación** (todas o una marca), vendedor, medida y orden.
Pestañas: equipos y marcas, clientes activados (con CSV), rolling de volumen por marca y por
asesor, y déficit semanal en volumen y en cobertura.

## 4. Resumen personalizado por asesor (`reporte.html`)

Se abre con el botón **Resumen personalizado** de Performance vendedores por marca. Reproduce el
formato "Seguimiento por Asesor — Equipo …" y se regenera solo con cada publicación del admin.

- **Filtros**: supervisiones, asesores, marcas, secciones, corte (cualquier día del mes cargado),
  medida del rolling y de las marcas, meta de activación de cartera (85 %) y umbrales en rojo.
- **Por supervisión**: portada con cuadro comparativo del equipo y referencia de la supervisión.
- **Por asesor**: posición general, cumplimiento por marca, déficit semanal (opcional) y focos
  generados con su desempeño.
- **Nestlé se omite** de todos los cálculos: se evalúa en su propio tablero.
- La cuota de cada marca por asesor se prorratea según su cartera (cartera ÷ maestro de clientes).
- Salida: **Imprimir o guardar en PDF** (A4, un asesor por página) o **Descargar para Word**.

---

## Reglas de cálculo

- **Activación**: cliente con venta mayor a cero en la marca, sobre el maestro de clientes.
  Con filtro de vendedor la base es su cartera; con filtro de zona, los clientes atendidos en ella.
- **Meta por asesor**: cartera asignada × target de la marca (100% en "todas las marcas").
- **Proyección**: volumen del período × (días hábiles del mes ÷ días hábiles transcurridos).
- **Clientes faltantes**: target × universo − clientes ya activados.
- **Profundidad**: promedio de marcas distintas compradas por cada cliente activo.
- **Documentos**: igual que el modelo Nestlé. Las notas de crédito de tesorería (NCTESO, NCADM)
  se excluyen; las ligadas a una factura netean monto y kilos pero no activan.
- **Mes evaluado**: el de la fecha más reciente del archivo; las líneas de otros meses se dejan fuera.

## Déficit semanal y metas por día hábil

1. **Semanas del mes**: bloques de lunes a viernes dentro del mes. La primera y la última suelen
   quedar cortas (octubre 2026: S1 = 1 y 2, solo 2 días).
2. **Feriados**: se cargan en el panel administrativo y se descuentan. Con el 12/10 octubre 2026
   tiene 21 días hábiles y la semana 3 queda de 4 días.
3. **Reparto de la cuota**: cada semana recibe cuota × (sus días hábiles ÷ días hábiles del mes).
   Una semana de 2 días carga 2/21 de la cuota, no 1/5.
4. **Meta acumulada al cierre de un día** = cuota × días hábiles transcurridos ÷ días hábiles del mes.
   En la semana en curso solo se exige lo de los días ya vividos.
5. **Déficit** = meta acumulada − real acumulado, contando solo lo facturado hasta ese día.
   El déficit del equipo es la suma de los déficits individuales.
6. **Para cerrar la semana**: lo que le falta a cada asesor para llegar al viernes con la meta
   acumulada de la semana, y cuánto es por día.

La meta de cobertura (cartera × target) se reparte igual que la cuota de volumen.

## Histórico de cierres diarios (`historial.json`)

- Cada día terminado queda **congelado** con su déficit semanal por asesor, en US$, kilos y
  clientes, más el avance de cada marca. Cambiar cuotas después no altera los cierres ya
  registrados; para recalcular un mes use **Rehacer los cierres de este mes**.
- Se registran solos al cargar el reporte: todos los días del archivo menos el último, que entra
  cuando ya pasó (o marcando "El último día del archivo ya cerró").
- **Publicar dataset.json** también publica `historial.json`, fusionándolo con el del repositorio:
  los cierres de meses anteriores nunca se pierden.
- En `performance.html`, pestaña **Histórico de cierres**: selector de mes y día, día anterior y
  siguiente, evolución diaria real contra meta, matriz de déficit asesor × día, marcas al cierre y
  CSV. Cada cierre tiene enlace propio: `performance.html#cierre=2026-10-07`.

### Columnas que lee del Excel

`DescrMarca`, `DescrCategoría`, `DescrSubCategoría`, `FechaFactura`, `CódigoCliente`, `RazónSocial`,
`RucCliente`, `DescZona`, `NombreVend`, `NombSuperv`, `Kilos`, `Cantidad`, `PrecioTotal`, `NúmeroFactura`.

---

## 4. Publicación en GitHub

Use un **repositorio o carpeta distinta** a la del tablero Nestlé: los dos esperan un
`dataset.json` en su raíz con formatos diferentes. Si GLOBAL KPI encuentra un `dataset.json` del
modelo Nestlé lo rechaza y lo indica en la cinta superior.

```bash
git init
git add .
git commit -m "GLOBAL KPI - Venejugos"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

En GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root)**.

La publicación con token funciona igual que en el modelo Nestlé (tarjeta **Publicar en GitHub**,
token de alcance fino con *Contents: Read and write*). Las llaves de almacenamiento del navegador
llevan el prefijo `vjm_`, así que ambos tableros pueden convivir en el mismo dominio sin pisarse.

## 5. Actualizar cada mes

1. Cargue el nuevo `.xlsx` en el panel administrativo.
2. Revise marcas nuevas, foco, targets, cuotas y asesores sin cartera.
3. **Guardar parámetros** y **Publicar dataset.json**.

---

Venejugos C.A. · Ventas 0412 501-6394 · @Venejugos
