# Tablero de cumplimiento de KPI Nestlé · Venejugos

Dashboard interactivo estilo Power BI para la evaluación de los KPI entregables de cumplimiento
Nestlé Venezuela, presentado por **Venejugos** en su condición de aliado comercial.

Dos páginas HTML autocontenidas: no requieren servidor, ni instalación, ni conexión a internet
(Chart.js y SheetJS van incrustados dentro de cada archivo).

| Archivo | Para qué sirve |
|---|---|
| `admin.html` | Panel administrativo. Llave de seguridad, carga del Excel de ventas, maestro de clientes Nestlé, cuotas y publicación. |
| `performance.html` | Performance vendedores: activación por supervisor y vendedor. |
| `reporte.html` | Resumen por asesor (con llave): activación de cartera contra el maestro de clientes, semanas, proyección y clientes por activar. Word o PDF. |
| `dataset.json` | Ventas del último reporte publicado desde el panel. |
| `maestro.enc.json` | Maestro de clientes Nestlé cifrado con la llave (lo crea el panel al publicar). |

---

## 1. Panel administrativo (`admin.html`)

1. Abra `admin.html`.
2. Introduzca la llave de seguridad (la misma que ya usa el equipo administrativo; no se escribe en los archivos).
3. Cargue el archivo `.xlsx` del Reporte General (botón o arrastrando el archivo).
4. Defina los parámetros y pulse **Guardar parámetros**:
   - **Cuota de kilos por categoría**: Caldos 3.706, Chocolates 3.812, Cerelac 1.311,
     La Campesina 789 y Leche Condensada 350 kg. Total 9.968 kg.
   - **Cuota de venta (US$)**: objetivo en valor.
   - **Maestro de clientes general**: 1.028 clientes. Base de activación de todas
     las categorías salvo Confites.
   - **Maestro Confites**: 1.297 clientes. Aplica a chocolates y galletas.
5. Pulse **Performance vendedores**. La página ya muestra los datos nuevos.

El archivo procesado queda guardado en el navegador, así que Performance y el resumen lo toman
automáticamente en ese mismo equipo. Para que todo el equipo lo vea, use
**Descargar dataset.json** y publique ese archivo en el repositorio (ver punto 3).

La llave se valida en el navegador con su huella; no aparece escrita en los archivos. El maestro de
clientes se publica cifrado con ella. El `dataset.json` de ventas sigue siendo legible para quien
conozca su dirección mientras el repositorio sea público.

## Maestro de clientes y resumen por asesor

**Maestro de clientes Nestlé** (tarjeta nueva del panel administrativo):

1. Cargue el Excel del maestro (hoja `CLIENTES MATRIZ NESTLE`, columnas `RIF`, `Razón Social` y `VENDEDOR`).
2. Los asignados a **RECUPERACION** se excluyen. El **día de visita** se toma de la columna
   `DIA DE VISITA` de la hoja; si no está, de la hoja `MAESTRO CLIENTES` del mismo archivo o de la
   copia del MAESTRO CLIENTES vinculado que Excel guarda dentro del archivo.
   Muestra cuántos clientes tiene cada vendedor y la diferencia contra su cartera del panel.
3. Pulse **Publicar ventas y maestro**. Se escriben `dataset.json` y `maestro.enc.json`.
   El maestro va cifrado con la llave: en el repositorio no se puede leer sin ella.
   Con él se guardan el teléfono, la dirección y la ruta de cada cliente que aparecen en los
   reportes de ventas cargados, y se acumulan mes a mes.
4. El maestro solo hay que volver a cargarlo cuando cambie. Cada publicación nueva de ventas
   reutiliza el maestro ya publicado y actualiza los contactos.

**Resumen por asesor** (`reporte.html`), con el formato *Comportamiento por categoría y proyección de la semana*:

- Pide la misma llave del panel administrativo.
- Base de cada asesor: sus clientes en el maestro. Activado: cliente del maestro con compra Nestlé
  mayor a cero en el mes, sin importar quién le facturó. Meta: 85 % de la base (editable).
- Bases por categoría (A&B y Confites) y targets: los del panel.
- Semanas de lunes a viernes sin feriados nacionales de Venezuela. Si el mes empieza a mitad
  de semana, esa primera semana es la **S0**.
- Ritmo = clientes nuevos por día hábil. Compara la semana anterior con la actual y proyecta
  la siguiente con la tendencia (variación entre ambas semanas, nunca mayor que 1).
- El corte automático es el último día facturado; si ese día tiene muy pocas facturas se toma
  como día en curso y se usa el anterior. También se puede elegir el corte a mano.
- Por cada coordinación: cuadro comparativo, meta semanal con proyección, categorías, clientes
  sin activar y focos. Por cada asesor: su análisis y su **lista de clientes** (hoja horizontal)
  con todos sus clientes del maestro: **Atendido** si compró al menos una categoría Nestlé en el
  mes, **No atendido** si no se le ha vendido nada, su **día de visita** del maestro y una marca ✓
  por cada categoría Nestlé que compró (sin teléfonos). Por defecto se usan todas las categorías Nestlé con target.
- Se imprime o guarda en PDF, o se descarga para Word.

Si el maestro no está publicado, el resumen usa la cartera del panel y las listas solo traen
clientes que ya compran; lo indica en pantalla.

## 2. Performance vendedores (`performance.html`)

Se abre desde el botón **Performance vendedores** del panel administrativo,
y toma los mismos datos, sin carga aparte.

- Una tarjeta por supervisor con su dona de cumplimiento y el marcador **meta / activados**.
- Dentro de cada tarjeta, el equipo de vendedores ordenado por cumplimiento; los que están
  por debajo de 70% quedan resaltados en rojo.
- Selectores de **categoría de activación** (las once de la tabla Nestlé más la vista
  general), de **supervisor** para ver solo su equipo (la lista de vendedores se limita a los
  suyos), de **vendedor** para aislar a una persona, y de **medida**: cumplimiento de la
  meta o su inverso, la brecha pendiente. El filtro de supervisor aplica a todas las pestañas:
  equipos, clientes, rolling y déficit semanal.
- **Alerta de vendedores**: quienes están por debajo de 70% del target, con los clientes
  que les faltan y el ritmo diario necesario.
- **Alerta de activación**: categorías por debajo del target, ordenadas por brecha.
- Tabla de **activación por categoría** con meta, activados, clientes por activar y
  activaciones por día hábil.
- Tabla final por vendedor con cartera, meta, activados, cumplimiento, brecha pendiente,
  clientes por activar y **activaciones por día** necesarias para llegar a la meta.

**Cómo se calcula la meta**: cartera atendida por el vendedor en el período × target de la
categoría. La cartera sale del archivo, es decir los clientes a los que ese vendedor
facturó algo; no hay asignación de clientes por vendedor en el reporte general.

## 4. Publicación en GitHub

```bash
git init
git add .
git commit -m "Tablero de cumplimiento Nestlé - Venejugos"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

Luego, en GitHub: **Settings → Pages → Source: Deploy from a branch → main / (root)**.
Las páginas quedan en `https://USUARIO.github.io/REPOSITORIO/admin.html`
y `.../performance.html`.

## 5. Actualizar el tablero cada mes

El panel administrativo escribe el `dataset.json` directamente en el repositorio.
Configuración inicial, una sola vez:

1. En GitHub: **Settings → Developer settings → Personal access tokens →
   Fine-grained tokens → Generate new token**.
   - *Repository access*: solo este repositorio.
   - *Permissions → Repository permissions → Contents*: **Read and write**.
2. En `admin.html`, tarjeta **Publicar en GitHub**: escriba el repositorio
   (`usuario/repositorio`), la rama, la ruta (`dataset.json`) y pegue el token.
3. **Probar conexión** y luego **Guardar conexión**.

Actualización mensual, en tres pasos:

1. Cargue el nuevo `.xlsx` en el panel administrativo.
2. Revise la verificación de la carga y ajuste cuotas si cambiaron.
3. Pulse **Publicar ventas y maestro**. GitHub genera el commit y GitHub Pages
   republica el sitio en menos de un minuto.

Las páginas leen primero el dataset.json del repositorio y usan la copia del navegador solo como respaldo
y siempre muestra el más reciente, indicándolo en la cinta superior.

Si prefiere no usar token: **Descargar dataset.json**, reemplazar el del repositorio
y hacer `git commit` + `git push`. El resultado es el mismo.

**Sobre el token**: se guarda solo en el navegador de quien lo escribe, nunca se
incluye en los archivos ni viaja a las páginas públicas, y puede revocarse desde GitHub en
cualquier momento. El botón **Olvidar token** lo borra de ese equipo. Si el
repositorio es público, el `dataset.json` publicado también lo será: para datos
comerciales sensibles use un repositorio privado.

---

## Reglas de cálculo aplicadas

- **Activación**: cliente con venta mayor a cero en la categoría, dividido entre el maestro
  que le corresponde: 1.297 clientes para chocolates y galletas (Confites), 1.028 para el resto.
- **Categorías del paso 1** (columna `DescrSubCategoría`): CALDOS, CHOCOLATES, CERELAC,
  LA CAMPESINA y LECHE CONDENSADA. El resto se omite en ese bloque.
- **Paso 2**: todas las subcategorías del archivo, contrastadas con los targets vigentes.
- **Proyección**: kilos y venta del período × (días hábiles del mes ÷ días hábiles transcurridos).
- **Avance en kilos**: se mide por categoría contra su cuota; el total del foco es la suma de las cinco.
- **Clientes faltantes**: target × universo − clientes ya activados.

### Targets de activación

| Categoría | Target | Categoría | Target |
|---|---|---|---|
| CALDOS | 75% | NESTEA | 25% |
| SOPAS | 75% | NESTUM | 30% |
| CHOCOLATES | 85% | LA CAMPESINA | 20% |
| GALLETAS | 70% | NUTRIRINDE | 20% |
| CERELAC | 40% | LECHE CONDENSADA | 20% |
| FORMULAS INFANTILES | 0% | | |

### Columnas que lee del Excel

`DescrSubCategoría`, `FechaFactura`, `CódigoCliente`, `DescZona`, `NombreVend`,
`Kilos`, `Cantidad`, `PrecioTotal`. Si alguna falta, el panel administrativo lo informa
en el registro de carga.

---

Venejugos C.A. · Ventas 0412 501-6394 · @Venejugos
