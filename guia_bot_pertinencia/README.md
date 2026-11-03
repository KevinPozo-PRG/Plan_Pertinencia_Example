# Repositorio y Guía del Asistente de Pertinencia Curricular (CES / CACES)

Este directorio contiene la documentación metodológica, el inventario de bases de datos oficiales, las fórmulas estadísticas y los scripts modulares en Python desarrollados para automatizar la formulación de **Estudios de Pertinencia Curricular de Educación Superior** bajo los estándares del Consejo de Educación Superior (CES) y el Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES).

El contenido de esta carpeta está organizado para responder tanto a la gestión directiva como al trabajo técnico de los **analistas de datos y planificadores curriculares**.

---

## 1. Estructura de este Directorio

```text
guia_bot_pertinencia/
│
├── README.md                       # Resumen ejecutivo, avances y guía de configuración general
├── CONFIGURACION_BOTS_IA.md        # Manual de configuración para ChatGPT, Claude, Gemini y Antigravity
├── GUIA_METODOLOGICA_ANALISTAS.md  # Manual técnico para analistas: bases de datos, fórmulas y taxonomías
│
├── datos_extraidos/                # Repositorio de resúmenes JSON generados por la minería de datos
│   ├── indice_datos_mineria.json   # Índice y metadatos de ejecución del pipeline
│   ├── supercias_consolidado.json  # Top 15 empleadores, balances y ventas SUPERCIAS
│   ├── enemdu_consolidado.json     # Salarios ponderados, informalidad IESS y déficit formativo
│   ├── senescyt_titulados_consolidado.json # Conteo de títulos nacionales/provinciales y alerta de vacancia
│   ├── amie_bachilleres_consolidado.json   # Serie histórica de 3ro de bachillerato (N = 41.728)
│   ├── reem_empresas_consolidado.json      # Universo empresarial formal (N = 16.673)
│   └── mercado_demanda_consolidado.json    # Muestreo Cochran, brecha laboral y proyección quinquenal
│
└── scripts/                        # Suite de minería, generación y auditoría en Python
    ├── mineria/                    # SCRIPTS DE MINERÍA DE BASES DE DATOS OFICIALES
    │   ├── mineria_supercias.py    # Extracción de directorios y ranking de balances SUPERCIAS
    │   ├── mineria_enemdu.py       # Procesamiento econométrico de microdatos de la ENEMDU
    │   ├── mineria_senescyt.py     # Minería de catálogo SNIESE y graduados históricos
    │   ├── mineria_mineduc_amie.py # Streaming y consolidación de matrículas de bachillerato
    │   ├── mineria_reem_sri.py     # Agregación de empresas formales y plazas de trabajo
    │   ├── mineria_encuestas.py    # Derivación cuantitativa de brecha laboral y proyección INEC
    │   └── orquestador_mineria.py  # Ejecutor maestro de toda la fase de minería de datos
    │
    ├── config_parametros.py        # Diccionario central de parámetros configurables
    ├── modulo_1_social_economico.py # Generador de Páginas 1 a 8 (Social y Económico)
    ├── modulo_2_academico_planificacion.py # Generador de Páginas 9 a 16 (Académico y Planificación)
    ├── modulo_3_mercado_demanda.py # Generador de Páginas 17 a 24 (Mercado, Malla y Conclusiones)
    ├── ensamblador_dossier_html.py # Ensamblador del HTML interactivo tipo Word con Chart.js
    └── auditor_dossier.py          # Script de auditoría de calidad y validación de estándares CACES
```

---

## 2. Documentos Disponibles

1. **[CONFIGURACION_BOTS_IA.md](CONFIGURACION_BOTS_IA.md):**
   Manual de configuración para asistentes de Inteligencia Artificial. Explica:
   * La arquitectura de trabajo en dos niveles (procesamiento numérico por scripts vs. redacción académica por IA).
   * Los 6 insumos exactos que debe recibir el asistente (ficha curricular, datos REEM/SUPERCIAS, catálogo SNIESE, serie AMIE, encuestas tabuladas y metas PND/PMDOT).
   * La Instrucción Maestra del Sistema (Prompt Base) lista para copiar y pegar.
   * Pasos de configuración para ChatGPT (Custom GPT), Claude (Claude Projects), Google Gemini (Gems) y Google Antigravity (AGY).

2. **[GUIA_METODOLOGICA_ANALISTAS.md](GUIA_METODOLOGICA_ANALISTAS.md):** 
   Manual técnico detallado dirigido a analistas de datos. Explica a fondo:
   * El inventario de las 7 bases de datos oficiales utilizadas (INEC Proyecciones 2020–2035, ENEMDU 2025, REEM 2012–2024, SUPERCIAS 2026, SNIESE 2026, SENESCYT 2012–2024, AMIE MINEDUC 2009–2026).
   * Los periodos de corte y las variables específicas extraídas.
   * Los 4 sistemas taxonómicos de estandarización oficial (UNESCO CINE-F 2013, CIIU Rev. 4, CIUO-08 y DPA INEC).
   * El desarrollo matemático de las fórmulas: Muestreo de Cochran, Factor de Expansión muestral, Derivación cuantitativa de demanda y brecha laboral, y Proyección quinquenal de matrícula con tasas demográficas del INEC.

3. **Suite de Scripts Modulares en Python (`scripts/`):**
   Código fuente para procesar microdatos, generar los bloques de contenido del dossier, ensamblar el documento final con gráficos Chart.js y auditar el cumplimiento normativo.

---

## 3. Resumen Ejecutivo del Avance y Resoluciones

En esta etapa del proyecto se consolidaron los siguientes resultados técnicos y metodológicos:

* **Cero Datos Inventados:** Los cálculos se alimentan exclusivamente de fuentes oficiales depuradas y reproducibles.
* **Titulados Tecnológicos Nacionales:** Se reflejan los **6.184 titulados tecnológicos en Gastronomía a nivel nacional** (4.110 en Pichincha) y la vacancia absoluta (0 títulos) en Barismo.
* **Aclaración Conceptual:** Se explica formalmente que Gastronomía es el área afín macro de referencia y que la carrera de Barismo es una titulación nueva sin oferta histórica previa.
* **Serie Histórica AMIE Sincronizada:** Registro continuo de bachilleres en Quito desde 48.615 (pico COVID 2020–2021) hasta la estabilización en 41.728 estudiantes en el ciclo 2025–2026.
* **Demanda Laboral Cuantitativa:** Se incorporó la pregunta de intención de contratación a 3 años ($n = 380$ empresas) expandida a las 16.673 empresas del REEM, calculando 600 plazas anuales y una brecha neta insatisfecha de 285 a 364 puestos técnicos al año (plena absorción de los 60 a 90 graduados anuales del IAVQ con 100% de empleabilidad).
* **Demanda Estudiantil Quinquenal:** Se eliminó el multiplicador referencial del 1% y se aplicó la tasa muestral de alta probabilidad de matrícula (1,84%) con las tasas demográficas oficiales del INEC para Quito (proyectando entre 768 y 786 aspirantes anuales frente a 70 cupos planificados).
* **Alineación con Metas Cuantificadas del PND:** Políticas 2.1, 2.3, 4.1, 4.3, 5.2 y 5.4 con sus metas numéricas oficiales al 2029.
* **PMDOT con Horizonte 2033:** Vigencia territorial oficial conforme a la Ordenanza Metropolitana No. 004-2024.
* **Visualización y PDF:** Formato interactivo tipo Word en HTML/CSS, gráficos dinámicos con Chart.js y sistema de impresión directa a PDF de 24 páginas limpias desde el navegador.

---

## 4. Guía Práctica: Cómo Configurar el Asistente para Nuevos Proyectos

Para formular una nueva carrera técnica o tecnológica en cualquier cantón:

### Paso 1: Definir la Ficha Inicial de la Carrera
Identificar los cuatro metadatos base:
1. **Carrera y Título:** Ejemplo: Técnico Superior en Mecánica de Motos / Barismo / Ciberseguridad.
2. **Campo CINE-UNESCO:** Campo amplio, específico y detallado.
3. **Actividad Económica CIIU:** Rama productiva vinculada (Sección y División).
4. **Cantón y Provincia de Ejecución:** Define los filtros de población, bachilleres y empresas.

### Paso 2: Configuración de Parámetros en Python
Abrir el archivo `scripts/config_parametros.py` y actualizar el diccionario `CONFIG` con las variables del nuevo proyecto.

### Paso 3: Flujo de Ejecución y Auditoría
1. Ubicarse en el directorio de scripts:
   ```bash
   cd guia_bot_pertinencia/scripts
   ```
2. Ejecutar el ensamblador para compilar el dossier HTML:
   ```bash
   python ensamblador_dossier_html.py
   ```
3. Ejecutar la auditoría automática para verificar que cumpla todas las reglas del CACES:
   ```bash
   python auditor_dossier.py
   ```
4. Abrir el archivo generado en el navegador web para visualizar el documento o generar el PDF oficial mediante el botón superior **"Imprimir / PDF"**.

---

## 5. Preguntas Frecuentes: Extensión de Hojas (¿24 vs. 32 Páginas?)

### ¿Existe un límite de 24 o 25 páginas en el documento?
No. El límite de 24 páginas fue únicamente el parámetro de diseño acordado para el primer dossier ejecutivo condensado. La estructura modular del sistema permite extender el estudio a **32, 40 o más páginas** de acuerdo con los requerimientos institucionales o del CES.

Para alcanzar una extensión de **32 páginas**, se recomienda incorporar los siguientes contenidos complementarios:
1. **Desglose Curricular Analítico (2 páginas adicionales):** Descripción detallada de resultados de aprendizaje, contenidos mínimos y competencias por cada asignatura de los 4 periodos ordinarios.
2. **Capacidad Instalada y Laboratorios (2 páginas adicionales):** Fichas técnicas de infraestructura, equipamiento especializado, talleres de simulación práctica y especificaciones del entorno virtual de aprendizaje (plataforma LMS).
3. **Sostenibilidad Financiera y Presupuesto Quinquenal (2 páginas adicionales):** Proyección de ingresos por aranceles frente a costos directos de docencia, mantenimiento y reposición de maquinaria a cinco años.
4. **Anexos Metodológicos de Campo (2 páginas adicionales):** Cuestionarios completos y ficha técnica de los instrumentos aplicados a empleadores y bachilleres.
