# Tablero de cumplimiento de KPI Nestlé · Venejugos

Dashboard interactivo estilo Power BI para la evaluación de los KPI entregables de cumplimiento
Nestlé Venezuela, presentado por **Venejugos** en su condición de aliado comercial.

Dos páginas HTML autocontenidas: no requieren servidor, ni instalación, ni conexión a internet
(Chart.js y SheetJS van incrustados dentro de cada archivo).

| Archivo | Para qué sirve |
|---|---|
| `index.html` | Panel visual. Es el tablero que se presenta y se imprime. |
| `admin.html` | Panel administrativo. Llave de seguridad, carga del Excel y cuotas. |
| `performance.html` | Performance vendedores: activación por supervisor y vendedor. |
| `dataset.json` | Datos del último reporte procesado. Opcional. |

---

## 1. Panel administrativo (`admin.html`)

1. Abra `admin.html`.
2. Introduzca la llave de seguridad: **DIGIMARKET2026**
3. Cargue el archivo `.xlsx` del Reporte General (botón o arrastrando el archivo).
4. Defina los parámetros y pulse **Guardar parámetros**:
   - **Cuota de kilos por categoría**: Caldos 3.706, Chocolates 3.812, Cerelac 1.311,
     La Campesina 789 y Leche Condensada 350 kg. Total 9.968 kg.
   - **Cuota de venta (US$)**: objetivo en valor.
   - **Maestro de clientes general**: 1.028 clientes. Base de activación de todas
     las categorías salvo Confites.
   - **Maestro Confites**: 1.297 clientes. Aplica a chocolates y galletas.
5. Pulse **Abrir panel visual**. El tablero ya muestra los datos nuevos.

El archivo procesado queda guardado en el navegador, así que el panel visual lo toma
automáticamente en ese mismo equipo. Para que todo el equipo lo vea, use
**Descargar dataset.json** y publique ese archivo en el repositorio (ver punto 3).

La llave se valida en el navegador: protege el uso del panel, no el contenido del archivo.
Para control de acceso real, publique en un repositorio privado o detrás de autenticación
del servidor.

## 2. Panel visual (`index.html`)

- Segmentadores de **zona o ruta** y **vendedor** en la cinta superior.
- Las cuotas pueden ajustarse en caliente para simular escenarios.
- **Ver resumen** abre el análisis descriptivo en cuadro de diálogo.
- **Imprimir o guardar en PDF** genera el entregable en A4 horizontal, sin los controles.

Orden de prioridad de los datos: lo cargado desde el panel administrativo, luego
`dataset.json` del repositorio, y en su defecto el archivo base incorporado.

## 3. Performance vendedores (`performance.html`)

Se abre desde el botón **Performance vendedores** del panel visual o del administrativo,
y toma los mismos datos, sin carga aparte.

- Una tarjeta por supervisor con su dona de cumplimiento y el marcador **meta / activados**.
- Dentro de cada tarjeta, el equipo de vendedores ordenado por cumplimiento; los que están
  por debajo de 70% quedan resaltados en rojo.
- Selectores de **categoría de activación** (las once de la tabla Nestlé más la vista
  general), de **vendedor** para aislar a una persona, y de **medida**: cumplimiento de la
  meta o su inverso, la brecha pendiente.
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
El tablero queda disponible en `https://USUARIO.github.io/REPOSITORIO/`
y el panel administrativo en `.../admin.html`.

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
3. Pulse **Publicar dataset.json**. GitHub genera el commit y GitHub Pages
   republica el sitio en menos de un minuto.

El panel visual compara la fecha del archivo del repositorio con la del navegador
y siempre muestra el más reciente, indicándolo en la cinta superior.

Si prefiere no usar token: **Descargar dataset.json**, reemplazar el del repositorio
y hacer `git commit` + `git push`. El resultado es el mismo.

**Sobre el token**: se guarda solo en el navegador de quien lo escribe, nunca se
incluye en los archivos ni viaja al panel visual, y puede revocarse desde GitHub en
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
