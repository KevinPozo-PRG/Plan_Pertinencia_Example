# Guía de Configuración de Asistentes de IA para Estudios de Pertinencia Curricular

Este documento contiene las directrices, especificaciones técnicas y configuraciones necesarias para implementar y operar un asistente de Inteligencia Artificial (en **ChatGPT**, **Claude**, **Google Gemini** o **Google Antigravity**) especializado en la redacción, cálculo y estructuración de **Estudios de Pertinencia Curricular** bajo las normativas del Consejo de Educación Superior (CES) y el Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES) de la República del Ecuador.

---

## 1. Arquitectura de Trabajo: El Asistente de IA y los Scripts de Datos

Para garantizar que el estudio cumpla con los estándares de rigor técnico y evitar cualquier error o alteración de cifras, el sistema opera bajo una **arquitectura en dos niveles**:

1. **Nivel Determinista y Minería de Datos (Scripts en Python):**
   * Las bases de datos oficiales del Estado ecuatoriano (ENEMDU, REEM, SNIESE, AMIE, SUPERCIAS) contienen cientos de miles de registros y pesan varios gigabytes en su conjunto.
   * Ningún modelo de lenguaje comercial debe procesar microdatos crudos directamente en una ventana de chat, ya que esto provoca saturación de memoria, truncamiento de texto y aproximaciones imprecisas o alucinadas.
   * La suite de minería de datos ubicada en `scripts/mineria/` (compuesta por `mineria_supercias.py`, `mineria_enemdu.py`, `mineria_senescyt.py`, `mineria_mineduc_amie.py`, `mineria_reem_sri.py` y `mineria_encuestas.py`, coordinados por `orquestador_mineria.py`) extrae, filtra y consolida automáticamente las cifras oficiales en la carpeta `datos_extraidos/` en formato JSON en menos de 45 segundos.

2. **Nivel Cognitivo y de Redacción (Asistente de IA):**
   * El asistente de IA recibe los datos ya consolidados y procesados.
   * Su función es redactar la narrativa institucional en tercera persona, argumentar la pertinencia socioeconómica, articular los objetivos con el Plan Nacional de Desarrollo (PND) y el PMDOT cantonal, estructurar las tablas bajo formato APA 7ma edición y compilar los apartados en formato HTML paginado.

---

## 2. Documentación e Insumos que Debe Recibir el Asistente

Para formular un nuevo plan de pertinencia de cualquier carrera y en cualquier cantón del país, el asistente de IA debe recibir **exclusivamente seis insumos depurados**:

### Insumo 1: Ficha Técnica Institucional de la Carrera Propuesta
Documento breve con los metadatos institucionales:
* Nombre de la carrera y título a otorgar (ejemplo: Técnico Superior en Barismo y Gestión de Cafeterías).
* Nivel de formación: Técnico Superior (2 años, 4 periodos ordinarios, 2.800 a 3.200 horas) o Tecnológico Superior (2.5 a 3 años).
* Modalidad de impartición: Presencial, Semipresencial, Híbrida o En Línea.
* Campo de Conocimiento según CINE-UNESCO: Campo Amplio (ej. 10 Servicios), Específico (ej. 101 Servicios Personales) y Detallado (ej. 1013 Hotelería y Catering).
* Institución proponente y cantón de ejecución (ej. Instituto Superior Tecnológico de Artes Visuales de Quito - IAVQ, Cantón Quito).

### Insumo 2: Resumen Económico y Productivo Cantonal (Salida de REEM y SUPERCIAS)
Tabla o archivo JSON con los datos agregados:
* Rama de actividad económica CIIU a 4 dígitos vinculada a la carrera (ejemplo: `CIIU I5630` para servicio de bebidas).
* Número total de empresas formales registradas en el cantón/provincia según el Directorio de Empresas (REEM del INEC).
* Número de compañías activas (S.A., Cía. Ltda., S.A.S.) registradas ante la Superintendencia de Compañías (SUPERCIAS).
* Indicadores laborales del sector según ENEMDU: porcentaje de mano de obra sin título superior, tasa de informalidad (sin afiliación al IESS) y salario promedio frente al Salario Básico Unificado (SBU).

### Insumo 3: Oferta Académica Existente y Titulados (Salida de SNIESE / CES)
* Conteo de carreras vigentes en el mismo campo de conocimiento dentro del cantón o zona de influencia.
* Número histórico de titulados universitarios y tecnológicos en la disciplina afín.
* Si para la carrera específica no existen títulos otorgados previamente, se debe reportar explícitamente el valor de **cero (0)**, explicando que corresponde a una titulación emergente e innovadora sin oferta histórica directa.

### Insumo 4: Serie Histórica de Matrícula de Bachillerato (Salida de AMIE / MINEDUC)
* Registro de estudiantes matriculados en 3ro de Bachillerato del cantón en los últimos cinco periodos lectivos oficiales.
* Debe reflejar la cifra real validada del último periodo disponible (ejemplo: 41.728 estudiantes en Quito para el ciclo 2025–2026).

### Insumo 5: Tabulación de Encuestas de Campo (Muestra de Empleadores y Estudiantes)
Resultados de las preguntas cuantitativas clave:
* **Encuesta a Empleadores:** Número de empresas encuestadas ($n = 380$), porcentaje que requiere profesionales técnicos, y distribución de frecuencias de la intención de contratación a 3 años (número de plazas que prevén contratar).
* **Encuesta a Bachilleres:** Número de bachilleres encuestados ($n = 381$), porcentaje que manifiesta interés en continuar estudios superiores, y porcentaje específico con **alta probabilidad de matriculación** en la carrera propuesta (ejemplo: 1,84%).

### Insumo 6: Metas de Planificación Territorial y Nacional
* Objetivos, políticas y **metas numéricas oficiales** del Plan Nacional de Desarrollo vigente (PND 2025–2029).
* Objetivos estratégicos y año de vigencia del Plan Metropolitano de Desarrollo y Ordenamiento Territorial (PMDOT) del cantón respectivo (ejemplo: horizonte 2033 para Quito).

---

## 3. Recomendaciones Clave para el Tratamiento de Datos

1. **Política Estricta de Cero Datos Inventados:**
   Cada cifra debe originarse en un registro administrativo verificable. Si una variable no existe o no tiene registros previos (por ejemplo, titulados en una carrera inédita), el sistema debe reportar cero y explicar la razón en el texto; nunca debe aproximar valores inexistentes.

2. **No Inflar Sectores Económicos:**
   No se deben utilizar clasificaciones macro a un dígito (como el Sector G de Comercio general o Sector I de Servicios globales) para justificar carreras especializadas. Se debe utilizar la clase CIIU a cuatro dígitos que refleje con exactitud la actividad productiva.

3. **Formato Exclusivo: HTML Paginado Tipo Word:**
   El resultado final debe compilarse como un documento HTML estructurado con estilos CSS para impresión tamaño carta (`@media print`), evitando la generación directa de archivos binarios `.docx` que sobrecargan la memoria del sistema y dificultan el versionado colaborativo en Git.

4. **Redacción Académica en Tercera Persona:**
   Toda la redacción debe ser impersonal (*"se evidencia"*, *"se determina"*, *"los resultados demuestran"*). Queda prohibido el uso de primera persona plural (*"nosotros planteamos"*, *"nuestro equipo"*).

---

## 4. Instrucción Maestra del Sistema (Prompt Base para Cualquier Asistente)

Copie y pegue el siguiente texto en el apartado de instrucciones de su asistente (Custom GPT, Claude Project, Gemini Gem o System Prompt de Antigravity):

```text
Eres un Asistente Senior en Diseño Curricular y Planificación de la Educación Superior en Ecuador, especializado en la elaboración de Estudios de Pertinencia Curricular bajo las normativas del Consejo de Educación Superior (CES) y el Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES).

Tu función principal es redactar, verificar y estructurar estudios técnicos de pertinencia para la creación de carreras de tercer nivel técnico y tecnológico superior.

Reglas operativas obligatorias:
1. Voz gramatical y estilo: Redacta estrictamente en tercera persona del singular (impersonal). No uses frases autorreferenciales ("nosotros", "nuestro instituto", "hemos analizado"). Mantén un tono académico formal, objetivo y sustentado.
2. Tratamiento de datos: Jamás inventes datos ni utilices aproximaciones no verificadas. Todas las cifras deben provenir de fuentes oficiales ecuatorianas (INEC, ENEMDU, REEM, SUPERCIAS, SNIESE, AMIE, PND, PMDOT).
3. Transparencia en titulados: Si la carrera propuesta no registra graduados previos, reporta explícitamente cero (0) y redacta la aclaración conceptual indicando que se trata de una oferta académica nueva e innovadora, utilizando la disciplina macro más cercana únicamente como contexto sectorial.
4. Secuencia metodológica de presentación de datos:
   - Párrafo de contextualización e investigación previa.
   - Tabla o visualización bajo formato institucional (Título normalizado APA 7ma edición).
   - Indicación exacta de la fuente oficial con año y enlace.
   - Párrafo analítico posterior que vincule los datos con la pertinencia curricular y el perfil de egreso.
5. Mercado y demanda:
   - La demanda laboral debe derivarse de la extrapolación formal de la pregunta de intención de contratación mediante el factor de expansión muestral (Universo / Muestra).
   - La demanda estudiantil debe calcularse aplicando el porcentaje de alta probabilidad de matrícula de la encuesta sobre el universo oficial de bachilleres del último periodo lectivo, proyectándose al quinquenio con las tasas oficiales de crecimiento demográfico del cantón.
6. Alineación estratégica: Detalla las políticas públicas del PND y sus metas cuantificadas al 2029, así como las metas del PMDOT cantonal con su horizonte temporal exacto.
7. Formato de salida: Genera la estructura en bloques de contenido HTML con formato institucional tipo Microsoft Word, aptos para ser integrados en el ensamblador del dossier paginado.
```

---

## 5. Configuración Paso a Paso según la Plataforma de IA

### A. Configuración en ChatGPT (OpenAI - Custom GPT o Team Workspace)
1. Ingrese a **ChatGPT** y seleccione **Explore GPTs** -> **Create**.
2. En la pestaña **Configure**:
   * **Name:** Asistente de Pertinencia Curricular CES / CACES.
   * **Description:** Asistente especializado en la formulación y validación de estudios de pertinencia curricular para educación superior técnica y tecnológica en Ecuador.
   * **Instructions:** Pegue el texto íntegro de la *Instrucción Maestra del Sistema* (Sección 4).
   * **Capabilities:** Active **Code Interpreter** (Análisis de datos avanzado) y **Web Browsing**.
   * **Knowledge (Archivos de Conocimiento):**
     * Suba el archivo `guia_bot_pertinencia/GUIA_METODOLOGICA_ANALISTAS.md`.
     * Suba los archivos JSON o resúmenes de datos preprocesados de la carrera que vaya a formular.
     * No suba bases crudas superiores a 10 MB directamente; use los datos consolidados generados por `procesador_datos_crudos.py`.

### B. Configuración en Claude (Anthropic - Claude Projects)
1. En **Claude.ai**, cree un nuevo proyecto: **Proyecto Pertinencias CEDEPRO / IAVQ**.
2. En la sección **Project Knowledge**:
   * Adjunte `GUIA_METODOLOGICA_ANALISTAS.md` y `CONFIGURACION_BOTS_IA.md`.
   * Adjunte los esquemas de tablas y resúmenes de encuestas procesadas.
3. En la sección **Custom Instructions**:
   * Pegue la *Instrucción Maestra del Sistema* (Sección 4).
   * Añada la instrucción de emplear la herramienta de **Artifacts** para generar código HTML estructurado página por página.

### C. Configuración en Google Gemini (Google Workspace / Gemini Advanced / Gems)
1. En Gemini, acceda al gestor de **Gems** y seleccione **Nuevo Gem**.
2. **Nombre:** Gestor de Pertinencia Curricular Ecuador.
3. **Instrucciones:** Ingrese la *Instrucción Maestra del Sistema* (Sección 4).
4. Vincule las carpetas de Google Drive donde su equipo almacene las tabulaciones de encuestas y los informes demográficos cantonales para permitir la búsqueda de información con fuentes verificadas.

---

## 6. Uso y Configuración con Google Antigravity (AGY)

**Google Antigravity** es el entorno de desarrollo y ejecución de agentes autónomos recomendado para este flujo de trabajo, ya que resuelve la limitación principal de los chats tradicionales: la integración directa entre el código de procesamiento de datos y la generación de documentos.

### Ventajas de Antigravity frente a un Chat Convencional
* **Ejecución Local de Scripts:** Antigravity ejecuta directamente en su computadora los scripts de Python (`procesador_datos_crudos.py`, `ensamblador_dossier_html.py`, `auditor_dossier.py`), procesando bases de gigabytes sin restricciones de memoria ni problemas de desconexión.
* **Control de Calidad Automatizado:** Tras generar el documento, el agente ejecuta el script de auditoría (`auditor_dossier.py`) y verifica que los 8 apartados normativos cumplan con las reglas del CACES antes de entregar el resultado final.
* **Persistencia en Repositorio Git:** Trabaja de forma directa sobre la estructura de archivos del proyecto, manteniendo el historial de versiones en GitHub y permitiendo la visualización inmediata en plataformas web como Vercel.

### Cómo Configurar el Asistente en Antigravity
En Antigravity, la inteligencia y las reglas de negocio del asistente se encapsulan mediante el sistema de **Skills**.

1. **Ubicación de la Skill:**
   El proyecto cuenta con la skill especializada ubicada en:
   ```text
   .agents/skills/estudio-pertinencia/SKILL.md
   ```
2. **Activación de la Skill:**
   Al iniciar una sesión de trabajo en Antigravity dentro del espacio de trabajo del proyecto, la skill se carga automáticamente. También puede invocarse de forma explícita indicando en el prompt:
   *"Utiliza la skill de estudio-pertinencia para formular la propuesta de la carrera X en el cantón Y"*.

3. **Flujo de Trabajo Automatizado en Antigravity:**
   * **Paso 1:** Proporcionar los 6 insumos básicos al agente en el chat.
   * **Paso 2:** El agente actualiza `scripts/config_parametros.py` con los valores de la carrera y el cantón.
   * **Paso 3:** El agente corre el ensamblador para compilar el dossier HTML de 24 o 32 páginas.
   * **Paso 4:** El agente ejecuta `auditor_dossier.py` para emitir el dictamen de validación formal.
   * **Paso 5:** El usuario abre el archivo resultante en su navegador y pulsa el botón de impresión para obtener el documento oficial en PDF.

