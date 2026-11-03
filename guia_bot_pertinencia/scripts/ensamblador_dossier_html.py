# -*- coding: utf-8 -*-
"""
Ensamblador del Dossier Completo de 24 Páginas:
Técnico Superior en Barismo - Instituto Superior Tecnológico de Artes Visuales de Quito (IAVQ)
"""

import os
import shutil
from modulo_1_social_economico import generate_pages_1_to_8
from modulo_2_academico_planificacion import generate_pages_9_to_16
from modulo_3_mercado_demanda import generate_pages_17_to_24

def build_full_html():
    p1_8 = generate_pages_1_to_8()
    p9_16 = generate_pages_9_to_16()
    p17_24 = generate_pages_17_to_24()

    all_pages = {}
    all_pages.update(p1_8)
    all_pages.update(p9_16)
    all_pages.update(p17_24)

    pages_html = "\n".join([all_pages[i] for i in range(1, 25)])

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Estudio de Pertinencia Curricular — Técnico Superior en Barismo (IAVQ)</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
  <style>
    /* Microsoft Word Native Typography and Layout */
    body {{
      font-family: Calibri, 'Segoe UI', Arial, sans-serif;
      background-color: #d1d5db; /* Neutral Word canvas */
      color: #000000;
      margin: 0;
      padding: 24px 0;
    }}

    /* Standard Word Hyperlink Styles */
    a {{
      color: #0563C1;
      text-decoration: underline;
    }}
    a:visited {{
      color: #0563C1;
    }}
    a:hover {{
      color: #004B91;
    }}
    .word-toc a {{
      color: #000000;
      text-decoration: none;
      display: flex;
      align-items: baseline;
      width: 100%;
    }}
    .word-toc a:hover .toc-title {{
      text-decoration: underline;
      color: #0563C1;
    }}
    .word-toc a:hover .toc-page {{
      color: #0563C1;
      font-weight: bold;
    }}

    .word-page {{
      width: 21.59cm;
      min-height: 27.94cm;
      padding: 2.2cm 2.4cm 2.0cm 2.4cm;
      margin: 20px auto;
      background: #ffffff;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2), 0 0 1px rgba(0, 0, 0, 0.1);
      box-sizing: border-box;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }}

    @media print {{
      @page {{
        size: letter portrait;
        margin: 1.8cm 2.0cm 1.8cm 2.0cm;
      }}
      body {{
        background: #ffffff !important;
        padding: 0 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
      .no-print {{
        display: none !important;
      }}
      .word-page {{
        margin: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        width: 100% !important;
        min-height: 100vh !important;
      }}
    }}

    .word-header {{
      border-bottom: 1px solid #7f7f7f;
      padding-bottom: 3pt;
      margin-bottom: 14pt;
      font-size: 8.5pt;
      color: #595959;
      display: flex;
      justify-content: space-between;
    }}

    .word-content {{
      flex-grow: 1;
      display: block;
    }}

    .word-footer {{
      border-top: 1px solid #7f7f7f;
      padding-top: 4pt;
      margin-top: auto;
      font-size: 8.5pt;
      color: #595959;
      display: flex;
      justify-content: space-between;
    }}

    /* Word Headings */
    .word-heading-1 {{
      font-size: 13pt;
      font-weight: bold;
      color: #1F4E79;
      text-transform: uppercase;
      margin-top: 8pt;
      margin-bottom: 4pt;
      letter-spacing: 0.2px;
      line-height: 1.25;
    }}

    .word-heading-2 {{
      font-size: 11.5pt;
      font-weight: bold;
      color: #2E75B6;
      margin-top: 7pt;
      margin-bottom: 3pt;
      line-height: 1.25;
    }}

    .word-heading-3 {{
      font-size: 10.5pt;
      font-weight: bold;
      color: #1F4E79;
      margin-top: 5pt;
      margin-bottom: 2pt;
      line-height: 1.25;
    }}

    .word-p {{
      font-size: 10pt;
      line-height: 1.28;
      color: #000000;
      text-align: justify;
      margin-top: 0;
      margin-bottom: 5pt;
    }}

    .word-callout {{
      background-color: #F2F5F9;
      border: 1px solid #D9E1F2;
      border-left: 4.5px solid #1F4E79;
      padding: 7pt 10pt;
      margin: 5pt 0;
      font-size: 9.2pt;
      line-height: 1.32;
      color: #1A1A1A;
    }}

    /* Formal Word Table Styles */
    .word-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 4pt 0 2pt 0;
      font-size: 8.5pt;
      color: #000000;
    }}

    .word-table th {{
      background-color: #1F4E79;
      color: #ffffff;
      font-weight: bold;
      padding: 4pt 6pt;
      border: 1px solid #1F4E79;
      text-align: left;
    }}

    .word-table td {{
      padding: 3pt 6pt;
      border: 1px solid #D9D9D9;
      vertical-align: middle;
    }}

    .word-table tbody tr:nth-child(even) {{
      background-color: #F9FBFD;
    }}

    .table-source {{
      font-size: 7.5pt;
      color: #595959;
      font-style: italic;
      margin-top: 2pt;
      margin-bottom: 6pt;
      text-align: right;
    }}

    /* Word Table of Contents */
    .word-toc {{
      font-size: 8.5pt;
      line-height: 1.35;
      margin-top: 6pt;
    }}

    .toc-group-title {{
      font-weight: bold;
      color: #1F4E79;
      font-size: 9pt;
      margin-top: 6pt;
      margin-bottom: 2pt;
      border-bottom: 1px solid #1F4E79;
      padding-bottom: 1.5pt;
    }}

    .toc-row {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 1.5pt;
    }}

    .toc-level-1 {{
      font-weight: bold;
      color: #1F4E79;
      margin-top: 2.5pt;
    }}

    .toc-level-2 {{
      padding-left: 10pt;
      font-weight: normal;
      color: #262626;
    }}

    .toc-title {{
      flex-shrink: 0;
      max-width: 82%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .toc-dots {{
      flex-grow: 1;
      border-bottom: 1.5px dotted #595959;
      margin: 0 4pt 2.5pt 4pt;
      min-width: 15px;
      height: 0;
    }}

    .toc-page {{
      flex-shrink: 0;
      font-weight: normal;
      text-align: right;
      min-width: 16px;
      font-variant-numeric: tabular-nums;
      color: #000000;
    }}

    /* Word Cover Page Styles */
    .word-cover-container {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      text-align: center;
      padding: 1.2cm 0 0.5cm 0;
      box-sizing: border-box;
    }}

    .word-cover-institution {{
      font-size: 16pt;
      font-weight: bold;
      color: #1F4E79;
      letter-spacing: 0.5px;
      margin: 0;
    }}

    .word-cover-subinst {{
      font-size: 11pt;
      font-weight: bold;
      color: #595959;
      margin: 2pt 0 0 0;
    }}

    .word-cover-divider {{
      width: 100px;
      height: 2px;
      background-color: #1F4E79;
      margin: 10pt auto;
    }}

    .word-cover-dept {{
      font-size: 8.5pt;
      font-weight: bold;
      color: #7f7f7f;
      letter-spacing: 1px;
    }}

    .word-cover-title {{
      font-size: 19pt;
      font-weight: bold;
      color: #000000;
      margin: 12pt 0;
      letter-spacing: 0.5px;
    }}

    .word-cover-project-tag {{
      font-size: 8.5pt;
      font-weight: bold;
      color: #2E75B6;
      letter-spacing: 1px;
      margin-bottom: 2pt;
    }}

    .word-cover-career-box {{
      margin: 10pt auto;
      max-width: 530px;
      text-align: center;
      background-color: #F2F5F9;
      border: 1.5px solid #1F4E79;
      border-radius: 2px;
      padding: 8pt 14pt;
    }}

    .word-cover-career-label {{
      font-size: 8.5pt;
      font-weight: bold;
      color: #595959;
      margin: 0 0 2pt 0;
    }}

    .word-cover-career-name {{
      font-size: 13pt;
      font-weight: bold;
      color: #1F4E79;
      margin: 0 0 6pt 0;
    }}

    .word-cover-itinerary-label {{
      font-size: 8.5pt;
      font-weight: bold;
      color: #595959;
      margin: 0 0 2pt 0;
    }}

    .word-cover-itinerary-list {{
      margin: 0;
      padding-left: 14pt;
      font-size: 8.5pt;
      line-height: 1.35;
      color: #000000;
    }}

    .word-cover-meta-table {{
      width: 100%;
      max-width: 520px;
      margin: 10pt auto 0 auto;
      border-collapse: collapse;
      font-size: 8.5pt;
      text-align: left;
    }}

    .word-cover-meta-table td {{
      padding: 2.5pt 6pt;
      border: none;
    }}

    .word-cover-meta-table .meta-label {{
      font-weight: bold;
      color: #333333;
      width: 42%;
    }}

    .word-cover-meta-table .meta-val {{
      color: #000000;
    }}

    .word-cover-date {{
      font-size: 10pt;
      font-weight: bold;
      color: #333333;
      margin: 0;
    }}

    .word-cover-place {{
      font-size: 9pt;
      color: #595959;
      margin: 2pt 0 0 0;
    }}
  </style>
</head>
<body>

  <!-- TOP CONTROLS NAVBAR -->
  <div class="no-print" style="position: fixed; top: 10px; right: 10px; z-index: 9999; display: flex; align-items: center; gap: 8px; background: #ffffff; padding: 5px 12px; border: 1px solid #7f7f7f; box-shadow: 0 2px 6px rgba(0,0,0,0.15); font-family: Calibri, 'Segoe UI', Arial, sans-serif; font-size: 11px; color: #000000;">
    <span style="font-weight: bold; color: #1F4E79;">2. Documento Oficial: Técnico Superior en Barismo (IAVQ)</span>
    <a href="dossier_mecanica_motos_vista_word.html" style="color: #2E75B6; text-decoration: none; font-weight: normal; margin-left: 4px;">[Ver 1. Mecánica de Motos (IST POLITEC)]</a>
    <span style="color: #7f7f7f;">|</span>
    <label for="page-selector" style="color: #333333;">Página:</label>
    <select id="page-selector" onchange="document.getElementById(this.value).scrollIntoView({{behavior:'smooth'}})" style="font-family: inherit; font-size: 11px; padding: 2px 6px; border: 1px solid #7f7f7f; background: #ffffff; color: #000000; cursor: pointer;">
      <option value="page-01-cover">P01. Portada Institucional</option>
      <option value="page-02-indice">P02. Índice General de Contenidos</option>
      <option value="page-03-intro">P03. 1. Introducción y Antecedentes</option>
      <option value="page-04-social-1">P04. 2.1. Población y Demografía (Tabla 1 + Gráf 1-2)</option>
      <option value="page-05-social-2">P05. 2.1. Mercado Laboral Juvenil (Gráf 3-6)</option>
      <option value="page-06-econ-1">P06. 2.2. Tejido Productivo CIIU 56 (Tablas 2-3)</option>
      <option value="page-07-econ-2">P07. 2.2. Facturación y Constitución (Tabla 4 + Gráf 7-8)</option>
      <option value="page-08-supercias">P08. 2.2. Ranking Empleadores SUPERCIAS (Tabla 5)</option>
      <option value="page-09-enemdu-edu">P09. 2.2. Diagnóstico Formativo ENEMDU (Tabla 6 + Gráf 9)</option>
      <option value="page-10-enemdu-iess">P10. 2.2. Seguridad Social e Informalidad (Tabla 7 + Gráf 10)</option>
      <option value="page-11-enemdu-salario">P11. 2.2. Retorno Salarial a la Titulación (Tabla 8 + Gráf 11)</option>
      <option value="page-12-acad-1">P12. 2.3. Oferta Campo CINE 1013 (Tabla 9 + Gráf 12)</option>
      <option value="page-13-acad-2">P13. 2.3. Vacancia y Bachilleres AMIE (Tablas 10-11 + Gráf 13)</option>
      <option value="page-14-cultural">P14. 2.4. Tercera Ola y Tecnología</option>
      <option value="page-15-pnd">P15. 3. Articulación PND 2025–2029 (Tabla 12)</option>
      <option value="page-16-territorial">P16. 4. Articulación PDOT y PMDOT (Tabla 13 + Gráf 14)</option>
      <option value="page-17-solucion">P17. 5. Contribución de Graduados (Tabla 14)</option>
      <option value="page-18-demanda-emp-1">P18. 6.1. Demanda Empresarial: Cochran</option>
      <option value="page-19-demanda-emp-2">P19. 6.1. Resultados 380 Cafeterías</option>
      <option value="page-20-brecha">P20. 6.1. Brecha Laboral y Absorción</option>
      <option value="page-21-estudiantil-1">P21. 6.2. Demanda Estudiantil: Cochran</option>
      <option value="page-22-malla">P22. 6.2. Proyección y Malla Curricular</option>
      <option value="page-23-conclusiones">P23. 7. Conclusiones Institucionales</option>
      <option value="page-24-referencias">P24. 8. Referencias y Matriz de Auditoría</option>
    </select>
    <button onclick="window.print()" style="font-family: inherit; font-size: 11px; padding: 2px 8px; border: 1px solid #1F4E79; background: #1F4E79; color: #ffffff; cursor: pointer;">Imprimir / PDF</button>
  </div>

  <!-- 24 WORD PAGES -->
  {pages_html}

  <!-- CHART.JS INITIALIZATION SCRIPT -->
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      Chart.register(ChartDataLabels);

      const colorNavy = '#1F4E79';
      const colorBlue = '#2E75B6';
      const colorLightBlue = '#5B9BD5';
      const colorGray = '#7F7F7F';
      const colorLightGray = '#D9D9D9';
      const colorRed = '#C00000';
      const colorOrange = '#ED7D31';

      // Gráfico 1: Grupo etario 18-24 años: Ecuador, Pichincha y Quito (2026 vs. 2035)
      new Chart(document.getElementById('chart-graf-01'), {{
        type: 'bar',
        data: {{
          labels: ['Ecuador', 'Pichincha', 'Quito'],
          datasets: [
            {{
              label: 'Año 2026',
              data: [2160613, 360644, 301883],
              backgroundColor: colorNavy
            }},
            {{
              label: 'Año 2035',
              data: [2211630, 353871, 296214],
              backgroundColor: colorLightBlue
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'top', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v) => (v/1000).toFixed(0) + 'k',
              font: {{ size: 7, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.5, weight: 'bold' }} }} }}
          }}
        }}
      }});

      // Gráfico 2: Proporción de la Juventud (18-24 años) en el Cantón Quito (2026)
      new Chart(document.getElementById('chart-graf-02'), {{
        type: 'doughnut',
        data: {{
          labels: ['Jóvenes 18-24 años (10,50%)', 'Resto de la Población (89,50%)'],
          datasets: [{{
            data: [301883, 2573192],
            backgroundColor: [colorNavy, colorLightGray]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'bottom', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{ display: false }}
          }}
        }}
      }});

      // Gráfico 3: Población del Cantón Quito por Nivel de Educación (ENEMDU 2025)
      new Chart(document.getElementById('chart-graf-03'), {{
        type: 'bar',
        data: {{
          labels: ['Básica', 'Secundaria', 'Sup. Univ.', 'Media', 'Primaria', 'Sup. No Univ.', 'Postgrado'],
          datasets: [{{
            data: [24.35, 21.33, 17.22, 14.04, 13.25, 5.61, 2.56],
            backgroundColor: [colorBlue, colorNavy, colorLightBlue, colorOrange, colorGray, colorNavy, colorGray]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v) => v.toFixed(1) + '%',
              font: {{ size: 7, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ max: 30, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 6.8 }} }} }}
          }}
        }}
      }});

      // Gráfico 4: Distribución de la Población del Cantón Quito por Sexo (ENEMDU 2025)
      new Chart(document.getElementById('chart-graf-04'), {{
        type: 'pie',
        data: {{
          labels: ['Mujeres (52,0%)', 'Hombres (48,0%)'],
          datasets: [{{
            data: [52.0, 48.0],
            backgroundColor: [colorBlue, colorNavy]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'bottom', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{ display: false }}
          }}
        }}
      }});

      // Gráfico 5: Asistencia a Clases de la Juventud 18-24 años en Quito (ENEMDU 2025)
      new Chart(document.getElementById('chart-graf-05'), {{
        type: 'doughnut',
        data: {{
          labels: ['No Asiste (50,23%)', 'Sí Asiste (49,77%)'],
          datasets: [{{
            data: [50.23, 49.77],
            backgroundColor: [colorRed, colorNavy]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'bottom', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{ display: false }}
          }}
        }}
      }});

      // Gráfico 6: Tasa de Desempleo Juvenil (18-24 años) vs. Promedio Cantonal (ENEMDU 2025)
      new Chart(document.getElementById('chart-graf-06'), {{
        type: 'bar',
        data: {{
          labels: ['Juventud 18-24 años', 'Promedio Cantonal Quito'],
          datasets: [{{
            data: [22.58, 7.24],
            backgroundColor: [colorRed, colorNavy]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v) => v.toFixed(2) + '%',
              font: {{ size: 7.5, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ max: 28, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.5, weight: 'bold' }} }} }}
          }}
        }}
      }});

      // Gráfico 7: Ventas REEM Quito
      new Chart(document.getElementById('chart-graf-07'), {{
        type: 'line',
        data: {{
          labels: ['2012', '2015', '2018', '2021', '2022', '2023', '2024'],
          datasets: [{{
            label: 'Ventas (M$)',
            data: [963.88, 1150.30, 1252.40, 1135.20, 1255.40, 1335.50, 1434.44],
            borderColor: colorNavy,
            backgroundColor: colorNavy,
            borderWidth: 2,
            pointRadius: 3,
            fill: false
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'top',
              align: 'top',
              formatter: (v) => '$' + v.toFixed(0) + 'M',
              font: {{ size: 7.5, weight: 'bold' }},
              color: colorNavy
            }}
          }},
          scales: {{
            y: {{ min: 800, max: 1600, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.5 }} }} }}
          }}
        }}
      }});

      // Gráfico 8: Constitución Empresas SUPERCIAS
      new Chart(document.getElementById('chart-graf-08'), {{
        type: 'bar',
        data: {{
          labels: ['Histórico (Pre-2020)', 'Auge Reciente (2020-2026)'],
          datasets: [{{
            data: [36, 123],
            backgroundColor: [colorGray, colorNavy]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v, ctx) => v + ' (' + ((v/159)*100).toFixed(1) + '%)',
              font: {{ size: 7.5, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ max: 150, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.5, weight: 'bold' }} }} }}
          }}
        }}
      }});

      // Gráfico 9: Instrucción Baristas ENEMDU
      new Chart(document.getElementById('chart-graf-09'), {{
        type: 'doughnut',
        data: {{
          labels: ['Secundaria Empírica (61,86%)', 'Primaria / Sin Inst. (18,34%)', 'Universitario (12,17%)', 'Técnico Superior (7,63%)'],
          datasets: [{{
            data: [61.86, 18.34, 12.17, 7.63],
            backgroundColor: [colorOrange, colorRed, colorLightBlue, colorNavy]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'right', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{ display: false }}
          }}
        }}
      }});

      // Gráfico 10: IESS Baristas ENEMDU
      new Chart(document.getElementById('chart-graf-10'), {{
        type: 'pie',
        data: {{
          labels: ['Sin IESS / Informal (80,89%)', 'IESS Obligatorio (17,21%)', 'IESS Voluntario (1,90%)'],
          datasets: [{{
            data: [80.89, 17.21, 1.90],
            backgroundColor: [colorRed, colorNavy, colorLightBlue]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'right', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{ display: false }}
          }}
        }}
      }});

      // Gráfico 11: Salarios ENEMDU
      new Chart(document.getElementById('chart-graf-11'), {{
        type: 'bar',
        data: {{
          labels: ['Primaria', 'Secundaria', 'SBU 2026', 'Técnico Sup.', 'Head Barista'],
          datasets: [{{
            data: [325.40, 412.50, 470.00, 546.87, 745.00],
            backgroundColor: [colorRed, colorOrange, colorGray, colorNavy, colorBlue]
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v) => '$' + v.toFixed(0),
              font: {{ size: 7.5, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ max: 850, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.5 }} }} }}
          }}
        }}
      }});

      // Gráfico 12: Oferta Consolidada por Nivel Formativo en Quito (Gastronomía vs Barismo)
      new Chart(document.getElementById('chart-graf-12'), {{
        type: 'bar',
        data: {{
          labels: ['Tecnológico Sup.', 'Grado Universitario', 'Tec. Sup. Univ.', 'Posgrado / Maestría', 'Técnico Superior'],
          datasets: [
            {{
              label: 'Gastronomía Quito (Total 44)',
              data: [26, 9, 5, 3, 1],
              backgroundColor: colorNavy
            }},
            {{
              label: 'Barismo Quito (Oferta Previa: 0)',
              data: [0, 0, 0, 0, 0],
              backgroundColor: colorRed
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'top', labels: {{ font: {{ size: 7.5 }} }} }},
            datalabels: {{
              anchor: 'end',
              align: 'top',
              formatter: (v) => v,
              font: {{ size: 7.5, weight: 'bold' }},
              color: '#000000'
            }}
          }},
          scales: {{
            y: {{ max: 32, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.0 }} }} }}
          }}
        }}
      }});

      // Gráfico 13: Bachilleres AMIE Quito (2020-2026)
      new Chart(document.getElementById('chart-graf-13'), {{
        type: 'line',
        data: {{
          labels: ['2020-2021', '2021-2022', '2022-2023', '2023-2024', '2024-2025', '2025-2026'],
          datasets: [{{
            label: 'Bachilleres Quito',
            data: [48615, 43964, 43297, 43573, 43756, 41728],
            borderColor: colorNavy,
            backgroundColor: colorNavy,
            borderWidth: 2,
            pointRadius: 4,
            fill: false
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{
              anchor: 'top',
              align: 'top',
              formatter: (v) => (v/1000).toFixed(1) + 'k',
              font: {{ size: 7.5, weight: 'bold' }},
              color: colorNavy
            }}
          }},
          scales: {{
            y: {{ min: 38000, max: 52000, ticks: {{ font: {{ size: 7.5 }} }} }},
            x: {{ ticks: {{ font: {{ size: 7.0 }} }} }}
          }}
        }}
      }});

      // Gráfico 14: Articulación Territorial
      new Chart(document.getElementById('chart-graf-14'), {{
        type: 'radar',
        data: {{
          labels: ['Café Chocó Andino', 'Circuitos Urbanos', 'Bioeconomía', 'Turismo Sostenible', 'Agregación Valor'],
          datasets: [{{
            label: 'Alineación Estratégica IAVQ',
            data: [95, 90, 85, 90, 95],
            borderColor: colorNavy,
            backgroundColor: 'rgba(31, 78, 121, 0.25)',
            borderWidth: 2,
            pointRadius: 3
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            datalabels: {{ display: false }}
          }},
          scales: {{
            r: {{ min: 50, max: 100, ticks: {{ display: false }} }}
          }}
        }}
      }});

    }});
  </script>
</body>
</html>
"""
    return html_template

if __name__ == "__main__":
    html_content = build_full_html()
    
    out_dir = "DOCUMENTOS_HTML_PERTINENCIA_BARISMO"
    os.makedirs(out_dir, exist_ok=True)
    local_file = os.path.join(out_dir, "dossier_barismo_iavq_vista_word.html")
    with open(local_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"File created successfully: {local_file} ({len(html_content):,} bytes)")

    repo_dir = r"C:\Users\kevin\Documents\GitHub\Planes_Pertinencia_Ejemplos\Plan_Pertinencia_Example"
    repo_file = os.path.join(repo_dir, "dossier_barismo_iavq_vista_word.html")
    shutil.copy2(local_file, repo_file)
    print(f"Copied to repo: {repo_file}")
