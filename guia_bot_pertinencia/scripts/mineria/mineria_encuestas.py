# -*- coding: utf-8 -*-
"""
SCRIPT DE MINERÍA DE DATOS: ENCUESTAS DE CAMPO Y MODELO ECONOMÉTRICO
Dirección de Planificación y Pertinencia Curricular (CES / CACES)

Este script realiza el procesamiento estadístico de las encuestas aplicadas
a empleadores y bachilleres, ejecutando:
1. Verificación del tamaño muestral mediante la fórmula de Cochran con población finita.
2. Tabulación y distribución de frecuencias de intención de contratación a 3 años.
3. Extrapolación formal mediante el Factor de Expansión muestral (F = N / n).
4. Estimación de la Demanda Laboral Bruta Anual y la Brecha Laboral Neta Insatisfecha.
5. Cálculo de la Demanda Estudiantil Inicial y Proyección Quinquenal con tasas del INEC.
"""

import os
import sys
import json
import numpy as np

# Configuración de salida en consola para caracteres especiales
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def calcular_muestreo_cochran(universo_n, nivel_confianza=0.95, margen_error=0.05, p_varianza=0.50):
    """
    Calcula el tamaño de muestra estadísticamente representativo según Cochran
    con corrección por población finita.
    """
    z_scores = {0.90: 1.645, 0.95: 1.960, 0.99: 2.576}
    z = z_scores.get(nivel_confianza, 1.960)
    q = 1.0 - p_varianza

    # Fórmula para población infinita
    n_0 = (z**2 * p_varianza * q) / (margen_error**2)

    # Corrección para población finita
    n_corregido = n_0 / (1.0 + ((n_0 - 1.0) / universo_n))
    
    return int(np.ceil(n_corregido))


def procesar_encuesta_empleadores(universo_empresas_n=16673, muestra_n=380, distribucion_contratacion=None, oferta_egreso_anual=60):
    """
    Procesa las respuestas patronales y deriva la brecha laboral anual insatisfecha.
    """
    print(f"[MERCADO LABORAL] Procesando demanda de empresas...")
    print(f"                  Universo N = {universo_empresas_n:,} | Muestra n = {muestra_n}")

    # Distribución por defecto validada en la investigación de campo
    if distribucion_contratacion is None:
        distribucion_contratacion = {
            "0_trabajadores": {"porcentaje": 90.43, "puestos": 0},
            "1_trabajador":   {"porcentaje": 8.51,  "puestos": 1},
            "2_trabajadores": {"porcentaje": 0.80,  "puestos": 2},
            "3_a_5_trabajadores": {"porcentaje": 0.27, "puestos": 3} # Promedio conservador = 3
        }

    # 1. Plazas directas reportadas en la muestra de 380 empresas
    plazas_muestra = 0.0
    for categoria, datos in distribucion_contratacion.items():
        empresas_cat = (datos["porcentaje"] / 100.0) * muestra_n
        plazas_cat = empresas_cat * datos["puestos"]
        plazas_muestra += plazas_cat

    plazas_muestra_redondeadas = int(round(plazas_muestra))

    # 2. Factor de Expansión Muestral
    factor_expansion = universo_empresas_n / float(muestra_n)

    # 3. Extrapolación al universo total para el trienio
    demanda_trienal_total = plazas_muestra * factor_expansion
    demanda_anual_bruta = int(round(demanda_trienal_total / 3.0))

    # 4. Brecha Laboral Neta (considerando competencia y egreso previo)
    # Rango de absorción institucional: egreso anual proyectado del instituto (60-90 cupos)
    brecha_laboral_anual_neta = demanda_anual_bruta - int(demanda_anual_bruta * 0.40) # 40% captado por otras áreas o empíricos
    
    tasa_empleabilidad_institucional = min(100.0, (brecha_laboral_anual_neta / oferta_egreso_anual) * 100.0)

    print(f"[MERCADO LABORAL] Resultados:")
    print(f"                  - Factor de Expansión (F): {factor_expansion:.4f}")
    print(f"                  - Plazas requeridas en la muestra: {plazas_muestra_redondeadas} puestos")
    print(f"                  - Demanda Laboral Bruta Anual: {demanda_anual_bruta:,} puestos/año")
    print(f"                  - Brecha Neta Insatisfecha: {brecha_laboral_anual_neta:,} puestos/año")
    print(f"                  - Empleabilidad Proyectada del Instituto: {tasa_empleabilidad_institucional:.1f}%")

    return {
        "universo_empresas_reem": universo_empresas_n,
        "muestra_encuestada": muestra_n,
        "factor_expansion_f": round(factor_expansion, 4),
        "plazas_en_muestra": plazas_muestra_redondeadas,
        "distribucion_respuestas_pct": {k: v["porcentaje"] for k, v in distribucion_contratacion.items()},
        "demanda_trienio_expandida": int(round(demanda_trienal_total)),
        "demanda_anual_bruta": demanda_anual_bruta,
        "brecha_laboral_anual_neta": brecha_laboral_anual_neta,
        "oferta_graduados_instituto_anual": oferta_egreso_anual,
        "tasa_empleabilidad_egresados_pct": tasa_empleabilidad_institucional
    }


def procesar_encuesta_estudiantes(universo_bachilleres_n=41728, muestra_n=381, tasa_alta_probabilidad=0.0184, cupos_planificados=70, tasas_inec=None):
    """
    Procesa las respuestas estudiantiles y proyecta la demanda para el quinquenio 2026-2030.
    """
    print(f"[DEMANDA ESTUDIANTIL] Procesando aspirantes de bachillerato...")
    print(f"                      Universo N = {universo_bachilleres_n:,} | Muestra n = {muestra_n}")
    print(f"                      Tasa Muestral de Alta Probabilidad = {tasa_alta_probabilidad * 100:.2f}%")

    if tasas_inec is None:
        # Tasas oficiales de crecimiento poblacional cantonal del INEC para Quito
        tasas_inec = {
            2027: 0.0063, # +0.63%
            2028: 0.0061, # +0.61%
            2029: 0.0058, # +0.58%
            2030: 0.0055  # +0.55%
        }

    # 1. Demanda Base Año 1 (2026)
    demanda_base_2026 = int(round(universo_bachilleres_n * tasa_alta_probabilidad))

    # 2. Proyección Quinquenal
    proyeccion_quinquenio = {
        2026: {
            "universo_bachilleres": universo_bachilleres_n,
            "tasa_crecimiento_inec": 0.0,
            "demanda_estudiantil_potencial": demanda_base_2026,
            "cupos_oferta_institucional": cupos_planificados,
            "cobertura_demanda_pct": round((demanda_base_2026 / cupos_planificados) * 100.0, 1)
        }
    }

    u_actual = float(universo_bachilleres_n)
    for anio, tasa in sorted(tasas_inec.items()):
        u_actual = u_actual * (1.0 + tasa)
        d_anio = int(round(u_actual * tasa_alta_probabilidad))
        proyeccion_quinquenio[anio] = {
            "universo_bachilleres": int(round(u_actual)),
            "tasa_crecimiento_inec": round(tasa * 100.0, 2),
            "demanda_estudiantil_potencial": d_anio,
            "cupos_oferta_institucional": cupos_planificados,
            "cobertura_demanda_pct": round((d_anio / cupos_planificados) * 100.0, 1)
        }

    print(f"[DEMANDA ESTUDIANTIL] Demanda Base 2026: {demanda_base_2026:,} aspirantes vs. {cupos_planificados} cupos.")
    print(f"[DEMANDA ESTUDIANTIL] Demanda Proyectada 2030: {proyeccion_quinquenio[2030]['demanda_estudiantil_potencial']:,} aspirantes.")

    return {
        "universo_bachilleres_base": universo_bachilleres_n,
        "muestra_encuestada": muestra_n,
        "tasa_alta_probabilidad_pct": round(tasa_alta_probabilidad * 100.0, 2),
        "cupos_institucionales_iniciales": cupos_planificados,
        "proyeccion_quinquenal_2026_2030": proyeccion_quinquenio
    }


def ejecutar_mineria_encuestas(universo_emp, universo_bach, out_json):
    """Ejecuta los dos modelos de mercado y genera el informe integrado."""
    cochran_emp = calcular_muestreo_cochran(universo_emp)
    cochran_bach = calcular_muestreo_cochran(universo_bach)
    
    mercado_laboral = procesar_encuesta_empleadores(universo_empresas_n=universo_emp, muestra_n=cochran_emp)
    demanda_estudiantil = procesar_encuesta_estudiantes(universo_bachilleres_n=universo_bach, muestra_n=cochran_bach)

    resultado = {
        "metadatos": {
            "fuente": "Investigación de Campo Directa - CEDEPRO / IAVQ",
            "metodologia_muestreo": "Muestreo Probabilístico Estratificado (Fórmula de Cochran con Población Finita)"
        },
        "diseno_muestral": {
            "empresas": {"universo_n": universo_emp, "muestra_calculada_n": cochran_emp, "confianza": 0.95, "error": 0.05},
            "estudiantes": {"universo_n": universo_bach, "muestra_calculada_n": cochran_bach, "confianza": 0.95, "error": 0.05}
        },
        "demanda_laboral": mercado_laboral,
        "demanda_estudiantil": demanda_estudiantil
    }

    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
        
    print(f"[MERCADO Y DEMANDA] Modelo cuantitativo consolidado exportado a: {out_json}")
    return resultado


if __name__ == "__main__":
    OUT_JSON = r"guia_bot_pertinencia\datos_extraidos\mercado_demanda_consolidado.json"
    ejecutar_mineria_encuestas(universo_emp=16673, universo_bach=41728, out_json=OUT_JSON)

