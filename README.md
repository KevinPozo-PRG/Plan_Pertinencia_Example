# Sistema Automatizado de Estudios de Pertinencia Curricular (CES / CACES)

Este repositorio alberga la plataforma de diseño, automatización y visualización interactiva de **Estudios de Pertinencia Curricular para Educación Superior en el Ecuador**, estructurados en estricto cumplimiento con el Reglamento de Régimen Académico del Consejo de Educación Superior (CES) y la Guía Metodológica del Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES).

El proyecto integra bases de datos oficiales del Estado ecuatoriano, modelos econométricos y demográficos de demanda, directrices de redacción académica institucional y visualizaciones interactivas en formato HTML tipo Microsoft Word con soporte de exportación a PDF.

---

## 1. Documentos Generados y Despliegue en Línea

Los estudios de pertinencia compilados se encuentran disponibles tanto en el repositorio como desplegados para su consulta interactiva en la web:

| Carrera / Proyecto | Institución | Formato Web | Despliegue en Línea |
| :--- | :--- | :--- | :--- |
| **Técnico Superior en Barismo y Gestión de Cafeterías** | IAVQ | [Ver HTML](dossier_barismo_iavq_vista_word.html) | [Enlace Vercel](https://planpertinenciasexample.vercel.app/dossier_barismo_iavq_vista_word) |
| **Tecnólogo Superior en Mecánica de Motos** | IAVQ | [Ver HTML](dossier_mecanica_motos_vista_word.html) | [Enlace Vercel](https://planpertinenciasexample.vercel.app/dossier_mecanica_motos_vista_word) |

> **Nota de Impresión:** Ambos dossiers cuentan con estilos de impresión optimizados (`@media print`). Al pulsar el botón superior **"Imprimir / Guardar como PDF"**, el navegador genera un documento formal de 24 páginas en tamaño carta sin cortes de tabla ni distorsiones.

---

## 2. Centro de Recursos para Analistas y Configuración de Asistentes: Directorio `guia_bot_pertinencia/`

Para los analistas de datos, planificadores curriculares y equipos de desarrollo que deseen replicar esta metodología, configurar sus propios asistentes de Inteligencia Artificial o formular nuevas carreras, toda la documentación técnica y el código fuente se encuentran centralizados en el directorio **[`guia_bot_pertinencia/`](guia_bot_pertinencia/)**:

```text
guia_bot_pertinencia/
│
├── README.md                       # Resumen ejecutivo, avances y guía de configuración general
├── CONFIGURACION_BOTS_IA.md        # Guía paso a paso para configurar ChatGPT, Claude, Gemini y Antigravity
├── GUIA_METODOLOGICA_ANALISTAS.md  # Manual metodológico: 7 bases de datos, periodos, fórmulas y taxonomías
│
└── scripts/                        # Suite modular en Python para procesar datos, ensamblar y auditar
    ├── config_parametros.py        # Diccionario central de parámetros de la carrera y territorio
    ├── procesador_datos_crudos.py  # Algoritmos de extracción y filtrado de microdatos oficiales
    ├── modulo_1_social_economico.py # Generador de Páginas 1 a 8 (Diagnóstico Social y Económico)
    ├── modulo_2_academico_planificacion.py # Generador de Páginas 9 a 16 (Académico y Articulación PND)
    ├── modulo_3_mercado_demanda.py # Generador de Páginas 17 a 24 (Mercado, Malla y Conclusiones)
    ├── ensamblador_dossier_html.py # Compilador del documento HTML interactivo con gráficos Chart.js
    └── auditor_dossier.py          # Script de auditoría automática de cumplimiento normativo CACES
```

---

## 3. Acceso Rápido a las Guías Técnicas

1. **[Guía de Configuración de Asistentes de IA (CONFIGURACION_BOTS_IA.md)](guia_bot_pertinencia/CONFIGURACION_BOTS_IA.md):**
   * **Insumos necesarios:** Los 6 documentos y datos específicos que debe recibir el asistente para formular una carrera (Ficha curricular, datos agregados REEM/SUPERCIAS, catálogo SNIESE, serie AMIE, encuestas tabuladas y metas PND/PMDOT).
   * **Recomendaciones de datos:** Por qué no deben subirse archivos crudos gigantes a las ventanas de chat y cómo preparar resúmenes estructurados.
   * **Prompt Maestro del Sistema:** Texto listo para copiar y pegar en las instrucciones de cualquier modelo de lenguaje para garantizar redacción en tercera persona y política de cero datos inventados.
   * **Configuración por plataforma:** Instrucciones detalladas para **ChatGPT (Custom GPTs)**, **Claude (Claude Projects)**, **Google Gemini (Gems)** y **Google Antigravity (AGY)**.

2. **[Manual Metodológico para Analistas de Datos (GUIA_METODOLOGICA_ANALISTAS.md)](guia_bot_pertinencia/GUIA_METODOLOGICA_ANALISTAS.md):**
   * Inventario de las 7 bases oficiales del Ecuador (INEC Proyecciones 2020–2035, ENEMDU 2025, REEM 2012–2024, SUPERCIAS 2026, SNIESE 2026, SENESCYT 2012–2024, AMIE MINEDUC 2009–2026).
   * Estandarización bajo taxonomías UNESCO CINE-F 2013, CIIU Rev. 4, CIUO-08 y DPA INEC.
   * Fórmulas matemáticas de muestreo de Cochran, factor de expansión muestral, cálculo de brecha laboral neta y proyección de demanda estudiantil con tasas demográficas del INEC.

3. **[Suite de Scripts de Procesamiento y Automatización (`guia_bot_pertinencia/scripts/`)](guia_bot_pertinencia/scripts/):**
   * Código en Python que permite cambiar los parámetros de una carrera en un único archivo de configuración (`config_parametros.py`) y generar el documento completo auditado en segundos.

---

## 4. Estándar de Extensión y Capacidad Documental

* **Extensión Actual:** 24 páginas completas estructuradas según los 8 apartados canónicos del CES/CACES.
* **Ampliación a 32 Páginas:** El sistema no tiene un límite fijo de 24 o 25 páginas. Para trámites institucionales que requieran 32 páginas, el sistema contempla la adición de 4 módulos específicos: desglose analítico de asignaturas (págs. 23-24), fichas de laboratorios y capacidad instalada (págs. 25-26), presupuesto quinquenal de sostenibilidad financiera (págs. 27-28) y anexos metodológicos de campo (págs. 29-30).

---

## 5. Instrucciones de Uso Rápido

Para compilar y verificar el dossier desde la terminal:

```bash
# 1. Ingresar al directorio de scripts
cd guia_bot_pertinencia/scripts

# 2. Compilar el dossier en formato HTML interactivo
python ensamblador_dossier_html.py

# 3. Ejecutar la auditoría automática CACES
python auditor_dossier.py
```

Al finalizar, abra el archivo generado en su navegador preferido para consultar el estudio interactivo o exportarlo directamente a formato PDF.
