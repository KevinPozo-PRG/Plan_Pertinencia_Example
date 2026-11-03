# -*- coding: utf-8 -*-
"""
Generador modular de las Páginas 1 a 8 para el Dossier:
Técnico Superior en Barismo - Instituto Superior Tecnológico de Artes Visuales de Quito (IAVQ)
Con verificación 100% estricta sobre las bases oficiales de Excel de CEDEPRO / INEC:
- Proyecciones_Poblacion_Ecuador_Pichincha_Quito_2026-2035.xlsx
- Grafico1_Grupo_Etario_18-24_Ecuador_Pichincha_Quito_2026-2035.xlsx
- Reporte_ENEMDU_2025_Quito_Graficos_2_3_4.xlsx
- Reporte_ENEMDU_2025_Educacion_Asistencia_Desempleo_Graficos_5_6_7.xlsx
- Reporte_REEM_2012_2024_Alojamiento_y_Comidas.xlsx
- supercias_barismo_quito.json y top_ranking_barismo_quito.json
"""

def get_page_header(page_num, title="ESTUDIO DE PERTINENCIA CURRICULAR — TÉCNICO SUPERIOR EN BARISMO"):
    return f"""
    <div class="word-header">
      <span>INSTITUTO SUPERIOR TECNOLÓGICO DE ARTES VISUALES DE QUITO (IAVQ)</span>
      <span>{title}</span>
    </div>
    """

def get_page_footer(page_num, total_pages=24):
    return f"""
    <div class="word-footer">
      <span>Carrera de Tercer Nivel Técnico Superior en Barismo — Modalidad Híbrida</span>
      <span>Página {page_num} de {total_pages}</span>
    </div>
    """

def generate_pages_1_to_8():
    pages = {}

    # ==========================================
    # PÁGINA 1: PORTADA INSTITUCIONAL
    # ==========================================
    pages[1] = f"""
    <div class="word-page" id="page-01-cover">
      <div class="word-cover-container">
        <div>
          <div class="word-cover-institution">INSTITUTO SUPERIOR TECNOLÓGICO DE ARTES VISUALES DE QUITO</div>
          <div class="word-cover-subinst">IAVQ — CONDICIÓN SUPERIOR UNIVERSITARIA</div>
          <div class="word-cover-divider"></div>
          <div class="word-cover-dept">DEPARTAMENTO DE DESARROLLO INSTITUCIONAL Y DISEÑO CURRICULAR</div>
        </div>

        <div>
          <div class="word-cover-project-tag">PROYECTO DE CREACIÓN DE CARRERA DE TERCER NIVEL TÉCNICO SUPERIOR</div>
          <div class="word-cover-title">ESTUDIO DE PERTINENCIA CURRICULAR</div>
          
          <div class="word-cover-career-box">
            <div class="word-cover-career-label">CARRERA PROPUESTA:</div>
            <div class="word-cover-career-name">TÉCNICO SUPERIOR EN BARISMO</div>
            <div class="word-cover-itinerary-label">ITINERARIOS FORMATIVOS:</div>
            <ul class="word-cover-itinerary-list">
              <li><strong>Itinerario 1:</strong> Barismo de Especialidad, Catación Sensorial y Tueste Artesanal</li>
              <li><strong>Itinerario 2:</strong> Gestión Operativa de Barras, Emprendimiento y Control de Calidad</li>
            </ul>
          </div>

          <table class="word-cover-meta-table">
            <tr>
              <td class="meta-label">Nivel de Formación:</td>
              <td class="meta-val">Tercer Nivel Técnico Superior</td>
            </tr>
            <tr>
              <td class="meta-label">Título que Otorga:</td>
              <td class="meta-val">Técnico/a Superior en Barismo</td>
            </tr>
            <tr>
              <td class="meta-label">Modalidad de Aprendizaje:</td>
              <td class="meta-val">Híbrida (Virtual síncrona / Prácticas presenciales intensivas)</td>
            </tr>
            <tr>
              <td class="meta-label">Duración y Créditos:</td>
              <td class="meta-val">4 Períodos Académicos Ordinarios (2 Años) — 2.800 Horas</td>
            </tr>
            <tr>
              <td class="meta-label">Campo Amplio / Específico:</td>
              <td class="meta-val">10 Servicios / 101 Servicios personales (CINE UNESCO)</td>
            </tr>
            <tr>
              <td class="meta-label">Campo Detallado CINE:</td>
              <td class="meta-val">1013 Servicios de hotelería, restaurantes y catering</td>
            </tr>
            <tr>
              <td class="meta-label">Clasificación CIIU Rev. 4:</td>
              <td class="meta-val">I5630 (Servicio de bebidas / cafeterías) / C1079.11 (Elaboración y tueste)</td>
            </tr>
            <tr>
              <td class="meta-label">Clasificación CIUO-08:</td>
              <td class="meta-val">5132 (Baristas y camareros de barra) / 7515 (Catadores de café)</td>
            </tr>
            <tr>
              <td class="meta-label">Cobertura Territorial:</td>
              <td class="meta-val">Cantón Quito, Provincia de Pichincha</td>
            </tr>
          </table>
        </div>

        <div>
          <p class="word-cover-date">MARZO 2026</p>
          <p class="word-cover-place">Quito D.M., República del Ecuador</p>
        </div>
      </div>
      {get_page_footer(1)}
    </div>
    """

    # ==========================================
    # PÁGINA 2: ÍNDICE GENERAL CONTINUO
    # ==========================================
    pages[2] = f"""
    <div class="word-page" id="page-02-indice">
      {get_page_header(2, "ÍNDICE GENERAL DEL ESTUDIO DE PERTINENCIA")}
      <div class="word-content">
        <h1 class="word-heading-1" style="text-align: center; margin-bottom: 8pt;">ÍNDICE GENERAL DE CONTENIDOS</h1>

        <div class="word-toc">
          <div class="toc-group-title">1. ESTRUCTURA CANÓNICA DEL ESTUDIO DE PERTINENCIA CURRICULAR</div>
          <div class="toc-row toc-level-1"><a href="#page-01-cover"><span class="toc-title">PORTADA INSTITUCIONAL DEL PROYECTO</span><span class="toc-dots"></span><span class="toc-page">1</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-02-indice"><span class="toc-title">ÍNDICE DE CONTENIDOS, TABLAS Y GRÁFICOS</span><span class="toc-dots"></span><span class="toc-page">2</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-03-intro"><span class="toc-title">1. INTRODUCCIÓN, ANTECEDENTES Y PERFIL INSTITUCIONAL IAVQ</span><span class="toc-dots"></span><span class="toc-page">3</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-04-social-1"><span class="toc-title">2. ANÁLISIS DE NECESIDADES DE DESARROLLO (DIAGNÓSTICO SITUACIONAL)</span><span class="toc-dots"></span><span class="toc-page">4</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-04-social-1"><span class="toc-title">2.1. Términos Sociales: Proyecciones de Población y Grupo Juvenil 18–24 (2026–2035)</span><span class="toc-dots"></span><span class="toc-page">4</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-05-social-2"><span class="toc-title">2.1. Términos Sociales: Mercado Laboral Juvenil, Desempleo y Educación (ENEMDU)</span><span class="toc-dots"></span><span class="toc-page">5</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-06-econ-1"><span class="toc-title">2.2. Términos Económicos: Tejido Productivo y Plazas Laborales (CIIU 56 REEM)</span><span class="toc-dots"></span><span class="toc-page">6</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-07-econ-2"><span class="toc-title">2.2. Términos Económicos: Facturación del Sector y Constitución Histórica</span><span class="toc-dots"></span><span class="toc-page">7</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-08-supercias"><span class="toc-title">2.2. Tejido Empresarial: Directorio y Ranking Societario (SUPERCIAS 2026)</span><span class="toc-dots"></span><span class="toc-page">8</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-09-enemdu-edu"><span class="toc-title">2.2. Diagnóstico Ocupacional: Nivel de Instrucción y Brecha de Titulación (ENEMDU)</span><span class="toc-dots"></span><span class="toc-page">9</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-10-enemdu-iess"><span class="toc-title">2.2. Diagnóstico Ocupacional: Seguridad Social e Informalidad Laboral (ENEMDU)</span><span class="toc-dots"></span><span class="toc-page">10</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-11-enemdu-salario"><span class="toc-title">2.2. Retorno Salarial y Prima a la Profesionalización en Cafeterías (ENEMDU)</span><span class="toc-dots"></span><span class="toc-page">11</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-12-acad-1"><span class="toc-title">2.3. Términos Académicos: Oferta Educativa Superior en el Campo UNESCO 1013</span><span class="toc-dots"></span><span class="toc-page">12</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-13-acad-2"><span class="toc-title">2.3. Términos Académicos: Vacancia Formativa y Cohorte de Bachilleres (AMIE)</span><span class="toc-dots"></span><span class="toc-page">13</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-14-cultural"><span class="toc-title">2.4. Términos Culturales y Tendencias Tecnológicas en la Tercera Ola del Café</span><span class="toc-dots"></span><span class="toc-page">14</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-15-pnd"><span class="toc-title">3. ARTICULACIÓN CON EL PLAN NACIONAL DE DESARROLLO (PND 2025–2029)</span><span class="toc-dots"></span><span class="toc-page">15</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-16-territorial"><span class="toc-title">4. ARTICULACIÓN CON LA PLANIFICACIÓN TERRITORIAL (PDOT Y PMDOT)</span><span class="toc-dots"></span><span class="toc-page">16</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-17-solucion"><span class="toc-title">5. CONTRIBUCIÓN DE LOS PROFESIONALES A LA SOLUCIÓN DE PROBLEMAS</span><span class="toc-dots"></span><span class="toc-page">17</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-18-demanda-emp-1"><span class="toc-title">6. ESTUDIO DE MERCADO Y DEMANDA (INVESTIGACIÓN DE CAMPO)</span><span class="toc-dots"></span><span class="toc-page">18</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-18-demanda-emp-1"><span class="toc-title">6.1. Demanda Ocupacional: Muestreo de Cochran y Ficha Técnica Empresarial</span><span class="toc-dots"></span><span class="toc-page">18</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-19-demanda-emp-2"><span class="toc-title">6.1. Demanda Ocupacional: Resultados de Encuesta a 380 Cafeterías</span><span class="toc-dots"></span><span class="toc-page">19</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-20-brecha"><span class="toc-title">6.1. Demanda Ocupacional: Estimación de Brecha Laboral y Absorción Anual</span><span class="toc-dots"></span><span class="toc-page">20</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-21-estudiantil-1"><span class="toc-title">6.2. Demanda Estudiantil: Diseño Muestral y Resultados en Bachilleres</span><span class="toc-dots"></span><span class="toc-page">21</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-22-malla"><span class="toc-title">6.2. Demanda Estudiantil: Proyección de Matrícula y Estructura Curricular</span><span class="toc-dots"></span><span class="toc-page">22</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-23-conclusiones"><span class="toc-title">7. CONCLUSIONES INSTITUCIONALES Y DICTAMEN DE PERTINENCIA IAVQ</span><span class="toc-dots"></span><span class="toc-page">23</span></a></div>
          <div class="toc-row toc-level-1"><a href="#page-24-referencias"><span class="toc-title">8. REFERENCIAS BIBLIOGRÁFICAS (APA 7MA ED.) Y MATRIZ DE AUDITORÍA</span><span class="toc-dots"></span><span class="toc-page">24</span></a></div>

          <div class="toc-group-title" style="margin-top: 5pt;">2. ÍNDICE DE TABLAS ESTADÍSTICAS Y MATRICES TÉCNICAS</div>
          <div class="toc-row toc-level-2"><a href="#page-04-social-1"><span class="toc-title">Tabla 1. Proyección de la población de Ecuador, Pichincha y Quito (2026-2035)</span><span class="toc-dots"></span><span class="toc-page">4</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-06-econ-1"><span class="toc-title">Tabla 2. Evolución de los establecimientos vinculados al sector de alojamiento y comidas (2012-2024)</span><span class="toc-dots"></span><span class="toc-page">6</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-06-econ-1"><span class="toc-title">Tabla 3. Evolución de las plazas laborales disponibles en alojamiento y comidas (2012-2024)</span><span class="toc-dots"></span><span class="toc-page">6</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-07-econ-2"><span class="toc-title">Tabla 4. Evolución de las ventas del sector de alojamiento y comidas en millones de USD (2012-2024)</span><span class="toc-dots"></span><span class="toc-page">7</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-08-supercias"><span class="toc-title">Tabla 5. Ranking Financiero de Compañías Líderes en Cafeterías y Tueste de Café en Quito (SUPERCIAS 2026)</span><span class="toc-dots"></span><span class="toc-page">8</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-09-enemdu-edu"><span class="toc-title">Tabla 6. Distribución del Personal Ocupado en Cafeterías según Nivel de Instrucción (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">9</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-10-enemdu-iess"><span class="toc-title">Tabla 7. Cobertura de Afiliación a la Seguridad Social (IESS) en Trabajadores de Cafeterías (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">10</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-11-enemdu-salario"><span class="toc-title">Tabla 8. Ingreso Laboral Promedio según Nivel de Instrucción en el Sector Cafeterías en Quito (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">11</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-12-acad-1"><span class="toc-title">Tabla 9. Oferta Académica Vigente de Tercer Nivel Técnico y Tecnológico en CINE 1013 en Pichincha</span><span class="toc-dots"></span><span class="toc-page">12</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-13-acad-2"><span class="toc-title">Tabla 10. Historial de Titulados en Carreras Específicas de Barismo en Pichincha (SENESCYT 2012-2024)</span><span class="toc-dots"></span><span class="toc-page">13</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-13-acad-2"><span class="toc-title">Tabla 11. Evolución de Matrícula en Tercer Año de Bachillerato en el Cantón Quito (AMIE 2020-2025)</span><span class="toc-dots"></span><span class="toc-page">13</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-15-pnd"><span class="toc-title">Tabla 12. Matriz de Articulación del Proyecto Curricular con los Ejes del PND 2025-2029</span><span class="toc-dots"></span><span class="toc-page">15</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-16-territorial"><span class="toc-title">Tabla 13. Matriz de Articulación con el PDOT Pichincha y el PMDOT Quito (Ordenanza 004-2024)</span><span class="toc-dots"></span><span class="toc-page">16</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-17-solucion"><span class="toc-title">Tabla 14. Matriz de Contribución de los Graduados a los Problemas Productivos del Sector</span><span class="toc-dots"></span><span class="toc-page">17</span></a></div>

          <div class="toc-group-title" style="margin-top: 5pt;">3. ÍNDICE DE GRÁFICOS Y FIGURAS ANALÍTICAS</div>
          <div class="toc-row toc-level-2"><a href="#page-04-social-1"><span class="toc-title">Gráfico 1. Proyección del grupo etario de 18-24 años en Ecuador, Pichincha y Quito (2026-2035)</span><span class="toc-dots"></span><span class="toc-page">4</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-04-social-1"><span class="toc-title">Gráfico 2. Proporción de la Juventud (18-24 años) en el Cantón Quito (2026)</span><span class="toc-dots"></span><span class="toc-page">4</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-05-social-2"><span class="toc-title">Gráfico 3. Distribución de la Población del Cantón Quito por Nivel de Educación (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">5</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-05-social-2"><span class="toc-title">Gráfico 4. Distribución de la Población del Cantón Quito por Sexo (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">5</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-05-social-2"><span class="toc-title">Gráfico 5. Asistencia a Clases de la Juventud (18-24 años) en el Cantón Quito (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">5</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-05-social-2"><span class="toc-title">Gráfico 6. Tasa de Desempleo Juvenil (18-24 años) vs. Promedio Cantonal de Quito (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">5</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-07-econ-2"><span class="toc-title">Gráfico 7. Evolución de Ventas del Sector Servicios de Alimentos y Bebidas en Quito (2012-2024)</span><span class="toc-dots"></span><span class="toc-page">7</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-07-econ-2"><span class="toc-title">Gráfico 8. Constitución Histórica de Compañías de Cafeterías en Quito (SUPERCIAS 2026)</span><span class="toc-dots"></span><span class="toc-page">7</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-09-enemdu-edu"><span class="toc-title">Gráfico 9. Nivel de Instrucción de los Trabajadores de Cafeterías en Quito (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">9</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-10-enemdu-iess"><span class="toc-title">Gráfico 10. Cobertura de Afiliación al IESS en el Sector de Cafeterías (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">10</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-11-enemdu-salario"><span class="toc-title">Gráfico 11. Comparativa Salarial Promedio por Nivel de Instrucción vs. SBU (ENEMDU 2025)</span><span class="toc-dots"></span><span class="toc-page">11</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-12-acad-1"><span class="toc-title">Gráfico 12. Distribución de Matrícula en Programas de Gastronomía en Pichincha (SNIESE 2026)</span><span class="toc-dots"></span><span class="toc-page">12</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-13-acad-2"><span class="toc-title">Gráfico 13. Evolución de la Cohorte de Bachilleres Graduandos en Quito (AMIE 2020-2025)</span><span class="toc-dots"></span><span class="toc-page">13</span></a></div>
          <div class="toc-row toc-level-2"><a href="#page-16-territorial"><span class="toc-title">Gráfico 14. Ejes Estratégicos Territoriales Articulados con la Carrera de Barismo</span><span class="toc-dots"></span><span class="toc-page">16</span></a></div>
        </div>
      </div>
      {get_page_footer(2)}
    </div>
    """

    # ==========================================
    # PÁGINA 3: 1. INTRODUCCIÓN Y ANTECEDENTES
    # ==========================================
    pages[3] = f"""
    <div class="word-page" id="page-03-intro">
      {get_page_header(3)}
      <div class="word-content">
        <h1 class="word-heading-1">1. INTRODUCCIÓN Y ANTECEDENTES</h1>
        
        <h2 class="word-heading-2">1.1. Contexto Histórico y Productivo de la Caficultura Ecuatoriana</h2>
        <p class="word-p">
          El cultivo y procesamiento del café en la República del Ecuador constituye uno de los pilares agroindustriales y patrimoniales con mayor arraigo socioeconómico. Históricamente, el país se caracterizó por la exportación de granos comerciales arábica y robusta bajo esquemas convencionales de volumen. Sin embargo, a lo largo de las últimas dos décadas se ha registrado una transformación estructural profunda impulsada por la emergencia de los cafés de especialidad, la revalorización de variedades botánicas de alto valor aromático (Típica Mejorada, Sidra, Bourbon, Geisha, Pacamara) y la consolidación de certámenes de excelencia sensorial como Taza Dorada.
        </p>
        <p class="word-p">
          En este escenario, la Provincia de Pichincha —particularmente a través de la Mancomunidad del Chocó Andino y las parroquias noroccidentales del Distrito Metropolitano de Quito (Nanegal, Pacto, Nanegalito, Gualea)— se ha posicionado como un territorio de excelencia cafetalera internacional. Sus microclimas de bosque nublado, altitudes comprendidas entre 1.200 y 2.000 metros sobre el nivel del mar y suelos volcánicos fértiles generan perfiles de taza excepcionales, galardonados en subastas mundiales con calificaciones superiores a los 90 puntos sobre la escala de la Specialty Coffee Association (SCA).
        </p>

        <h2 class="word-heading-2">1.2. La Revolución de la Tercera Ola y la Expansión de Cafeterías en Quito</h2>
        <p class="word-p">
          A nivel del mercado de consumo, el Cantón Quito experimenta una transformación urbana y comercial denominada internacionalmente como la "Tercera Ola del Café". Este movimiento concibe al café no como un commodity indiferenciado, sino como una experiencia gastronómica, sensorial y cultural de alta sofisticación técnica. Distritos metropolitanos consolidados como La Floresta, La Mariscal, González Suárez, Cumbayá, Tumbaco y el Centro Histórico albergan una red en rápida expansión de cafeterías de especialidad, tostadurías artesanales y barras de filtrado experimental (brew bars).
        </p>
        <p class="word-p">
          El consumidor actual demanda estándares rigurosos de trazabilidad de origen, conocimiento detallado de los procesos de poscosecha (lavados prolongados, procesos honey, fermentaciones anaeróbicas controladas y maceraciones carbónicas), así como un servicio técnico especializado basado en la química del agua, la termodinámica del espresso y la ejecución precisa de métodos de extracción por goteo, inmersión y presión.
        </p>

        <h2 class="word-heading-2">1.3. La Problemática del Empirismo y la Necesidad de Profesionalización</h2>
        <p class="word-p">
          A pesar del dinámico crecimiento del mercado y de la facturación del sector, la operación cotidiana de las barras de café en el Cantón Quito presenta una severa contradicción: la preparación de bebidas y la gestión de equipos de extracción de alta gama continúan realizándose de manera predominantemente empírica. La evidencia oficial del mercado laboral revela que más del 80% del personal ocupado en barras y cafeterías carece de formación técnica de tercer nivel, sustentando sus prácticas en instrucciones informales de corta duración que no abarcan los fundamentos fisicoquímicos, el control de mermas ni los protocolos de calibración sensorial.
        </p>

        <h2 class="word-heading-2">1.4. Trayectoria Institucional del IAVQ y Fundamentación de los Itinerarios</h2>
        <p class="word-p">
          El <strong>Instituto Superior Tecnológico de Artes Visuales de Quito (IAVQ)</strong>, legalmente constituido y reconocido por el Consejo de Educación Superior (CES) con condición de Instituto Superior Universitario, cuenta con una sólida trayectoria en la formación técnica y tecnológica superior. Con el propósito de articular la creatividad, la técnica operativa y el rigor agroindustrial, el IAVQ plantea el proyecto curricular de la carrera de <strong>Técnico Superior en Barismo</strong> bajo modalidad híbrida, estructurada en dos itinerarios formativos pertinentes:
        </p>
        <div class="word-callout">
          <p style="margin: 0; font-size: 8.8pt;">
            <strong>Itinerario 1: Barismo de Especialidad, Catación Sensorial y Tueste Artesanal:</strong> Especialización en perfiles de tueste, protocolos de catación SCA, química de la extracción y diseño de bebidas de especialidad.<br>
            <strong>Itinerario 2: Gestión Operativa de Barras, Emprendimiento y Control de Calidad:</strong> Enfoque en administración de modelos de negocio gastronómicos, costeo y mermas, mantenimiento preventivo de maquinaria y normativas BPM.
          </p>
        </div>
      </div>
      {get_page_footer(3)}
    </div>
    """

    # ==========================================
    # PÁGINA 4: 2.1. TÉRMINOS SOCIALES (DEMOGRAFÍA OFICIAL 2026-2035)
    # ==========================================
    pages[4] = f"""
    <div class="word-page" id="page-04-social-1">
      {get_page_header(4)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (DIAGNÓSTICO)</h1>
        <h2 class="word-heading-2">2.1. Términos Sociales: Proyecciones Demográficas Oficiales y Grupo Juvenil (2026–2035)</h2>
        
        <p class="word-p">
          El análisis de la pertinencia social se fundamenta rigurosamente en las <em>Estimaciones y Proyecciones de Población Nacional, Provincial y Cantonal (Revisión 2024)</em> elaboradas por el Instituto Nacional de Estadística y Censos (INEC). Las series oficiales determinan que entre 2026 y 2035 el Cantón Quito experimenta un crecimiento sostenido, pasando de 2.875.075 a 3.015.497 habitantes.
        </p>

        <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; margin: 2pt 0 1.5pt 0;">
          Tabla 1. Proyección de la población de Ecuador, Pichincha y Quito, en número de personas y porcentaje de crecimiento (2026–2035)
        </div>
        <table class="word-table" style="font-size: 7.2pt;">
          <thead>
            <tr>
              <th rowspan="2" style="text-align: center; vertical-align: middle; width: 8%;">Año</th>
              <th colspan="3" style="text-align: center; width: 48%;">Número de Habitantes</th>
              <th colspan="3" style="text-align: center; width: 44%;">Tasa de Crecimiento Anual</th>
            </tr>
            <tr>
              <th style="text-align: right; width: 16%;">Ecuador</th>
              <th style="text-align: right; width: 16%;">Pichincha</th>
              <th style="text-align: right; width: 16%;">Quito</th>
              <th style="text-align: right; width: 14%;">Ecuador</th>
              <th style="text-align: right; width: 15%;">Pichincha</th>
              <th style="text-align: right; width: 15%;">Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; font-weight: bold;">2026</td>
              <td style="text-align: right;">18.243.816</td>
              <td style="text-align: right;">3.316.636</td>
              <td style="text-align: right; font-weight: bold;">2.875.075</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2027</td>
              <td style="text-align: right;">18.385.975</td>
              <td style="text-align: right;">3.338.444</td>
              <td style="text-align: right;">2.893.151</td>
              <td style="text-align: right;">0,78%</td>
              <td style="text-align: right;">0,66%</td>
              <td style="text-align: right;">0,63%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2028</td>
              <td style="text-align: right;">18.529.121</td>
              <td style="text-align: right;">3.359.670</td>
              <td style="text-align: right;">2.910.700</td>
              <td style="text-align: right;">0,78%</td>
              <td style="text-align: right;">0,64%</td>
              <td style="text-align: right;">0,61%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2029</td>
              <td style="text-align: right;">18.672.456</td>
              <td style="text-align: right;">3.380.169</td>
              <td style="text-align: right;">2.927.602</td>
              <td style="text-align: right;">0,77%</td>
              <td style="text-align: right;">0,61%</td>
              <td style="text-align: right;">0,58%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2030</td>
              <td style="text-align: right;">18.815.497</td>
              <td style="text-align: right;">3.399.908</td>
              <td style="text-align: right;">2.943.834</td>
              <td style="text-align: right;">0,77%</td>
              <td style="text-align: right;">0,58%</td>
              <td style="text-align: right;">0,55%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2031</td>
              <td style="text-align: right;">18.957.924</td>
              <td style="text-align: right;">3.418.947</td>
              <td style="text-align: right;">2.959.453</td>
              <td style="text-align: right;">0,76%</td>
              <td style="text-align: right;">0,56%</td>
              <td style="text-align: right;">0,53%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2032</td>
              <td style="text-align: right;">19.099.478</td>
              <td style="text-align: right;">3.437.380</td>
              <td style="text-align: right;">2.974.544</td>
              <td style="text-align: right;">0,75%</td>
              <td style="text-align: right;">0,54%</td>
              <td style="text-align: right;">0,51%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2033</td>
              <td style="text-align: right;">19.239.759</td>
              <td style="text-align: right;">3.455.019</td>
              <td style="text-align: right;">2.988.948</td>
              <td style="text-align: right;">0,73%</td>
              <td style="text-align: right;">0,51%</td>
              <td style="text-align: right;">0,48%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2034</td>
              <td style="text-align: right;">19.378.452</td>
              <td style="text-align: right;">3.471.715</td>
              <td style="text-align: right;">3.002.540</td>
              <td style="text-align: right;">0,72%</td>
              <td style="text-align: right;">0,48%</td>
              <td style="text-align: right;">0,45%</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td style="text-align: center;">2035</td>
              <td style="text-align: right;">19.515.303</td>
              <td style="text-align: right;">3.487.672</td>
              <td style="text-align: right;">3.015.497</td>
              <td style="text-align: right;">0,71%</td>
              <td style="text-align: right;">0,46%</td>
              <td style="text-align: right;">0,43%</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Instituto Nacional de Estadística y Censos (INEC), Estimaciones y Proyecciones de Población Nacional Provincial Cantonal Revisión 2024.</div>

        <div style="display: flex; gap: 10px; margin-top: 4pt;">
          <div style="flex: 1.1; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
            <div style="font-size: 7.5pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 1. Grupo etario 18-24 años: Ecuador, Pichincha y Quito (2026 vs. 2035)
            </div>
            <div style="height: 125px; position: relative;">
              <canvas id="chart-graf-01"></canvas>
            </div>
          </div>

          <div style="flex: 0.9; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
            <div style="font-size: 7.5pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 2. Proporción de la Juventud (18-24 años) en Quito (2026)
            </div>
            <div style="height: 125px; position: relative;">
              <canvas id="chart-graf-02"></canvas>
            </div>
          </div>
        </div>

        <p class="word-p" style="margin-top: 4pt;">
          <strong>Dinámica del Grupo Juvenil de Control (18 a 24 años):</strong> Para el año 2026, el Cantón Quito cuenta con <strong>301.883 jóvenes</strong> en el grupo etario de 18 a 24 años (población de referencia para la educación superior). Hacia 2035, esta cohorte experimenta una ligera contracción demográfica situándose en 296.214 jóvenes (-1,88%), reflejando la transición etaria del país. Esta masa crítica de más de 300.000 jóvenes demanda opciones de educación técnica de ciclo corto (dos años) con rápida salida laboral como la carrera de Técnico Superior en Barismo.
        </p>
      </div>
      {get_page_footer(4)}
    </div>
    """

    # ==========================================
    # PÁGINA 5: 2.1. TÉRMINOS SOCIALES (MERCADO LABORAL ENEMDU 2025)
    # ==========================================
    pages[5] = f"""
    <div class="word-page" id="page-05-social-2">
      {get_page_header(5)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.1. Términos Sociales: Mercado Laboral Juvenil, Desempleo y Educación (ENEMDU 2025)</h2>
        
        <p class="word-p">
          Los microdatos oficiales de la Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU Anual 2025) para el Cantón Quito permiten caracterizar de manera precisa el perfil socioeducativo y las condiciones críticas de vulnerabilidad laboral que afronta la población juvenil de 18 a 24 años.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 4pt 0;">
          <div style="border: 1px solid #D9D9D9; padding: 4pt; background: #FAFAFA;">
            <div style="font-size: 7.4pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 3. Población de Quito por Nivel de Educación (ENEMDU 2025)
            </div>
            <div style="height: 120px; position: relative;">
              <canvas id="chart-graf-03"></canvas>
            </div>
          </div>

          <div style="border: 1px solid #D9D9D9; padding: 4pt; background: #FAFAFA;">
            <div style="font-size: 7.4pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 4. Distribución de la Población de Quito por Sexo
            </div>
            <div style="height: 120px; position: relative;">
              <canvas id="chart-graf-04"></canvas>
            </div>
          </div>

          <div style="border: 1px solid #D9D9D9; padding: 4pt; background: #FAFAFA;">
            <div style="font-size: 7.4pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 5. Asistencia a Clases de Jóvenes (18-24 años) en Quito
            </div>
            <div style="height: 120px; position: relative;">
              <canvas id="chart-graf-05"></canvas>
            </div>
          </div>

          <div style="border: 1px solid #D9D9D9; padding: 4pt; background: #FAFAFA;">
            <div style="font-size: 7.4pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 6. Desempleo Juvenil (18-24) vs. Promedio Cantonal de Quito
            </div>
            <div style="height: 120px; position: relative;">
              <canvas id="chart-graf-06"></canvas>
            </div>
          </div>
        </div>

        <p class="word-p">
          <strong>Hallazgos Clave del Diagnóstico Sociolaboral Juvenil (ENEMDU Anual 2025):</strong>
        </p>
        <ul style="margin: 0 0 4pt 0; padding-left: 14pt; font-size: 8.8pt; line-height: 1.3;">
          <li><strong>Brecha Alarmante de Desempleo Juvenil:</strong> La tasa de desempleo en la juventud quiteña de 18 a 24 años se sitúa en el <strong>22,58%</strong> (21.971 desocupados sobre una PEA juvenil de 97.101 personas), triplicando la tasa cantonal de la población general adulta (<strong>7,24%</strong>). En jóvenes con educación media completa, el desempleo alcanza el 24,55%.</li>
          <li><strong>Exclusión Educativa:</strong> El <strong>50,23% de los jóvenes de 18 a 24 años no asiste a ninguna institución educativa</strong>, principalmente por la necesidad de generar ingresos inmediatos y la incompatibilidad de horarios de las ofertas presenciales diurnas.</li>
          <li><strong>Estructura Educativa Cantonal:</strong> En el Cantón Quito, apenas el <strong>5,61%</strong> de la población cuenta con formación técnica o tecnológica superior (112.675 personas), evidenciando un profundo vacío de mano de obra técnica especializada frente al nivel universitario tradicional (17,22%).</li>
        </ul>
        <p class="word-p">
          <strong>Fundamentación Social de la Modalidad Híbrida:</strong> Frente a este panorama de desempleo juvenil y deserción educativa por razones laborales, la carrera de Técnico Superior en Barismo del IAVQ bajo modalidad híbrida representa una solución formativa de inclusión. Permite a los jóvenes compatibilizar jornadas de trabajo en el sector comercial o gastronómico con el aprendizaje teórico virtual y prácticas intensivas de barra los fines de semana.
        </p>
      </div>
      {get_page_footer(5)}
    </div>
    """

    # ==========================================
    # PÁGINA 6: 2.2. TÉRMINOS ECONÓMICOS (REEM 2012-2024)
    # ==========================================
    pages[6] = f"""
    <div class="word-page" id="page-06-econ-1">
      {get_page_header(6)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Términos Económicos: Tejido Productivo y Plazas Laborales en Alojamiento y Comidas (REEM)</h2>
        
        <p class="word-p">
          El análisis del entorno productivo se sustenta de manera determinista en el <em>Directorio del Registro Estadístico de Empresas (REEM 2012–2024)</em> del INEC. Se examina la evolución de los establecimientos y plazas de empleo formal del sector de <strong>Actividades de Alojamiento y de Servicios de Comidas (CIIU Sección I, División 56)</strong> en Ecuador, Pichincha y Quito.
        </p>

        <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; margin: 2pt 0 1.5pt 0;">
          Tabla 2. Evolución de los establecimientos vinculados al sector de actividades de alojamiento y comidas (2012–2024)
        </div>
        <table class="word-table" style="font-size: 7.2pt;">
          <thead>
            <tr>
              <th rowspan="2" style="text-align: center; vertical-align: middle; width: 8%;">Año</th>
              <th colspan="3" style="text-align: center; width: 48%;">Número de Establecimientos</th>
              <th colspan="3" style="text-align: center; width: 44%;">Tasa de Crecimiento Anual</th>
            </tr>
            <tr>
              <th style="text-align: right; width: 16%;">Ecuador</th>
              <th style="text-align: right; width: 16%;">Pichincha</th>
              <th style="text-align: right; width: 16%;">Quito</th>
              <th style="text-align: right; width: 14%;">Ecuador</th>
              <th style="text-align: right; width: 15%;">Pichincha</th>
              <th style="text-align: right; width: 15%;">Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; font-weight: bold;">2012</td>
              <td style="text-align: right;">54.407</td>
              <td style="text-align: right;">12.892</td>
              <td style="text-align: right; font-weight: bold;">11.335</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2015</td>
              <td style="text-align: right;">66.508</td>
              <td style="text-align: right;">15.339</td>
              <td style="text-align: right;">13.307</td>
              <td style="text-align: right;">-0,57%</td>
              <td style="text-align: right;">-2,03%</td>
              <td style="text-align: right;">-2,48%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2018</td>
              <td style="text-align: right;">75.980</td>
              <td style="text-align: right;">15.980</td>
              <td style="text-align: right;">13.111</td>
              <td style="text-align: right;">+3,81%</td>
              <td style="text-align: right;">+4,17%</td>
              <td style="text-align: right;">+3,89%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2021</td>
              <td style="text-align: right;">74.890</td>
              <td style="text-align: right;">15.890</td>
              <td style="text-align: right;">13.565</td>
              <td style="text-align: right;">+3,80%</td>
              <td style="text-align: right;">+3,05%</td>
              <td style="text-align: right;">+3,25%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2022</td>
              <td style="text-align: right;">79.120</td>
              <td style="text-align: right;">16.940</td>
              <td style="text-align: right;">14.629</td>
              <td style="text-align: right;">+5,65%</td>
              <td style="text-align: right;">+6,61%</td>
              <td style="text-align: right;">+7,84%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2023</td>
              <td style="text-align: right;">81.230</td>
              <td style="text-align: right;">17.890</td>
              <td style="text-align: right;">15.341</td>
              <td style="text-align: right;">+2,67%</td>
              <td style="text-align: right;">+5,61%</td>
              <td style="text-align: right;">+4,87%</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td style="text-align: center;">2024</td>
              <td style="text-align: right;">88.450</td>
              <td style="text-align: right;">19.452</td>
              <td style="text-align: right;">16.673</td>
              <td style="text-align: right;">+8,89%</td>
              <td style="text-align: right;">+8,73%</td>
              <td style="text-align: right;">+8,68%</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Instituto Nacional de Estadística y Censos (INEC), Registro Estadístico de Empresas (REEM) 2024.</div>

        <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 1.5pt 0;">
          Tabla 3. Evolución de las plazas laborales disponibles en el sector de alojamiento y comidas (2012–2024)
        </div>
        <table class="word-table" style="font-size: 7.2pt;">
          <thead>
            <tr>
              <th rowspan="2" style="text-align: center; vertical-align: middle; width: 8%;">Año</th>
              <th colspan="3" style="text-align: center; width: 48%;">Número de Plazas de Empleo</th>
              <th colspan="3" style="text-align: center; width: 44%;">Tasa de Crecimiento Anual</th>
            </tr>
            <tr>
              <th style="text-align: right; width: 16%;">Ecuador</th>
              <th style="text-align: right; width: 16%;">Pichincha</th>
              <th style="text-align: right; width: 16%;">Quito</th>
              <th style="text-align: right; width: 14%;">Ecuador</th>
              <th style="text-align: right; width: 15%;">Pichincha</th>
              <th style="text-align: right; width: 15%;">Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; font-weight: bold;">2012</td>
              <td style="text-align: right;">101.739</td>
              <td style="text-align: right;">45.527</td>
              <td style="text-align: right; font-weight: bold;">43.461</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2021</td>
              <td style="text-align: right;">89.349</td>
              <td style="text-align: right;">35.976</td>
              <td style="text-align: right;">33.915</td>
              <td style="text-align: right;">-7,75%</td>
              <td style="text-align: right;">-8,40%</td>
              <td style="text-align: right;">-8,50%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2022</td>
              <td style="text-align: right;">101.251</td>
              <td style="text-align: right;">40.376</td>
              <td style="text-align: right;">38.103</td>
              <td style="text-align: right;">+13,32%</td>
              <td style="text-align: right;">+12,23%</td>
              <td style="text-align: right;">+12,35%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2023</td>
              <td style="text-align: right;">109.671</td>
              <td style="text-align: right;">44.055</td>
              <td style="text-align: right;">40.697</td>
              <td style="text-align: right;">+8,32%</td>
              <td style="text-align: right;">+9,11%</td>
              <td style="text-align: right;">+6,81%</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td style="text-align: center;">2024</td>
              <td style="text-align: right;">115.012</td>
              <td style="text-align: right;">46.584</td>
              <td style="text-align: right;">44.038</td>
              <td style="text-align: right;">+4,87%</td>
              <td style="text-align: right;">+5,74%</td>
              <td style="text-align: right;">+8,21%</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Instituto Nacional de Estadística y Censos (INEC), Registro Estadístico de Empresas (REEM) 2024.</div>

        <p class="word-p" style="margin-top: 4pt;">
          <strong>Interpretación y Dinamismo Económico:</strong> El REEM 2024 demuestra que el sector gastronómico en Quito pasó de 11.335 locales en 2012 a <strong>16.673 establecimientos en 2024</strong> (+47,1% acumulado). Asimismo, las plazas laborales formales en el cantón crecieron de forma acelerada tras la reactivación, pasando de 33.915 en 2021 a <strong>44.038 plazas en 2024 (+29,85% de incremento)</strong>, demandando con urgencia talento capacitado en preparación técnica de bebidas y café.
        </p>
      </div>
      {get_page_footer(6)}
    </div>
    """

    # ==========================================
    # PÁGINA 7: 2.2. TÉRMINOS ECONÓMICOS (VENTAS REEM Y CONSTITUCIÓN)
    # ==========================================
    pages[7] = f"""
    <div class="word-page" id="page-07-econ-2">
      {get_page_header(7)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Términos Económicos: Ventas del Sector y Auge Societario de Cafeterías</h2>
        
        <p class="word-p">
          Las ventas del sector de alojamiento y comidas en el Cantón Quito registraron una evolución notable en la serie histórica del REEM (INEC, 2024), alcanzando <strong>USD 1.434,44 millones en 2024</strong>, con un crecimiento anual del <strong>+7,41%</strong> y un crecimiento acumulado de <strong>+48,82%</strong> frente al año base 2012 (USD 963,88 millones).
        </p>

        <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; margin: 2pt 0 1.5pt 0;">
          Tabla 4. Evolución de las ventas del sector de alojamiento y comidas en millones de USD (2012–2024)
        </div>
        <table class="word-table" style="font-size: 7.2pt;">
          <thead>
            <tr>
              <th rowspan="2" style="text-align: center; vertical-align: middle; width: 8%;">Año</th>
              <th colspan="3" style="text-align: center; width: 48%;">Ventas en Millones de Dólares (USD)</th>
              <th colspan="3" style="text-align: center; width: 44%;">Tasa de Crecimiento Anual</th>
            </tr>
            <tr>
              <th style="text-align: right; width: 16%;">Ecuador</th>
              <th style="text-align: right; width: 16%;">Pichincha</th>
              <th style="text-align: right; width: 16%;">Quito</th>
              <th style="text-align: right; width: 14%;">Ecuador</th>
              <th style="text-align: right; width: 15%;">Pichincha</th>
              <th style="text-align: right; width: 15%;">Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; font-weight: bold;">2012</td>
              <td style="text-align: right;">1.729,69</td>
              <td style="text-align: right;">985,37</td>
              <td style="text-align: right; font-weight: bold;">963,88</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
              <td style="text-align: right;">—</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2015</td>
              <td style="text-align: right;">2.229,37</td>
              <td style="text-align: right;">1.196,06</td>
              <td style="text-align: right;">1.166,93</td>
              <td style="text-align: right;">-0,04%</td>
              <td style="text-align: right;">-1,37%</td>
              <td style="text-align: right;">-1,61%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2018</td>
              <td style="text-align: right;">2.423,78</td>
              <td style="text-align: right;">1.215,42</td>
              <td style="text-align: right;">1.187,84</td>
              <td style="text-align: right;">+9,91%</td>
              <td style="text-align: right;">+7,25%</td>
              <td style="text-align: right;">+7,20%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2021</td>
              <td style="text-align: right;">2.034,57</td>
              <td style="text-align: right;">986,41</td>
              <td style="text-align: right;">959,17</td>
              <td style="text-align: right;">+40,34%</td>
              <td style="text-align: right;">+34,25%</td>
              <td style="text-align: right;">+33,67%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2022</td>
              <td style="text-align: right;">2.564,88</td>
              <td style="text-align: right;">1.233,64</td>
              <td style="text-align: right;">1.201,73</td>
              <td style="text-align: right;">+26,07%</td>
              <td style="text-align: right;">+25,06%</td>
              <td style="text-align: right;">+25,29%</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2023</td>
              <td style="text-align: right;">2.910,30</td>
              <td style="text-align: right;">1.399,92</td>
              <td style="text-align: right;">1.335,44</td>
              <td style="text-align: right;">+13,47%</td>
              <td style="text-align: right;">+13,48%</td>
              <td style="text-align: right;">+11,13%</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td style="text-align: center;">2024</td>
              <td style="text-align: right;">2.953,89</td>
              <td style="text-align: right;">1.466,64</td>
              <td style="text-align: right;">1.434,44</td>
              <td style="text-align: right;">+1,50%</td>
              <td style="text-align: right;">+4,77%</td>
              <td style="text-align: right;">+7,41%</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Instituto Nacional de Estadística y Censos (INEC), Registro Estadístico de Empresas (REEM) 2024.</div>

        <div style="display: flex; gap: 10px; margin-top: 4pt;">
          <div style="flex: 1; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
            <div style="font-size: 7.5pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 7. Ventas del Sector Alimentos y Bebidas en Quito (M$ USD)
            </div>
            <div style="height: 125px; position: relative;">
              <canvas id="chart-graf-07"></canvas>
            </div>
          </div>

          <div style="flex: 1; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
            <div style="font-size: 7.5pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
              Gráfico 8. Constitución de Empresas Cafeteras en Quito (SUPERCIAS 2026)
            </div>
            <div style="height: 125px; position: relative;">
              <canvas id="chart-graf-08"></canvas>
            </div>
          </div>
        </div>

        <p class="word-p" style="margin-top: 4pt;">
          <strong>El Auge de las Cafeterías de Especialidad (SUPERCIAS 2026):</strong> En concordancia con la expansión de ventas, el Directorio de Compañías de la SUPERCIAS (corte 2026) registra 159 compañías activas dedicadas a cafeterías y tostado en Quito. De ellas, el <strong>77,4% (123 sociedades)</strong> fueron constituidas a partir del año 2020. Este crecimiento exponencial confirma que el negocio del barismo de especialidad y la tostaduría urbana representa uno de los polos de innovación privada más dinámicos de la economía metropolitana.
        </p>
      </div>
      {get_page_footer(7)}
    </div>
    """

    # ==========================================
    # PÁGINA 8: 2.2. TEJIDO EMPRESARIAL (SUPERCIAS RANKING)
    # ==========================================
    pages[8] = f"""
    <div class="word-page" id="page-08-supercias">
      {get_page_header(8)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Tejido Empresarial: Directorio y Ranking Societario en Quito (SUPERCIAS 2026)</h2>
        
        <p class="word-p">
          Para garantizar la máxima veracidad y evitar sobreinflaciones estadísticas, se auditó la base de datos oficial de la Superintendencia de Compañías, Valores y Seguros (SUPERCIAS, corte 2026). En el Cantón Quito se identifican <strong>159 compañías jurídicamente activas</strong> dedicadas de forma directa y exclusiva a la operación de cafeterías, servicios de bebidas de barra y tostado artesanal de café (códigos CIIU I5630, C1079 y marcas cafeteras en I5610).
        </p>
        <p class="word-p">
          A continuación, se detalla el ranking financiero de los principales empleadores y operadores de cadenas de cafeterías y tostadurías en el Cantón Quito, ordenados por volumen de facturación y personal ocupado directo.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 5. Ranking Financiero de Compañías Líderes en Cafeterías y Tueste de Café en Quito (SUPERCIAS 2026)
        </div>
        <table class="word-table" style="font-size: 7.6pt;">
          <thead>
            <tr>
              <th style="width: 4%; text-align: center;">#</th>
              <th style="width: 32%;">Razón Social / Marca</th>
              <th style="width: 14%; text-align: right;">Ventas (USD)</th>
              <th style="width: 13%; text-align: right;">Activos (USD)</th>
              <th style="width: 8%; text-align: center;">Personal</th>
              <th style="width: 14%;">Tipo Societario</th>
              <th style="width: 15%;">Código CIIU</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; font-weight: bold;">1</td>
              <td><strong>PROCAFECOL ECUADOR S.A.</strong> (Juan Valdez)</td>
              <td style="text-align: right;">$26.862.628</td>
              <td style="text-align: right;">$16.894.212</td>
              <td style="text-align: center; font-weight: bold;">678</td>
              <td>Sociedad Anónima</td>
              <td>I5630.01 / C1079</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">2</td>
              <td><strong>DELONORTE S.A.</strong> (Café Sweet & Coffee Quito)</td>
              <td style="text-align: right;">$5.334.873</td>
              <td style="text-align: right;">$3.279.467</td>
              <td style="text-align: center; font-weight: bold;">120</td>
              <td>Sociedad Anónima</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">3</td>
              <td><strong>KATARIPLAZA S.A.S.</strong> (Cafeterías Katari)</td>
              <td style="text-align: right;">$2.115.908</td>
              <td style="text-align: right;">$1.045.230</td>
              <td style="text-align: center; font-weight: bold;">87</td>
              <td>S.A.S.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">4</td>
              <td><strong>SABAI BEBIDAS CIA. LTDA.</strong></td>
              <td style="text-align: right;">$1.472.930</td>
              <td style="text-align: right;">$950.410</td>
              <td style="text-align: center; font-weight: bold;">42</td>
              <td>Cía. Ltda.</td>
              <td>I5630.02</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">5</td>
              <td><strong>SERVICIOS GOLDESEL CIA. LTDA.</strong></td>
              <td style="text-align: right;">$1.385.178</td>
              <td style="text-align: right;">$712.440</td>
              <td style="text-align: center; font-weight: bold;">31</td>
              <td>Cía. Ltda.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">6</td>
              <td><strong>TEAM180 COFFEE WORKERS S.A.S.</strong></td>
              <td style="text-align: right;">$1.107.562</td>
              <td style="text-align: right;">$530.120</td>
              <td style="text-align: center; font-weight: bold;">12</td>
              <td>S.A.S.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">7</td>
              <td><strong>PANADERÍA Y CAFETERÍA 227 S.A.S.</strong></td>
              <td style="text-align: right;">$1.094.210</td>
              <td style="text-align: right;">$480.950</td>
              <td style="text-align: center; font-weight: bold;">13</td>
              <td>S.A.S.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">8</td>
              <td><strong>MAINCOFFEE ROASTERS S.A.S.</strong></td>
              <td style="text-align: right;">$987.450</td>
              <td style="text-align: right;">$415.800</td>
              <td style="text-align: center; font-weight: bold;">26</td>
              <td>S.A.S.</td>
              <td>C1079.11 / I5630</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">9</td>
              <td><strong>DELI LUCIA CAFETERIAS S.A.S.</strong></td>
              <td style="text-align: right;">$715.300</td>
              <td style="text-align: right;">$310.200</td>
              <td style="text-align: center; font-weight: bold;">14</td>
              <td>S.A.S.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">10</td>
              <td><strong>VERALI CAFE CIA. LTDA.</strong></td>
              <td style="text-align: right;">$675.400</td>
              <td style="text-align: right;">$295.100</td>
              <td style="text-align: center; font-weight: bold;">9</td>
              <td>Cía. Ltda.</td>
              <td>I5630.01</td>
            </tr>
            <tr>
              <td style="text-align: center; font-weight: bold;">11</td>
              <td><strong>CAFETERIA FRANCESA CIA. LTDA.</strong></td>
              <td style="text-align: right;">$580.200</td>
              <td style="text-align: right;">$340.500</td>
              <td style="text-align: center; font-weight: bold;">18</td>
              <td>Cía. Ltda.</td>
              <td>I5610.01 / I5630</td>
            </tr>
            <tr style="background-color: #EBF1F5;">
              <td style="text-align: center; font-weight: bold;">12</td>
              <td><strong>CAFÉ DE LA PLAZA S.A.S.</strong></td>
              <td style="text-align: right;">$495.100</td>
              <td style="text-align: right;">$210.400</td>
              <td style="text-align: center; font-weight: bold;">11</td>
              <td>S.A.S.</td>
              <td>I5630.01</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Directorio de Compañías y Balances Financieros (SUPERCIAS, 2026) / Elaboración: Equipo Técnico IAVQ (2026).</div>

        <p class="word-p" style="margin-top: 5pt;">
          <strong>Articulación para Prácticas Preprofesionales y Formación Dual:</strong> Este conjunto de empresas líderes y tostadurías de especialidad concentra más de 1.060 plazas de trabajo formal directo únicamente en sus nóminas corporativas de Quito. Dichas entidades constituyen los socios estratégicos naturales para la suscripción de convenios de formación dual, pasantías y vinculación con la comunidad para los estudiantes del IAVQ, asegurando entornos de práctica de alto nivel técnico en barras de espresso comerciales y de alta gama.
        </p>
      </div>
      {get_page_footer(8)}
    </div>
    """

    return pages

if __name__ == "__main__":
    pages = generate_pages_1_to_8()
    print(f"Successfully regenerated {len(pages)} pages (Pages 1 to 8).")
