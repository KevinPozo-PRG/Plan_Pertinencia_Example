# -*- coding: utf-8 -*-
"""
MÓDULO DE CONFIGURACIÓN Y PARÁMETROS DEL PROYECTO
Estudio de Pertinencia Curricular de Educación Superior (CES / CACES)

Este archivo centraliza todas las variables institucionales, taxonómicas,
demográficas y estadísticas del proyecto curricular para su reutilización por analistas de datos.
"""

CONFIG = {
    # 1. Identidad Institucional y Proyecto
    "institucion": "INSTITUTO SUPERIOR TECNOLÓGICO DE ARTES VISUALES DE QUITO",
    "siglas_institucion": "IAVQ",
    "condicion_institucion": "Condición Superior Universitaria",
    "carrera": "TÉCNICO SUPERIOR EN BARISMO",
    "nivel_formacion": "Tercer Nivel Técnico Superior",
    "modalidad": "Modalidad Híbrida",
    "vigencia_anios": 5,
    "total_horas_malla": 2800,
    "periodos_academicos": 4,

    # 2. Itinerarios Curriculares Propuestos
    "itinerarios": [
        "Itinerario 1: Barismo de Especialidad, Catación Sensorial y Tueste Artesanal",
        "Itinerario 2: Gestión Operativa de Barras, Emprendimiento y Control de Calidad"
    ],

    # 3. Delimitación Territorial y Taxonomía Oficial
    "provincia": "PICHINCHA",
    "canton": "QUITO",
    "campo_amplio_cine": "10 Servicios",
    "campo_especifico_cine": "101 Servicios Personales",
    "campo_detallado_cine": "1013 Servicios de Hotelería, Restaurantes y Catering",
    "ciiu_seccion": "Sección I: Actividades de Alojamiento y de Servicio de Comidas",
    "ciiu_division": "División 56: Actividades de servicios de comidas y bebidas",
    "ciuo_ocupaciones": [
        "5132 Camareros de barra",
        "7515 Elaboradores y catadores de bebidas"
    ],

    # 4. Parámetros Demográficos y Muestrales (Cochran)
    "universo_empresas_reem": 16673,
    "muestra_empresas": 380,
    "universo_bachilleres_amie": 41728,
    "muestra_bachilleres": 385,
    "nivel_confianza_z": 1.96,  # 95%
    "error_muestral_e": 0.05,   # 5%
    "varianza_pq": 0.25,        # p=0.50, q=0.50 (máxima dispersión)

    # 5. Tasas Oficiales de Crecimiento Demográfico Cantonal (INEC Proyecciones Revisión 2024)
    "tasas_crecimiento_inec_quito": {
        2027: 0.0063,  # +0.63%
        2028: 0.0061,  # +0.61%
        2029: 0.0058,  # +0.58%
        2030: 0.0055   # +0.55%
    },

    # 6. Demanda Estudiantil y Oferta Institucional
    "tasa_alta_probabilidad_matricula": 0.0184,  # 1.84% según encuesta muestral
    "cupos_anuales_planificados": {
        2026: 70,   # 2 paralelos de 35
        2027: 85,   # 2 paralelos de 42
        2028: 100,  # 3 paralelos de 33
        2029: 110,  # 3 paralelos de 36
        2030: 120   # 3 paralelos de 40
    },

    # 7. Horizonte de Planificación Territorial
    "pnd_periodo": "2025–2029",
    "pdot_pichincha_periodo": "2023–2027",
    "pmdot_quito_horizonte": "2024–2033"  # Ordenanza Metropolitana No. 004-2024
}

