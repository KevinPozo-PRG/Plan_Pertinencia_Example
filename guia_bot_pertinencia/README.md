# Guía de Avance y Configuración del Asistente Inteligente para Planes de Pertinencia

Este documento tiene como finalidad compartir con el equipo de trabajo el avance consolidado en el desarrollo de la herramienta de formulación de Estudios de Pertinencia Curricular, explicar de forma clara el proceso técnico y metodológico que se ha seguido, presentar los resultados alcanzados hasta el momento y detallar la guía paso a paso para que cualquier miembro del equipo pueda configurar y utilizar el asistente en nuevos proyectos de carreras o sedes.

---

## 1. Contexto y Objetivo del Proyecto

La elaboración de un Estudio de Pertinencia Curricular es el requisito fundamental exigido por el Consejo de Educación Superior (CES) y evaluado por el Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES) para aprobar la creación de carreras técnicas y tecnológicas en el Ecuador.

Tradicionalmente, este proceso presentaba tres desafíos importantes:
1. **Dispersión y volumen de datos:** La información requerida proviene de múltiples fuentes del Estado (INEC, SENESCYT, Ministerio de Educación, SUPERCIAS y Secretaría de Planificación), sumando gigabytes de información en formatos diversos.
2. **Tiempos prolongados de elaboración:** Analizar y cruzar manualmente estas bases de datos demandaba entre 2 y 4 meses por cada carrera.
3. **Riesgo de inconsistencias y cifras no sustentadas:** Al redactar con herramientas de inteligencia artificial convencionales sin un control estricto de datos, los modelos tienden a inventar cifras o aproximar datos demográficos, lo que genera observaciones inmediatas por parte de los organismos de control.

El objetivo de este desarrollo ha sido crear un sistema automatizado, riguroso y escalable que tome directamente las bases de datos oficiales de la institución, realice los cruces estadísticos exactos y genere un documento oficial con formato institucional tipo Word, gráficos interactivos y cálculos matemáticos transparentes.

---

## 2. Proceso Realizado: ¿Cómo se Construyó la Solución?

Para lograr un sistema fiable y sin datos inventados, el trabajo se estructuró en cuatro fases de desarrollo:

### Fase 1: Recopilación y Estandarización de Fuentes Oficiales
Se levantaron y depuraron las bases de datos oficiales del Estado ecuatoriano correspondientes al corte 2024–2026:
* **Proyecciones de Población (INEC, Revisión 2024):** Proyecciones cantonales y provinciales 2026–2035 por grupos etarios, identificando el segmento de jóvenes de 18 a 24 años.
* **Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU Anual 2025):** Microdatos procesados para medir desempleo juvenil, tasa de no asistencia a educación superior, nivel educativo del personal en barra y retorno salarial frente al Salario Básico Unificado (SBU).
* **Directorio del Registro Estadístico de Empresas (REEM 2012–2024):** Series históricas de establecimientos, empleo registrado y volumen de facturación en el sector de alimentos y bebidas (Sección I).
* **Directorio Societario (SUPERCIAS 2026):** Empresas activas constituidas en el cantón, identificando el crecimiento reciente post-2020.
* **Catálogo de Oferta y Registro de Títulos (SNIESE / SENESCYT 2012–2024):** Inventario de carreras vigentes por nivel de formación y títulos registrados a nivel nacional y provincial.
* **Archivo Maestro de Instituciones Educativas (AMIE 2020–2026, MINEDUC):** Matrícula histórica real de estudiantes en 3.º de Bachillerato en el cantón Quito.
* **Planificación Nacional y Territorial:** Objetivos, políticas y metas del Plan Nacional de Desarrollo (PND 2025–2029), PDOT de Pichincha y PMDOT de Quito (vigencia al 2033).

### Fase 2: Arquitectura en Dos Capas para Evitar la Alucinación
Para evitar que la inteligencia artificial procesara archivos gigantescos en tiempo real (lo cual suele colapsar el sistema o producir cifras aproximadas), se implementó una arquitectura en dos capas:
* **Capa 1 (Procesamiento de Datos):** Scripts que leen las bases de datos originales, aplican los filtros cantonales y disciplinarios requeridos, y generan tablas resumen consolidadas con valores matemáticos exactos.
* **Capa 2 (Generación y Redacción Académica):** El asistente recibe únicamente los datos consolidados y las directrices de redacción institucional en tercera persona, encargándose de interpretar, vincular con la normativa y redactar los capítulos sin necesidad de estimar números.

### Fase 3: Modelado Matemático de Oferta y Demanda
Se reemplazaron los supuestos referenciales por fórmulas metodológicas aprobadas por CACES:
* **Muestreo de Cochran para poblaciones finitas:** Determinación del tamaño de muestra representativa con 95% de confianza y 5% de margen de error para empresas y estudiantes.
* **Derivación de Demanda Laboral con Factor de Expansión:** A partir de la pregunta cuantitativa de intención de contratación a 3 años levantada en la encuesta muestral, se aplica el factor de expansión sobre el total de empresas del cantón para obtener los requerimientos anuales de personal y contrastarlos contra la oferta de titulados, calculando la brecha neta insatisfecha.
* **Derivación de Demanda Estudiantil con Tasas Demográficas:** Se toma el porcentaje de la muestra de bachilleres con alta probabilidad de matriculación efectiva (1,84%) sobre el universo del AMIE y se proyecta para el quinquenio 2026–2030 utilizando las tasas oficiales de crecimiento poblacional cantonal del INEC.

### Fase 4: Formato Visual Tipo Hoja de Word y Despliegue en la Nube
En lugar de generar documentos en formatos cerrados que alteran tipografías y tablas entre versiones, se desarrolló un visor en HTML/CSS estructurado como una plantilla de Microsoft Word:
* Hojas independientes con medidas de hoja carta portrait y saltos de página limpios.
* Tipografía Calibri oficial, jerarquía de encabezados, tablas formales y márgenes reglamentarios.
* Gráficos dinámicos con Chart.js sincronizados con las tablas de datos.
* Despliegue continuo en la web a través de Vercel para revisión interactiva en cualquier dispositivo.

---

## 3. Estado Actual: ¿Hasta Dónde Hemos Llegado?

A la fecha, el desarrollo cuenta con los siguientes resultados operativos y verificados:

1. **Dossier Unificado Completo de la Carrera Técnico Superior en Barismo (IAVQ):**
   * Documento estructurado con 24 páginas calibradas que abarcan la totalidad de los capítulos exigidos por el CACES (Introducción, Diagnóstico Social, Diagnóstico Económico, Diagnóstico Académico, Términos Culturales, Articulación con PND/PMDOT, Perfil de Egreso, Estudio de Mercado y Demanda, Conclusiones y Referencias).
2. **Resolución de Todas las Observaciones Metodológicas Previas:**
   * **Oferta Académica Consolidada:** Tabla comparativa por nivel de formación (Ecuador, Pichincha, Quito), aclarando que Gastronomía es el área afín de referencia y que para Barismo existe vacancia absoluta (0 oferta y 0 graduados históricos).
   * **Titulados Tecnológicos Nacionales:** Incorporación de los 6.184 titulados tecnológicos en Gastronomía a nivel nacional y 4.110 en Pichincha.
   * **Serie Oficial de Bachilleres (AMIE):** Registro histórico sin desfasajes desde el pico COVID (48.615) hasta la estabilización actual (41.728 graduandos en 2025–2026).
   * **Demanda Laboral Cuantitativa:** Frecuencias de contratación muestrales expandidas al universo de 16.673 empresas de la Sección I, determinando una demanda bruta de 600 plazas anuales y una brecha neta insatisfecha de 285 a 364 puestos técnicos al año (frente a los 60 a 90 graduados previstos por el IAVQ, fundamentando 100% de empleabilidad).
   * **Demanda Estudiantil Cuantitativa:** Proyección quinquenal 2026–2030 basada en el 1,84% de alta probabilidad de matrícula con tasas demográficas del INEC, proyectando entre 768 y 786 aspirantes anuales frente a 70 cupos ofertados (tasa de captación conservadora del 9,1%).
   * **Metas Cuantificadas del PND:** Inclusión de metas numéricas oficiales para las políticas 2.1, 2.3, 4.1, 4.3, 5.2 y 5.4.
   * **Vigencia Territorial:** Horizonte del PMDOT de Quito fijado al año 2033 (Ordenanza Metropolitana No. 004-2024).
   * **Referencias Bibliográficas:** 15 fuentes institucionales en normas APA 7ma edición con enlaces web verificados y funcionales.
3. **Plataforma y Visualización en Línea:**
   * El documento se encuentra publicado y accesible en tiempo real en la plataforma web del proyecto (Vercel).
   * Incorpora un botón superior de impresión que permite generar el PDF oficial de forma directa y limpia desde el navegador.

---

## 4. Guía Práctica: Cómo Configurar el Asistente para Nuevos Proyectos

Para que el equipo pueda utilizar este sistema en la formulación de nuevas carreras (por ejemplo, Diseño Gráfico, Mecánica, Desarrollo de Software, etc.) o en otros cantones del país, el procedimiento se divide en tres pasos sencillos:

### Paso 1: Definir los Datos Clave de la Nueva Carrera (Ficha Inicial)
Antes de interactuar con el asistente, se debe contar con cuatro datos básicos del proyecto:
1. **Nombre de la Carrera y Título que Otorga:** Ejemplo: Técnico Superior en Barismo.
2. **Campo de Educación (UNESCO CINE):** Campo amplio, específico y detallado (ejemplo: Campo 1013 - Hotelería, Restaurantes y Catering).
3. **Actividad Económica Principal (INEC CIIU):** Código de rama productiva vinculada (ejemplo: Sección I, División 56 - Alimentos y Bebidas).
4. **Cantón y Provincia de Ejecución:** Determina los filtros territoriales de población, bachilleres y empresas.

### Paso 2: Configuración del Asistente en la Plataforma de Inteligencia Artificial
En el espacio de trabajo institucional (por ejemplo, ChatGPT Business / Team o en un Custom GPT dedicado):
1. **Nombre del Asistente:** Generador de Estudios de Pertinencia Curricular (CES / CACES).
2. **Instrucciones Principales (System Prompt):**
   * Definir el rol como especialista en planificación curricular y evaluación de pertinencia conforme a la normativa del CES y CACES.
   * Establecer la regla de oro: redactar siempre en tercera persona académica y utilizar exclusivamente los datos provistos en las tablas consolidadas, sin estimar cifras poblacionales ni inventar porcentajes.
   * Indicar que cuando se mencione un área disciplinar afín (macro), se debe aclarar que sirve de marco contextual y diferenciarla de la oferta específica de la nueva carrera.
3. **Archivos de Soporte (Base de Conocimiento / Knowledge):**
   * Subir las tablas maestras consolidadas (archivos en formato Excel o JSON que contienen las proyecciones de población del cantón, la tabla consolidada de oferta académica SNIESE, la serie de graduados de secundaria AMIE y los resultados de las encuestas aplicadas).

### Paso 3: Flujo de Trabajo por Módulos (Uso Secuencial)
Para garantizar coherencia y evitar saturar la memoria del modelo, se recomienda trabajar en bloques ordenados:
* **Módulo A (Social y Demográfico):** Solicitar el análisis poblacional y los indicadores de empleo juvenil a partir de las tablas de población y ENEMDU.
* **Módulo B (Económico y Empresarial):** Solicitar el diagnóstico de empresas activas, facturación y empleo formal a partir de las tablas del REEM y SUPERCIAS.
* **Módulo C (Académico y Formativo):** Solicitar la matriz comparativa de oferta por nivel de formación y la serie de bachilleres del AMIE.
* **Módulo D (Mercado y Demanda):** Proporcionar la distribución de frecuencias de las encuestas (intención de contratación de empresas y probabilidad de matrícula de bachilleres) para que el asistente aplique el factor de expansión y derive el balance de brecha laboral y la proyección de matrícula quinquenal.
* **Módulo E (Alineación y Conclusiones):** Integrar la matriz con las políticas y metas del Plan Nacional de Desarrollo, el plan territorial local y consolidar las conclusiones en viñetas directas.

---

## 5. Preguntas Frecuentes y Próximos Pasos

### ¿Existe un límite de 24 o 25 páginas en el documento?
No. El límite de 24 páginas fue únicamente el parámetro de diseño acordado para el primer dossier ejecutivo condensado. La estructura modular del sistema permite extender el estudio a **32, 40 o más páginas** de acuerdo con las necesidades de la institución o los requerimientos de entrega ante el CES.

Para alcanzar una extensión de **32 páginas**, se recomienda incorporar los siguientes contenidos complementarios:
1. **Desglose Curricular Analítico (2 a 3 páginas adicionales):** Descripción detallada de resultados de aprendizaje, contenidos mínimos y competencias por cada asignatura de los 4 periodos ordinarios.
2. **Capacidad Instalada y Laboratorios (2 páginas adicionales):** Fichas técnicas de infraestructura, equipamiento especializado, talleres de simulación práctica y especificaciones del entorno virtual de aprendizaje (plataforma LMS).
3. **Sostenibilidad Financiera y Presupuesto Quinquenal (2 páginas adicionales):** Proyección de ingresos por aranceles frente a costos directos de docencia, mantenimiento y reposición de maquinaria a cinco años.
4. **Anexos Metodológicos de Campo (1 a 2 páginas adicionales):** Cuestionarios completos y ficha de validación de los instrumentos aplicados a empleadores y bachilleres.

### ¿Cómo proceder para probar los cambios actuales?
Los archivos del proyecto se encuentran actualizados en este repositorio. Al realizar la sincronización con el servidor de despliegue, el documento reflejará de inmediato todos los ajustes cuantitativos y de formato, quedando listo para su revisión institucional.
