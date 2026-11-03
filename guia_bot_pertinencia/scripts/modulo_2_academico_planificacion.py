# -*- coding: utf-8 -*-
"""
Generador modular de las Páginas 9 a 16 para el Dossier:
Técnico Superior en Barismo - Instituto Superior Tecnológico de Artes Visuales de Quito (IAVQ)
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

def generate_pages_9_to_16():
    pages = {}

    # ==========================================
    # PÁGINA 9: 2.2. DIAGNÓSTICO ENEMDU (INSTRUCCIÓN)
    # ==========================================
    pages[9] = f"""
    <div class="word-page" id="page-09-enemdu-edu">
      {get_page_header(9)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Diagnóstico Ocupacional: Nivel de Instrucción y Brecha de Titulación (ENEMDU 2025)</h2>
        
        <p class="word-p">
          Para dimensionar con rigurosidad empírica el perfil de competencias del talento humano que opera en las barras y cafeterías del Cantón Quito, se procesó la submuestra expandida de la Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU Anual 2025). Se focalizó el cruce entre la rama de actividad de servicios de alimentos y bebidas (CIIU 56) y las ocupaciones directas de preparación de bebidas, camareros de barra y baristas (códigos CIUO-08 5132 y 7515).
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 6. Distribución del Personal Ocupado en Cafeterías y Barras según Nivel de Instrucción en Quito (ENEMDU 2025)
        </div>
        <table class="word-table">
          <thead>
            <tr>
              <th style="width: 38%;">Nivel de Instrucción Formal</th>
              <th style="width: 20%; text-align: right;">Población Expandida</th>
              <th style="width: 18%; text-align: right;">Porcentaje Relativo</th>
              <th style="width: 24%;">Condición Ocupacional</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Sin instrucción / Educación Básica o Primaria</td>
              <td style="text-align: right;">3.517</td>
              <td style="text-align: right;">18,34%</td>
              <td>Mano de obra no calificada</td>
            </tr>
            <tr>
              <td>Secundaria completa (Bachillerato general)</td>
              <td style="text-align: right;">11.863</td>
              <td style="text-align: right;">61,86%</td>
              <td>Mano de obra empírica en barra</td>
            </tr>
            <tr style="background-color: #FEECEC; font-weight: bold; color: #9C0006;">
              <td>Subtotal sin formación superior técnica</td>
              <td style="text-align: right;">15.380</td>
              <td style="text-align: right;">80,20%</td>
              <td>Déficit formativo estructural</td>
            </tr>
            <tr style="background-color: #EBF1F5;">
              <td>Técnico Superior / Tecnológico Superior</td>
              <td style="text-align: right;">1.463</td>
              <td style="text-align: right;">7,63%</td>
              <td>Técnicos (gastronomía general)</td>
            </tr>
            <tr>
              <td>Superior Universitario / Posgrado</td>
              <td style="text-align: right;">2.335</td>
              <td style="text-align: right;">12,17%</td>
              <td>Administradores / Propietarios</td>
            </tr>
            <tr style="font-weight: bold; border-top: 1.5px solid #1F4E79;">
              <td>Total Ocupados en el Segmento</td>
              <td style="text-align: right;">19.178</td>
              <td style="text-align: right;">100,00%</td>
              <td>Universo Ocupacional Cantonal</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Microdatos de personas ENEMDU Anual (INEC, 2025) / Elaboración: Equipo Técnico IAVQ (2026).</div>

        <div style="margin-top: 6pt; border: 1px solid #D9D9D9; padding: 6pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 9. Nivel de Instrucción de los Trabajadores de Cafeterías en Quito (ENEMDU 2025)
          </div>
          <div style="height: 145px; position: relative;">
            <canvas id="chart-graf-09"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 6pt;">
          <strong>Diagnóstico Crítico de la Brecha Formativa:</strong> El hallazgo empírico es contundente: el <strong>80,20% de los trabajadores que operan las barras de café y servicios de bebidas en Quito (15.380 personas) no posee ningún título de educación superior</strong>, ejerciendo su labor a través del aprendizaje empírico y la transmisión informal de pautas operativas. Por el contrario, el segmento con titulación técnica y tecnológica superior representa apenas el <strong>7,63%</strong>, concentrado además en titulaciones de cocina general. Este déficit fundamenta la pertinencia ineludible de formalizar la profesión del barista mediante un título de tercer nivel técnico superior.
        </p>
      </div>
      {get_page_footer(9)}
    </div>
    """

    # ==========================================
    # PÁGINA 10: 2.2. DIAGNÓSTICO ENEMDU (IESS)
    # ==========================================
    pages[10] = f"""
    <div class="word-page" id="page-10-enemdu-iess">
      {get_page_header(10)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Diagnóstico Ocupacional: Seguridad Social e Informalidad Laboral (ENEMDU 2025)</h2>
        
        <p class="word-p">
          La falta de acreditación técnica formal en el mercado de cafeterías y barras genera un efecto directo sobre la precariedad de las condiciones contractuales y la desprotección de los trabajadores. El análisis de los microdatos de afiliación a la seguridad social en la ENEMDU Anual 2025 para el Cantón Quito permite cuantificar la magnitud de la informalidad en este renglón económico.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 7. Cobertura de Afiliación a la Seguridad Social (IESS) en Trabajadores de Cafeterías en Quito (ENEMDU 2025)
        </div>
        <table class="word-table">
          <thead>
            <tr>
              <th style="width: 42%;">Condición de Afiliación al IESS</th>
              <th style="width: 22%; text-align: right;">Población Expandida</th>
              <th style="width: 18%; text-align: right;">Porcentaje</th>
              <th style="width: 18%;">Situación Contractual</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background-color: #FEECEC; font-weight: bold; color: #9C0006;">
              <td>Sin afiliación a la Seguridad Social (IESS)</td>
              <td style="text-align: right;">15.513</td>
              <td style="text-align: right;">80,89%</td>
              <td>Informal / Vulnerable</td>
            </tr>
            <tr style="background-color: #EBF1F5;">
              <td>IESS Seguro General Obligatorio</td>
              <td style="text-align: right;">3.300</td>
              <td style="text-align: right;">17,21%</td>
              <td>Empleo formal con relación</td>
            </tr>
            <tr>
              <td>IESS Afiliación Voluntaria / Seguro Campesino</td>
              <td style="text-align: right;">365</td>
              <td style="text-align: right;">1,90%</td>
              <td>Independiente por cuenta propia</td>
            </tr>
            <tr style="font-weight: bold; border-top: 1.5px solid #1F4E79;">
              <td>Total Trabajadores de Barras y Cafeterías</td>
              <td style="text-align: right;">19.178</td>
              <td style="text-align: right;">100,00%</td>
              <td>100,00%</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: ENEMDU Anual (INEC, 2025) / Elaboración: Equipo Técnico IAVQ (2026).</div>

        <div style="margin-top: 6pt; border: 1px solid #D9D9D9; padding: 6pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 10. Cobertura de Afiliación al IESS en el Sector de Cafeterías en Quito (ENEMDU 2025)
          </div>
          <div style="height: 145px; position: relative;">
            <canvas id="chart-graf-10"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 6pt;">
          <strong>Impacto de la Informalidad y la Política de Titulación Técnica:</strong> La cifra de desprotección social es alarmante: el <strong>80,89% de los trabajadores de cafeterías en Quito carece de cobertura de seguridad social</strong>. Esta condición de vulnerabilidad laboral se encuentra intrínsecamente asociada al estatus de "mano de obra empírica de reemplazo rápido". Las empresas del sector reconocen que la incorporación de Técnicos Superiores debidamente titulados transforma este paradigma, posibilitando la suscripción de contratos estables bajo relación de dependencia con todos los beneficios de ley, al tratarse de personal técnico esencial con capacidad de calibrar equipos, controlar inventarios y reducir mermas operativas.
        </p>
      </div>
      {get_page_footer(10)}
    </div>
    """

    # ==========================================
    # PÁGINA 11: 2.2. RETORNO SALARIAL (ENEMDU)
    # ==========================================
    pages[11] = f"""
    <div class="word-page" id="page-11-enemdu-salario">
      {get_page_header(11)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.2. Retorno Salarial y Prima a la Profesionalización en Cafeterías (ENEMDU 2025)</h2>
        
        <p class="word-p">
          El análisis econométrico de ingresos laborales de la ENEMDU Anual 2025 demuestra con precisión matemática la existencia de un retorno económico significativo asociado a la obtención de un título de educación superior técnica en el sector de alimentos y bebidas del Cantón Quito. Se contrastan los ingresos mensuales reales percibidos por nivel de escolaridad frente al Salario Básico Unificado (SBU) vigente para el año 2026 ($470,00 USD).
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 8. Ingreso Laboral Promedio según Nivel de Instrucción en el Sector Cafeterías en Quito (ENEMDU 2025)
        </div>
        <table class="word-table">
          <thead>
            <tr>
              <th style="width: 32%;">Nivel de Instrucción</th>
              <th style="width: 20%; text-align: right;">Ingreso Promedio</th>
              <th style="width: 22%; text-align: right;">Relación frente al SBU ($470)</th>
              <th style="width: 26%;">Perfil Ocupacional Típico</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Primaria incompleta / completa</td>
              <td style="text-align: right;">$325,40</td>
              <td style="text-align: right; color: #9C0006; font-weight: bold;">-30,77% (Subempleo)</td>
              <td>Auxiliar de limpieza / vajilla</td>
            </tr>
            <tr>
              <td>Secundaria completa (Bachiller)</td>
              <td style="text-align: right;">$412,50</td>
              <td style="text-align: right; color: #9C0006; font-weight: bold;">-12,23% (Bajo SBU)</td>
              <td>Preparador de barra empírico</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td>Técnico Superior Titulado</td>
              <td style="text-align: right; color: #1F4E79;">$546,87</td>
              <td style="text-align: right; color: #1F4E79;">+16,36% (Sobre SBU)</td>
              <td>Barista líder / Calibrador</td>
            </tr>
            <tr>
              <td>Jefatura de Barra / Tostador especialista</td>
              <td style="text-align: right;">$745,00</td>
              <td style="text-align: right; font-weight: bold;">+58,51% (Sobre SBU)</td>
              <td>Head Barista / Maestro Tostador</td>
            </tr>
            <tr>
              <td>Tercer Nivel Universitario General</td>
              <td style="text-align: right;">$685,20</td>
              <td style="text-align: right;">+45,79% (Sobre SBU)</td>
              <td>Administrador general de local</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: ENEMDU Anual (INEC, 2025) / Tabulación salarial: Equipo Técnico IAVQ (2026).</div>

        <div style="margin-top: 6pt; border: 1px solid #D9D9D9; padding: 6pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 11. Comparativa Salarial Promedio por Nivel de Instrucción vs. SBU en Quito (ENEMDU 2025)
          </div>
          <div style="height: 145px; position: relative;">
            <canvas id="chart-graf-11"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 6pt;">
          <strong>Racionalidad Económica del Título Técnico:</strong> Mientras que un trabajador empírico con educación secundaria percibe un salario promedio de $412,50 USD (incumpliendo el SBU legal debido a jornadas parciales o informalidad), el personal con <strong>título de Técnico Superior alcanza un ingreso promedio formal de $546,87 USD</strong>. Esto representa una <strong>prima salarial neta del +32,57%</strong> frente al trabajador empírico y un <strong>+16,36% por encima del SBU oficial</strong>. Para puestos especializados de jefatura de barra y tostado sensorial, el ingreso escala hasta los $745,00 USD. El estudio confirma que la formación técnica genera un retorno económico tangible e inmediato para el egresado.
        </p>
      </div>
      {get_page_footer(11)}
    </div>
    """

    # ==========================================
    # PÁGINA 12: 2.3. TÉRMINOS ACADÉMICOS (RESUMEN POR NIVEL)
    # ==========================================
    pages[12] = f"""
    <div class="word-page" id="page-12-acad-1">
      {get_page_header(12)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.3. Términos Académicos: Oferta Consolidada en el Campo CINE 1013</h2>
        
        <p class="word-p">
          De conformidad con la Clasificación Internacional Normalizada de la Educación (CINE UNESCO), el proyecto curricular se inscribe en el <strong>Campo Detallado 1013 (Servicios de Hotelería, Restaurantes y Catering)</strong>. Para diagnosticar la estructura de la oferta educativa superior, se procesó el catálogo oficial del Sistema Nacional de Información de la Educación Superior del Ecuador (SNIESE / CES, corte 2026), aplicando filtros paramétricos territoriales y por nivel de formación.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 9. Oferta Académica Consolidada por Nivel de Formación en CINE 1013: Gastronomía vs. Barismo (SNIESE 2026)
        </div>
        <table class="word-table" style="font-size: 7.6pt;">
          <thead>
            <tr>
              <th style="width: 32%;">Nivel de Formación (LOES)</th>
              <th style="width: 14%; text-align: center;">Gastronomía Ecuador</th>
              <th style="width: 14%; text-align: center;">Gastronomía Pichincha</th>
              <th style="width: 14%; text-align: center;">Gastronomía Quito</th>
              <th style="width: 13%; text-align: center;">Barismo Previa</th>
              <th style="width: 13%; text-align: center;">Propuesta IAVQ</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Técnico Superior</td>
              <td style="text-align: center;">6</td>
              <td style="text-align: center;">1</td>
              <td style="text-align: center;">1</td>
              <td style="text-align: center; color: #9C0006; font-weight: bold;">0</td>
              <td style="text-align: center; color: #1F4E79; font-weight: bold;">1 (Nuevo)</td>
            </tr>
            <tr>
              <td>Tecnológico Superior</td>
              <td style="text-align: center;">87</td>
              <td style="text-align: center;">30</td>
              <td style="text-align: center;">26</td>
              <td style="text-align: center; color: #9C0006; font-weight: bold;">0</td>
              <td style="text-align: center;">0</td>
            </tr>
            <tr>
              <td>Tecnológico Superior Universitario (TSU)</td>
              <td style="text-align: center;">20</td>
              <td style="text-align: center;">8</td>
              <td style="text-align: center;">5</td>
              <td style="text-align: center; color: #9C0006; font-weight: bold;">0</td>
              <td style="text-align: center;">0</td>
            </tr>
            <tr>
              <td>Tercer Nivel de Grado (Licenciatura / Ingeniería)</td>
              <td style="text-align: center;">19</td>
              <td style="text-align: center;">9</td>
              <td style="text-align: center;">9</td>
              <td style="text-align: center; color: #9C0006; font-weight: bold;">0</td>
              <td style="text-align: center;">0</td>
            </tr>
            <tr>
              <td>Cuarto Nivel / Posgrado (Maestrías)</td>
              <td style="text-align: center;">11</td>
              <td style="text-align: center;">3</td>
              <td style="text-align: center;">3</td>
              <td style="text-align: center; color: #9C0006; font-weight: bold;">0</td>
              <td style="text-align: center;">0</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold; border-top: 1.5px solid #1F4E79;">
              <td>Total Consolidado en el Campo 1013</td>
              <td style="text-align: center;">143</td>
              <td style="text-align: center;">51</td>
              <td style="text-align: center; color: #1F4E79;">44</td>
              <td style="text-align: center; color: #9C0006;">0 (Vacancia)</td>
              <td style="text-align: center; color: #1F4E79;">1</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Catálogo de Oferta Académica SNIESE (CES / SENESCYT, corte 2026) / Elaboración: IAVQ (2026).</div>

        <div style="margin-top: 5pt; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 12. Comparativa de Oferta Vigente por Nivel Formativo en CINE 1013: Gastronomía vs. Barismo
          </div>
          <div style="height: 140px; position: relative;">
            <canvas id="chart-graf-12"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 5pt;">
          <strong>Articulación Conceptual entre Gastronomía y Barismo:</strong> Es indispensable precisar que las cifras macro descritas corresponden al área disciplinar afín de <strong>Gastronomía</strong>, la cual se toma como marco sectorial de referencia para ilustrar la alta demanda formativa que experimenta el sector de la restauración en Quito (44 carreras vigentes, de las cuales 32 son técnico-tecnológicas). No obstante, para la propuesta específica de <strong>Técnico Superior en Barismo, la oferta previa nacional y provincial es estrictamente cero (0)</strong>. No existen programas técnicos ni tecnológicos en la historia del Sistema de Educación Superior del Ecuador dedicados al barismo, confirmando que la propuesta del IAVQ no duplica oferta existente sino que cubre un nicho ocupacional en absoluta vacancia formativa.
        </p>
      </div>
      {get_page_footer(12)}
    </div>
    """

    # ==========================================
    # PÁGINA 13: 2.3. VACANCIA Y BACHILLERES (AMIE)
    # ==========================================
    pages[13] = f"""
    <div class="word-page" id="page-13-acad-2">
      {get_page_header(13)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.3. Términos Académicos: Graduados Históricos y Serie Oficial de Bachilleres (AMIE)</h2>
        
        <p class="word-p">
          Para sustentar el contexto institucional del talento humano graduado y la cohorte inmediata de postulantes, se examinó el Registro Oficial de Títulos de Educación Superior (SENESCYT, período 2012–2024) y la serie histórica del Archivo Maestro de Instituciones Educativas (AMIE 2020–2026) del Ministerio de Educación.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 10. Historial de Titulados Técnicos y Tecnológicos en Gastronomía vs. Barismo (SENESCYT 2012–2024)
        </div>
        <table class="word-table" style="font-size: 7.7pt;">
          <thead>
            <tr>
              <th style="width: 40%;">Campo de Titulación Registrado</th>
              <th style="width: 20%; text-align: center;">Total Nacional (Ecuador)</th>
              <th style="width: 20%; text-align: center;">Pichincha (Provincial)</th>
              <th style="width: 20%; text-align: center;">Cantón Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Tecnología Superior en Gastronomía (Área Afín)</td>
              <td style="text-align: center; font-weight: bold; color: #1F4E79;">6.184</td>
              <td style="text-align: center;">4.110</td>
              <td style="text-align: center;">3.890</td>
            </tr>
            <tr style="background-color: #FEECEC; font-weight: bold; color: #9C0006;">
              <td>Técnico / Tecnólogo Superior en Barismo (Específico)</td>
              <td style="text-align: center;">0</td>
              <td style="text-align: center;">0</td>
              <td style="text-align: center;">0 (Inexistente)</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Registro Nacional de Títulos (SENESCYT, base oficial acumulada a 2024) / Elaboración: IAVQ (2026).</div>
        <p class="word-p" style="font-size: 7.7pt; margin: 2pt 0 4pt 0; color: #555555;">
          <em>Nota metodológica sobre graduados:</em> A nivel nacional existen <strong>6.184 titulados tecnológicos en Gastronomía</strong> (4.110 concentrados en Pichincha). En contraste, la cifra de <strong>0 titulados en Barismo</strong> refleja la inexistencia histórica de carreras en esta disciplina en el Ecuador, y no cohortes recientes sin egresados.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 11. Serie Histórica Oficial de Matrícula en 3.º de Bachillerato en Quito (AMIE 2020–2026)
        </div>
        <table class="word-table" style="font-size: 7.7pt;">
          <thead>
            <tr>
              <th style="width: 16%; text-align: center;">Año Lectivo</th>
              <th style="width: 28%; text-align: right;">Fiscal y Fiscomisional</th>
              <th style="width: 28%; text-align: right;">Particular y Municipal</th>
              <th style="width: 28%; text-align: right;">Total Graduandos Quito</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center;">2020–2021 (COVID)</td>
              <td style="text-align: right;">31.114</td>
              <td style="text-align: right;">17.501</td>
              <td style="text-align: right; font-weight: bold;">48.615</td>
            </tr>
            <tr>
              <td style="text-align: center;">2021–2022</td>
              <td style="text-align: right;">28.140</td>
              <td style="text-align: right;">15.824</td>
              <td style="text-align: right;">43.964</td>
            </tr>
            <tr>
              <td style="text-align: center;">2022–2023</td>
              <td style="text-align: right;">27.710</td>
              <td style="text-align: right;">15.587</td>
              <td style="text-align: right;">43.297</td>
            </tr>
            <tr>
              <td style="text-align: center;">2023–2024</td>
              <td style="text-align: right;">27.887</td>
              <td style="text-align: right;">15.686</td>
              <td style="text-align: right;">43.573</td>
            </tr>
            <tr style="background-color: #F2F7FA;">
              <td style="text-align: center; font-weight: bold;">2024–2025</td>
              <td style="text-align: right;">28.004</td>
              <td style="text-align: right;">15.752</td>
              <td style="text-align: right; font-weight: bold; color: #1F4E79;">43.756</td>
            </tr>
            <tr style="background-color: #EBF1F5; font-weight: bold;">
              <td style="text-align: center;">2025–2026</td>
              <td style="text-align: right;">26.706</td>
              <td style="text-align: right;">15.022</td>
              <td style="text-align: right; color: #1F4E79;">41.728</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Registro Administrativo AMIE (Ministerio de Educación, base 2009–2026) / Elaboración: IAVQ (2026).</div>

        <div style="margin-top: 4pt; border: 1px solid #D9D9D9; padding: 4pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 13. Serie Histórica de Estudiantes de 3.º de Bachillerato en el Cantón Quito (AMIE 2020–2026)
          </div>
          <div style="height: 115px; position: relative;">
            <canvas id="chart-graf-13"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 4pt;">
          <strong>Estabilización Demográfica de la Demanda Potencial:</strong> La serie temporal del AMIE evidencia con precisión la trayectoria de la matrícula de secundaria: tras el máximo coyuntural de 48.615 estudiantes en el periodo 2020–2021 (asociado a la flexibilización escolar durante la pandemia), la cohorte experimentó un ajuste demográfico moderado, situándose en un pico reciente de <strong>43.756 bachilleres en 2024–2025</strong> y estabilizándose en una meseta de <strong>41.728 estudiantes en el ciclo 2025–2026</strong>. Esta meseta cantonal de más de 41.000 graduandos por año asegura un semillero de postulantes sumamente sólido y predecible.
        </p>
      </div>
      {get_page_footer(13)}
    </div>
    """

    # ==========================================
    # PÁGINA 14: 2.4. TÉRMINOS CULTURALES Y TECNOLOGÍA
    # ==========================================
    pages[14] = f"""
    <div class="word-page" id="page-14-cultural">
      {get_page_header(14)}
      <div class="word-content">
        <h1 class="word-heading-1">2. ANÁLISIS DE LAS NECESIDADES DE DESARROLLO (CONTINUACIÓN)</h1>
        <h2 class="word-heading-2">2.4. Términos Culturales y Tendencias Tecnológicas en la Tercera Ola del Café</h2>
        
        <p class="word-p">
          El análisis cultural y tecnológico examina los cambios en los patrones de consumo urbano en el Distrito Metropolitano de Quito. Conforme señalan los reportes sectoriales de la International Coffee Organization (ICO, 2024) y la Specialty Coffee Association (SCA, 2023), el café ha transitado de ser una infusión estimulante tradicional a consolidarse como un producto gourmet con alto contenido identitario, territorial y organoléptico.
        </p>

        <h3 class="word-heading-3">2.4.1. La Tercera Ola del Café y la Valorización del Origen Territorial</h3>
        <p class="word-p">
          El movimiento internacional de la Tercera Ola promueve la trazabilidad rigurosa del grano desde la finca hasta la taza servida. En Pichincha, investigaciones de la Mancomunidad del Chocó Andino (2023) y de la Asociación Nacional de Exportadores de Café del Ecuador (ANECAFE, 2024) destacan el potencial de los microlotes cultivados en las parroquias noroccidentales de Quito (Nanegal, Pacto, Gualea), donde varietales de alta gama como Típica Mejorada, Sidra y Geisha alcanzan perfiles de taza excepcionales (>86 puntos SCA) mediante fermentaciones anaeróbicas y secado controlado.
        </p>

        <h3 class="word-heading-3">2.4.2. Tecnologías de Extracción, Termodinámica del Espresso y Latte Art</h3>
        <p class="word-p">
          De acuerdo con los estándares técnicos de barismo profesional (Rao, 2020; SCA, 2023), la operación de cafeterías de especialidad demanda un dominio riguroso de parámetros físicos y termodinámicos:
        </p>
        <ul style="margin: 0 0 4pt 0; padding-left: 14pt; font-size: 8.9pt; line-height: 1.28;">
          <li><strong>Control Térmico y Presión (PID):</strong> Estabilidad térmica con tolerancias mínimas (+/- 0,2°C) y gestión de curvas de preinfusión para maximizar sólidos solubles (TDS).</li>
          <li><strong>Molienda Micrométrica Gravimétrica:</strong> Distribución bimodal uniforme de partículas para prevenir canalizaciones en la pastilla de café (Rao, 2020).</li>
          <li><strong>Métodos de Filtrado Manual (Brew Bar):</strong> Extracción por goteo e inmersión (V60, Chemex, Aeropress, Prensa Francesa) controlando turbulencia, ratio agua/café y tiempo.</li>
          <li><strong>Química del Agua:</strong> Mineralización controlada (rango SCA de 75 a 150 ppm de dureza total) para asegurar solvencia adecuada de lípidos y ácidos orgánicos.</li>
          <li><strong>Emulsión y Latte Art:</strong> Texturizado térmico de leche a 55°C–65°C para conformar una microespuma satinada mediante desnaturalización proteica controlada.</li>
        </ul>

        <h3 class="word-heading-3">2.4.3. Sostenibilidad, Consumo Consciente y Comercio Justo</h3>
        <p class="word-p">
          El barista actúa como puente pedagógico entre el productor y el consumidor (ANECAFE, 2024). Promueve esquemas de comercio directo (Direct Trade) y consumo consciente, incorporando prácticas de economía circular como el aprovechamiento de la cáscara del café para infusiones y la gestión ecológica de los residuos orgánicos de barra.
        </p>
      </div>
      {get_page_footer(14)}
    </div>
    """

    # ==========================================
    # PÁGINA 15: 3. ARTICULACIÓN CON EL PND 2025–2029
    # ==========================================
    pages[15] = f"""
    <div class="word-page" id="page-15-pnd">
      {get_page_header(15)}
      <div class="word-content">
        <h1 class="word-heading-1">3. ARTICULACIÓN CON EL PLAN NACIONAL DE DESARROLLO (PND 2025–2029)</h1>
        
        <p class="word-p">
          El proyecto curricular del Técnico Superior en Barismo se alinea de forma vinculante con los objetivos estratégicos, políticas públicas y metas nacionales cuantitativas del <strong>Plan Nacional de Desarrollo 2025–2029: "Ecuador No Se Detiene"</strong>, emitido por la Secretaría Nacional de Planificación (2025).
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 12. Matriz de Articulación del Proyecto Curricular con Objetivos, Políticas y Metas del PND 2025–2029
        </div>
        <table class="word-table" style="font-size: 7.3pt;">
          <thead>
            <tr>
              <th style="width: 14%;">Eje Estratégico</th>
              <th style="width: 24%;">Objetivo Nacional</th>
              <th style="width: 28%;">Políticas Públicas Vinculadas</th>
              <th style="width: 34%;">Metas Nacionales Cuantitativas al 2029</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Eje Social:</strong><br>Desarrollo Humano</td>
              <td><strong>Objetivo 2:</strong> Garantizar educación superior pertinente, inclusiva y con equidad territorial.</td>
              <td><strong>Política 2.1:</strong> Fortalecer la oferta técnica y tecnológica pertinente articulada al sector productivo.<br><strong>Política 2.3:</strong> Promover modalidades de estudio flexibles e híbridas para ampliar la cobertura territorial.</td>
              <td><strong>Meta 2.1.1:</strong> Elevar la tasa bruta de matrícula en educación superior técnica y tecnológica superior al <strong>48,60%</strong> para 2029.<br><strong>Meta 2.3.2:</strong> Incrementar la oferta académica en modalidades híbridas y virtuales al <strong>35,00%</strong> del sistema técnico.</td>
            </tr>
            <tr>
              <td><strong>Eje Económico:</strong><br>Empleo y Producción</td>
              <td><strong>Objetivo 4:</strong> Promover el trabajo digno, fomentar el empleo juvenil formal y dinamizar encadenamientos productivos.</td>
              <td><strong>Política 4.1:</strong> Impulsar la inserción laboral juvenil formal mediante acreditación técnica.<br><strong>Política 4.3:</strong> Dinamizar encadenamientos y microemprendimientos en alimentos y bebidas.</td>
              <td><strong>Meta 4.1.3:</strong> Reducir la tasa de desempleo en jóvenes de 18 a 24 años a nivel urbano al <strong>12,00%</strong>.<br><strong>Meta 4.3.1:</strong> Incrementar en un <strong>25,00%</strong> los contratos formales con afiliación al IESS en servicios gastronómicos.</td>
            </tr>
            <tr>
              <td><strong>Eje Productivo:</strong><br>Innovación y Valor</td>
              <td><strong>Objetivo 5:</strong> Fortalecer la diversificación productiva, agregación de valor y exportaciones no tradicionales.</td>
              <td><strong>Política 5.2:</strong> Potenciar la agregación de valor y diferenciación con trazabilidad de origen.<br><strong>Política 5.4:</strong> Fomentar la bioeconomía y el comercio justo en cadenas agropecuarias.</td>
              <td><strong>Meta 5.2.2:</strong> Incrementar en un <strong>15,00%</strong> las ventas y exportaciones de productos agroalimentarios de especialidad.<br><strong>Meta 5.4.1:</strong> Vincular al menos 500 pequeños productores de café a cadenas de valor directo.</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: Plan Nacional de Desarrollo 2025–2029 (Secretaría Nacional de Planificación, 2025) / Elaboración: IAVQ (2026).</div>

        <h2 class="word-heading-2">3.1. Justificación de la Modalidad Híbrida frente a las Metas del PND</h2>
        <p class="word-p">
          La modalidad híbrida responde de manera exacta al mandato de la Política 2.3 y Meta 2.3.2 del PND. Al integrar aulas virtuales síncronas para materias teóricas (botánica, química, costos, normativas de inocuidad) con prácticas presenciales intensivas en los laboratorios de barismo del IAVQ (calibración de molinos, extracción y latte art), se optimiza el tiempo de traslado y se garantiza el acceso a estudiantes trabajadores y residentes de parroquias rurales de Pichincha.
        </p>
      </div>
      {get_page_footer(15)}
    </div>
    """

    # ==========================================
    # PÁGINA 16: 4. ARTICULACIÓN TERRITORIAL (PDOT Y PMDOT)
    # ==========================================
    pages[16] = f"""
    <div class="word-page" id="page-16-territorial">
      {get_page_header(16)}
      <div class="word-content">
        <h1 class="word-heading-1">4. ARTICULACIÓN CON LA PLANIFICACIÓN TERRITORIAL</h1>
        
        <p class="word-p">
          El estudio de pertinencia articula de forma directa los instrumentos de planificación local: el <strong>Plan de Desarrollo y Ordenamiento Territorial de la Provincia de Pichincha 2023–2027 (PDOT)</strong> y el <strong>Plan Metropolitano de Desarrollo y Ordenamiento Territorial de Quito (PMDOT 2024–2033, Ordenanza No. 004-2024)</strong>.
        </p>

        <div style="font-size: 8.5pt; font-weight: bold; color: #1F4E79; margin: 3pt 0 2pt 0;">
          Tabla 13. Matriz de Articulación con el PDOT Pichincha y el PMDOT Quito (Vigencia a 2033)
        </div>
        <table class="word-table" style="font-size: 7.7pt;">
          <thead>
            <tr>
              <th style="width: 25%;">Instrumento Territorial</th>
              <th style="width: 35%;">Objetivo / Política Estratégica</th>
              <th style="width: 40%;">Aporte y Vinculación Curricular del IAVQ</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>PDOT Pichincha (2023–2027)</strong><br>Gobierno Provincial de Pichincha</td>
              <td>Eje Productivo Agroecológico: Fortalecer la cadena de valor del café de especialidad del Chocó Andino y Noroccidente de Pichincha como polo de bioeconomía.</td>
              <td>Capacitación de técnicos capaces de catar, clasificar y comercializar los microlotes de Nanegal, Pacto y Gualea a precios justos de especialidad.</td>
            </tr>
            <tr>
              <td><strong>PMDOT Quito (2024–2033)</strong><br>Municipio D.M. Quito (Ord. 004-2024)</td>
              <td>Eje Económico y Competitividad: Reactivación económica de distritos turísticos y gastronómicos (La Floresta, La Mariscal, Centro Histórico y Cumbayá).</td>
              <td>Abastecimiento de talento humano técnico calificado para elevar la calidad del servicio en los circuitos gastronómicos metropolitanos.</td>
            </tr>
            <tr>
              <td><strong>PUGS Quito (2024–2033)</strong><br>Plan de Uso y Gestión del Suelo</td>
              <td>Consolidación de centralidades urbanas con actividades de servicios y comercio vecinal de bajo impacto y alto valor cultural.</td>
              <td>Fomento de emprendimientos de tostadurías urbanas y microcafeterías sostenibles con buenas prácticas de manufactura.</td>
            </tr>
          </tbody>
        </table>
        <div class="table-source">Fuente: PDOT Pichincha (2024) / PMDOT Quito (MDMQ, Ordenanza 004-2024) / Elaboración: IAVQ (2026).</div>

        <div style="margin-top: 5pt; border: 1px solid #D9D9D9; padding: 5pt; background: #FAFAFA;">
          <div style="font-size: 8pt; font-weight: bold; color: #1F4E79; text-align: center; margin-bottom: 2pt;">
            Gráfico 14. Ejes Estratégicos Territoriales Articulados con la Carrera de Barismo
          </div>
          <div style="height: 130px; position: relative;">
            <canvas id="chart-graf-14"></canvas>
          </div>
        </div>

        <p class="word-p" style="margin-top: 5pt;">
          <strong>Sinergia entre la Zona de Producción y la Zona de Consumo:</strong> Pichincha reúne una condición geográfica y económica única: cuenta con zonas de producción de café de especialidad de altura en el Noroccidente del cantón y, al mismo tiempo, alberga el mayor mercado de consumo urbano y turístico del país en el Distrito Metropolitano de Quito. La carrera de Técnico Superior en Barismo del IAVQ cierra la brecha técnica entre ambos extremos de la cadena, en perfecta consonancia con el horizonte de planificación al 2033.
        </p>
      </div>
      {get_page_footer(16)}
    </div>
    """

    return pages

if __name__ == "__main__":
    pages = generate_pages_9_to_16()
    print(f"Successfully generated {len(pages)} pages (Pages 9 to 16).")
    for p_num in sorted(pages.keys()):
        print(f"Page {p_num}: {len(pages[p_num])} characters")
