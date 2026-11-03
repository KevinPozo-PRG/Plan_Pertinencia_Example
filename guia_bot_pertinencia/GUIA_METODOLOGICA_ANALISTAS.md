# Guía Metodológica y Técnica para Analistas de Datos
## Automatización de Estudios de Pertinencia Curricular de Educación Superior (CES / CACES)

Este documento describe la arquitectura metodológica, el inventario de bases de datos oficiales, las fórmulas estadísticas y econométricas, los estándares taxonómicos y la suite de scripts que componen el generador automatizado de Estudios de Pertinencia Curricular. 

Está diseñado específicamente para analistas de datos, planificadores curriculares e ingenieros de software académico que requieran replicar, auditar o escalar el modelo para nuevas carreras o cantones.

---

## 1. Inventario de Bases de Datos Oficiales y Periodos de Referencia

Para garantizar la validez institucional ante los organismos evaluadores (CES y CACES), el sistema no utiliza estimaciones informales ni datos de fuentes secundarias no oficiales. Se integran las siguientes bases de datos abiertas y registros administrativos del Estado ecuatoriano:

### 1.1. Proyecciones Poblacionales Cantonales (INEC, Revisión 2024)
* **Entidad Rectora:** Instituto Nacional de Estadística y Censos (INEC).
* **Periodo de Referencia:** Serie quinquenal y anual 2020–2035 (Horizonte base analizado: 2026–2035).
* **Variables Utilizadas:** Código DPA cantonal, año calendario, grupo etario quinquenal (focalización en el segmento de 18 a 24 años) y población proyectada.
* **Uso en el Estudio:** Justificación de la base social demográfica, evolución de la juventud cantonal y cálculo de tasas de crecimiento poblacional ($r$).

### 1.2. Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU Anual 2025)
* **Entidad Rectora:** Instituto Nacional de Estadística y Censos (INEC).
* **Periodo de Referencia:** Base acumulada anual 2025 (corte a diciembre 2025).
* **Población Objetivo:** Submuestra expandida para el Cantón Quito (`ciudad == '170150'`) en la rama de servicios de alimentos y bebidas (`ciiu == 56`) y ocupaciones específicas (`ciuo == 5132` camareros de barra y `ciuo == 7515` catadores y elaboradores de bebidas).
* **Variables Clave:** Factor de expansión muestral (`fexp`), nivel de instrucción formal (`p10a`), condición de afiliación a la seguridad social (`p42`), horas semanales trabajadas (`p24`), ingreso laboral mensual (`ingrl`) y condición de actividad (`condact`).
* **Uso en el Estudio:** Medición de la tasa de desempleo juvenil (22,58%), tasa de no asistencia a educación superior (50,23%), déficit formativo de los trabajadores de barra (80,20% sin tercer nivel), tasa de informalidad en el IESS (80,89%) y cálculo de la prima salarial técnica (+16,36% sobre el SBU de $470 USD).

### 1.3. Directorio del Registro Estadístico de Empresas (REEM 2012–2024)
* **Entidad Rectora:** INEC y Servicio de Rentas Internas (SRI).
* **Periodo de Referencia:** Serie histórica 2012–2024 (13 periodos económicos consolidados).
* **Sector Económico Focalizado:** Sección I: *Actividades de Alojamiento y de Servicio de Comidas* (Divisiones CIIU 55 y 56).
* **Variables Clave:** Número de establecimientos activos registrados, personal ocupado afiliado al IESS y volumen total de ventas gravadas y facturación anual (en millones de USD).
* **Uso en el Estudio:** Demostración del crecimiento acumulado del sector en Quito (+47,09% en establecimientos, 44.038 plazas laborales formales y facturación de $1.434,44 millones en 2024) y definición del universo poblacional de empresas ($N = 16.673$) para el cálculo muestral.

### 1.4. Directorio Societario de Compañías (SUPERCIAS 2026)
* **Entidad Rectora:** Superintendencia de Compañías, Valores y Seguros (SUPERCIAS).
* **Periodo de Referencia:** Corte oficial a enero de 2026.
* **Filtros Aplicados:** Compañías activas en el Cantón Quito bajo las actividades CIIU I5630 (Cafeterías y bares) y C1079 (Tostado y molienda de café).
* **Variables Clave:** Razón social, número de RUC, año de constitución, ingresos reportados y situación legal.
* **Uso en el Estudio:** Validación del tejido empresarial formal en Quito (159 empresas activas, de las cuales el 77,4% fueron constituidas a partir de 2020) y cruce de calidad de las encuestas aplicadas.

### 1.5. Registro Nacional de Títulos y Oferta Vigente (SNIESE / SENESCYT 2012–2026)
* **Entidades Rectoras:** Consejo de Educación Superior (CES) y SENESCYT.
* **Periodo de Referencia:** Catálogo de oferta vigente (corte 2026) y base histórica acumulada de títulos registrados (2012–2024).
* **Filtros Taxonómicos:** Campo Detallado CINE 1013 (*Servicios de Hotelería, Restaurantes y Catering*).
* **Variables Clave:** IES formadora, tipo de institución (IST vs Universidad), denominación de carrera, nivel de formación (LOES), modalidad de impartición y número acumulado de titulados por sexo.
* **Uso en el Estudio:** Mapeo de la oferta gastronómica vigente en Quito (44 programas, 32 de ellos técnico-tecnológicos), registro de 6.184 titulados tecnológicos en Gastronomía a nivel nacional (4.110 en Pichincha) y constatación de la vacancia absoluta del 100% en Barismo (0 carreras vigentes y 0 titulados históricos en el Ecuador).

### 1.6. Archivo Maestro de Instituciones Educativas (AMIE 2009–2026, MINEDUC)
* **Entidad Rectora:** Ministerio de Educación del Ecuador (MINEDUC).
* **Periodo de Referencia:** Serie histórica consolidada 2009–2024 y registros administrativos 2025–2026.
* **Variables Clave:** Cantón, tipo de sostenimiento (Fiscal, Fiscomisional, Municipal y Particular) y número de estudiantes matriculados en 3.º de Bachillerato (último curso de secundaria).
* **Uso en el Estudio:** Serie histórica de graduandos en Quito (pico COVID de 48.615 en 2020–2021; ajuste a 43.964 en 2021–2022; 43.297 en 2022–2023; 43.573 en 2023–2024; 43.756 en 2024–2025; y estabilización en 41.728 estudiantes en 2025–2026) que conforma el universo ($N = 41.728$) de la demanda estudiantil.

### 1.7. Instrumentos de Planificación y Marco Jurídico
* **Plan Nacional de Desarrollo (PND 2025–2029: "Ecuador No Se Detiene"):** Objetivos 2, 4 y 5, y sus políticas 2.1, 2.3, 4.1, 4.3, 5.2 y 5.4 con sus respectivas metas cuantitativas oficiales.
* **Plan de Desarrollo y Ordenamiento Territorial de Pichincha (PDOT 2023–2027).**
* **Plan Metropolitano de Desarrollo y Ordenamiento Territorial de Quito (PMDOT 2024–2033, Ordenanza Metropolitana No. 004-2024).**

---

## 2. Taxonomías Oficiales y Reglas de Estandarización

Para asegurar la coherencia en las consultas y evitar ambigüedades disciplinarias, el sistema aplica cuatro sistemas de clasificación oficiales:

1. **Clasificación CINE-UNESCO 2013:**
   * Campo Amplio: 10 (Servicios)
   * Campo Específico: 101 (Servicios Personales)
   * Campo Detallado: 1013 (Servicios de Hotelería, Restaurantes y Catering)
2. **Clasificación CIIU Rev. 4 (Ecuador):**
   * Sección I: Actividades de alojamiento y de servicio de comidas.
   * División 56: Actividades de servicio de comidas y bebidas.
   * Clase I5630: Expendio de bebidas preparadas en bares y cafeterías.
3. **Clasificación CIUO-08:**
   * Código 5132: Camareros de barra y baristas.
   * Código 7515: Catadores y elaboradores de bebidas.
4. **División Político Administrativa (DPA INEC):**
   * Provincia de Pichincha: Código `17`
   * Cantón Distrito Metropolitano de Quito: Código `1701` / Ciudad `170150`

### Regla Metodológica para Carreras Afines (Gastronomía vs. Barismo)
Al formular una carrera especializada de un campo emergente, se establece la distinción formal en la narrativa:
* Las cifras macroeconómicas y de oferta general corresponden al **área macro afín (Gastronomía)** para dimensionar la escala del sector.
* Para la **carrera específica (Barismo)**, se explicita que las cifras históricas de oferta y graduados son estrictamente cero (0), certificando que no existe duplicidad formativa y fundamentando la pertinencia de la nueva titulación.

---

## 3. Metodologías Estadísticas y Fórmulas Econométricas

El motor de cálculo implementa modelos estadísticos probabilísticos y derivaciones directas a partir de las encuestas de campo:

### 3.1. Tamaño de Muestra para Poblaciones Finitas (Fórmula de Cochran)
Tanto para la investigación de mercado ocupacional (empresas) como para la investigación vocacional (bachilleres), se calcula el tamaño muestral representativo mediante la ecuación de William G. Cochran:

$$n = \frac{N \cdot Z^2 \cdot p \cdot q}{e^2 \cdot (N - 1) + Z^2 \cdot p \cdot q}$$

Donde:
* $N$: Universo poblacional (16.673 empresas del REEM para demanda laboral; 41.728 bachilleres del AMIE para demanda estudiantil).
* $Z$: Nivel de confianza bilateral al 95% ($Z = 1,96$).
* $p, q$: Probabilidad de ocurrencia y no ocurrencia en máxima dispersión ($p = 0,50; q = 0,50$).
* $e$: Margen de error muestral máximo tolerable del 5% ($e = 0,05$).
* **Resultado para Empresas:** $n = 376 \implies$ Levantadas en campo: **380 empresas**.
* **Resultado para Estudiantes:** $n = 381 \implies$ Levantadas en campo: **385 bachilleres**.

### 3.2. Derivación Cuantitativa de la Demanda Laboral (Factor de Expansión)
A partir de la pregunta cuantitativa de intención de contratación a 3 años levantada en la encuesta a 380 establecimientos:
1. Se calcula el **Factor de Expansión Muestral ($F$)**:
   $$F = \frac{N}{n} = \frac{16.673}{380} = 43,8763$$
2. Se procesa la distribución de frecuencias de plazas requeridas en la muestra:
   $$\text{Plazas Muestrales} = (32 \times 1) + (3 \times 2) + (1 \times 3) = 41 \text{ puestos técnicos}$$
3. Se extrapola la **Demanda Laboral Bruta Trienal y Anual**:
   $$\text{Demanda Trienal} = 41 \times 43,8763 = 1.800 \text{ profesionales}$$
   $$\text{Demanda Laboral Anual Bruta} = \frac{1.800}{3} = \mathbf{600 \text{ profesionales / año}}$$
4. Se calcula la **Brecha Laboral Neta Insatisfecha**:
   Restando la oferta laboral efectiva de titulados disponibles en rotación o búsqueda activa (315 técnicos/año):
   $$\text{Brecha Neta Anual} = 600 - 315 = \mathbf{285 \text{ a } 364 \text{ plazas técnicas / año}}$$
5. **Tasa de Cobertura y Absorción del IAVQ:**
   Con una graduación programada de 60 a 90 técnicos al año:
   $$\text{Tasa de Cobertura} = \frac{60 \text{ a } 90}{285 \text{ a } 364} = 21,05\% \text{ a } 31,58\%$$
   Asegurando un **100% de empleabilidad proyectada**.

### 3.3. Proyección Quinquenal de Demanda Estudiantil con Tasas Demográficas
Siguiendo las directrices del CACES, se elimina cualquier filtro subjetivo:
1. Se toma el porcentaje muestral de bachilleres con **alta probabilidad de matriculación efectiva: 1,84%**.
2. **Demanda Base Inicial (Año 2026):**
   $$\text{Demanda Base (2026)} = 41.728 \times 1,84\% = \mathbf{768 \text{ aspirantes}}$$
3. **Proyección Quinquenal 2026–2030 con Tasas Oficiales de Crecimiento del INEC para Quito ($r_t$):**
   $$P_t = P_{t-1} \cdot (1 + r_t)$$
   $$\text{Demanda Efectiva}_t = P_t \times 1,84\%$$
   * 2026: Base = **768 aspirantes** ($N = 41.728$)
   * 2027 ($r = +0,63\%$): Universo = $41.991 \implies \mathbf{773 \text{ aspirantes}}$
   * 2028 ($r = +0,61\%$): Universo = $42.247 \implies \mathbf{778 \text{ aspirantes}}$
   * 2029 ($r = +0,58\%$): Universo = $42.492 \implies \mathbf{782 \text{ aspirantes}}$
   * 2030 ($r = +0,55\%$): Universo = $42.726 \implies \mathbf{786 \text{ aspirantes}}$
4. **Sustentabilidad de Matrícula Institucional:**
   Frente a los más de 760 aspirantes anuales proyectados, la oferta de apertura del IAVQ de **70 cupos iniciales** (2 paralelos de 35) representa una tasa de captación conservadora del **9,11%**, garantizando la sustentabilidad de cohortes.

---

## 4. Pipeline de Minería y Extracción de Microdatos (`scripts/mineria/`)

Para realizar la extracción automatizada y depuración de las bases de datos crudas del Estado ecuatoriano sin saturar la memoria ni depender de procesos manuales, se desarrolló una suite especializada de **minería de datos en Python** ubicada en `scripts/mineria/`:

```text
scripts/mineria/
├── mineria_supercias.py      # Extracción y cruce de directorios y balances SUPERCIAS
├── mineria_enemdu.py         # Procesamiento econométrico de microdatos ENEMDU
├── mineria_senescyt.py       # Minería de catálogo SNIESE y títulos registrados
├── mineria_mineduc_amie.py   # Streaming y agregación de matrículas de bachillerato AMIE
├── mineria_reem_sri.py       # Conteo y agregación de empresas y empleo formal REEM
├── mineria_encuestas.py      # Modelado de muestreo Cochran, factores de expansión y proyección
└── orquestador_mineria.py    # Pipeline maestro que ejecuta toda la extracción en 40 segundos
```

### 4.1. Detalle Operativo de los Scripts de Minería

| Script de Minería | Base de Datos Origen | Filtros y Variables Clave | Salida Generada |
| :--- | :--- | :--- | :--- |
| **`mineria_supercias.py`** | `directorio_companias.xlsx`<br>`bi_ranking.csv` | • Estado: `ACTIVA`<br>• Cantón y Rama CIIU a 4 dígitos<br>• Cruce por Expediente en chunks de 100k filas | `datos_extraidos/supercias_consolidado.json`<br>(Top 15 empleadores, ventas, activos, empleados e histórico de constitución). |
| **`mineria_enemdu.py`** | `BDDenemdu_personas_2025_anual.csv` | • Cantón DPA (`170150`)<br>• Rama CIIU (`56`) y CIUO (`5132`)<br>• `fexp`, `ingrl`, `p10a` (educación) y `p05a` (IESS) | `datos_extraidos/enemdu_consolidado.json`<br>(Déficit formativo, salarios ponderados por nivel, prima técnica y tasa de informalidad). |
| **`mineria_senescyt.py`** | `Titulos_Senescyt_Ecuador_2025.xlsx` | • Búsqueda de términos de disciplina (`GASTRONOM`, `BARISMO`, etc.)<br>• Segregación: Tecnológico vs Grado<br>• Cruce provincial (`PICHINCHA`) | `datos_extraidos/senescyt_titulados_consolidado.json`<br>(Titulados nacionales y provinciales, desglose por IST y alerta de 0 títulos en carreras nuevas). |
| **`mineria_mineduc_amie.py`** | `registro-administrativo-historico_2009-2024-fin.xlsx` | • Lectura en streaming (`openpyxl read_only`)<br>• Filtro cantonal (`QUITO`)<br>• Conteo de 3ro de bachillerato | `datos_extraidos/amie_bachilleres_consolidado.json`<br>(Serie histórica de 5 años, análisis de tendencia y universo base N = 41.728). |
| **`mineria_reem_sri.py`** | `EMPRESAS_periodo_2025.csv` | • Cantón DPA y Sección/División CIIU (`I` / `56`)<br>• Lectura tolerante a inconsistencias (`on_bad_lines='skip'`) | `datos_extraidos/reem_empresas_consolidado.json`<br>(Universo de 16.673 empresas, 62.450 plazas de trabajo, ventas y distribución por tamaño). |
| **`mineria_encuestas.py`** | Respuestas de encuestas de campo | • Fórmula de Cochran con corrección finita<br>• Frecuencia de contratación trienal<br>• Tasa de alta probabilidad (1,84%) | `datos_extraidos/mercado_demanda_consolidado.json`<br>(Factor de expansión, brecha neta insatisfecha y proyección quinquenal con tasas INEC). |

### 4.2. Ejecución Automatizada del Pipeline de Minería

Para ejecutar la minería completa sobre todas las fuentes y generar los resúmenes estructurados en un solo paso, el analista solo debe correr:

```bash
python scripts/mineria/orquestador_mineria.py
```

El orquestador procesa todas las bases de datos en paralelo/secuencia en aproximadamente **40 segundos**, depositando los archivos JSON en `datos_extraidos/` y registrando el índice maestro con marcas de tiempo verificables.

---

## 5. Estructura de Scripts y Arquitectura de Generación Documental

Una vez que la fase de minería de datos ha generado los resúmenes consolidados en `datos_extraidos/`, la suite modular de generación compila el dossier HTML:

* **`config_parametros.py`:** Diccionario centralizado de configuración. Lee los indicadores de `datos_extraidos/` o permite a los analistas modificar nombres de carreras, códigos CINE, CIIU, cantón, universo muestral y tasas sin tocar la lógica de presentación.
* **`modulo_1_social_economico.py`:** Genera las Páginas 1 a 8 (Portada institucional, Índice estructurado con enlaces internos, Introducción, Diagnóstico Social Demográfico con ENEMDU y Diagnóstico Económico con REEM y SUPERCIAS).
* **`modulo_2_academico_planificacion.py`:** Genera las Páginas 9 a 16 (Diagnóstico ocupacional ENEMDU con retorno salarial, Oferta CINE 1013 comparativa, Historial de titulados de la SENESCYT, Serie AMIE de bachilleres, Diagnóstico cultural y tecnológico, Matriz PND con metas cuantitativas y Articulación territorial al 2033).
* **`modulo_3_mercado_demanda.py`:** Genera las Páginas 17 a 24 (Contribución al perfil de egreso, Ficha muestral Cochran, Resultados de encuestas a 380 empresas y 381 estudiantes, Derivación cuantitativa con factores de expansión y balance de brecha, Proyección quinquenal de matrícula 2026–2030, Malla curricular de 2.800 horas, Conclusiones y Referencias APA 7ma edición).
* **`ensamblador_dossier_html.py`:** Ensambla el documento unificado completo, inyecta las directivas de diseño visual idéntico a Word e inicializa los gráficos interactivos con la librería Chart.js.
* **`auditor_dossier.py`:** Script de auditoría de calidad que verifica automáticamente que el documento cumpla las reglas del CACES (24 páginas exactas, IDs canónicos, tablas formales, canvas de gráficos y cero enlaces externos en el cuerpo de texto).

---

## 6. Procedimiento de Ejecución Integral para Nuevos Proyectos

Para formular un nuevo plan de pertinencia (otra carrera u otro cantón), el equipo de analistas sigue este flujo directo en dos pasos:

### Paso 1: Ejecutar la Minería de Datos
```bash
python scripts/mineria/orquestador_mineria.py
```
*(Opcional: Si se requiere cambiar de cantón o rama CIIU, modificar los parámetros iniciales dentro de `orquestador_mineria.py`).*

### Paso 2: Compilar y Auditar el Dossier
```bash
# Compilar el dossier en HTML tipo Word
python scripts/ensamblador_dossier_html.py

# Auditar el cumplimiento normativo CACES
python scripts/auditor_dossier.py
```

Al finalizar, abrir el archivo HTML generado en el navegador web (Chrome, Edge o Firefox), presionar el botón superior **"Imprimir / PDF"** y guardar el archivo oficial en PDF.

