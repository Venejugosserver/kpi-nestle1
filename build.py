# -*- coding: utf-8 -*-
"""Genera admin.html, performance.html e index.html a partir de src/app.html."""
import io, re, os

src = io.open('src/app.html', encoding='utf-8').read()

TAB_ADMIN = '    <button class="tab" data-view="admin">Panel Administrativo</button>\n'
assert TAB_ADMIN in src

# ---------- ADMIN ----------
admin = src
admin = admin.replace('<title>Venejugos | Dashboard KPI Nestlé</title>',
                      '<title>Venejugos | Panel Administrativo</title>')
admin = admin.replace('var CLAVE = "DIGIMARKET2026";',
                      'var CLAVE = "DIGIMARKET2026";\nvar MODO = "admin";')
admin = admin.replace('  try{ cargaSnap(); }catch(e){ console.warn("No se pudieron cargar los datos publicados:",e); }\n  badge();',
                      '  try{ cargaSnap(); }catch(e){ console.warn("No se pudieron cargar los datos publicados:",e); }\n  badge();\n  pedirClave();')
admin = admin.replace('<button class="btn btn-ghost btn-full" id="btnCancelLogin" style="margin-top:9px">Volver al panel visual</button>',
                      '<button class="btn btn-ghost btn-full" id="btnCancelLogin" style="margin-top:9px">Ver solo el panel de performance</button>')

# ---------- PERFORMANCE ----------
perf = src
perf = perf.replace('<title>Venejugos | Dashboard KPI Nestlé</title>',
                    '<title>Venejugos | Performance KPI Nestlé</title>')
perf = perf.replace('var CLAVE = "DIGIMARKET2026";', 'var CLAVE = null;   /* el acceso administrativo vive en admin.html */')
perf = perf.replace(TAB_ADMIN, '')                      # sin pestaña de administración
perf = perf.replace('<span>Dashboard de Cumplimiento y Activación de Clientes</span>',
                    '<span>Panel de Performance · Cumplimiento y Activación de Clientes</span>')
perf = perf.replace('Ingrese al Panel Administrativo, cargue el archivo de ventas y presione “Procesar y generar dashboard”.',
                    'La información se publica desde admin.html. Suba el archivo datos.js al repositorio para ver el reporte del mes.')

io.open('admin.html', 'w', encoding='utf-8').write(admin)
io.open('performance.html', 'w', encoding='utf-8').write(perf)
io.open('index.html', 'w', encoding='utf-8').write(perf)   # la raíz muestra el panel público
print('admin.html %d KB · performance.html %d KB · index.html %d KB' %
      (len(admin)//1024, len(perf)//1024, len(perf)//1024))
