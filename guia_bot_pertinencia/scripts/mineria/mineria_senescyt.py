# -*- coding: utf-8 -*-
"""
SCRIPT DE MINERÍA DE DATOS: OFERTA ACADÉMICA Y TITULADOS (SENESCYT / SNIESE)
Dirección de Planificación y Pertinencia Curricular (CES / CACES)

Este script realiza la extracción, normalización y conteo de graduados históricos
a partir de los registros oficiales de SENESCYT y el catálogo SNIESE:
1. Conteo de titulados a nivel nacional y provincial por campo de conocimiento.
2. Segregación rigurosa por nivel de formación (Técnico/Tecnológico vs. Grado Universitario).
3. Identificación de Institutos Superiores Tecnológicos (IST) formadores en la provincia.
4. Detección automática de carreras emergentes (alerta de cero titulados previos).
"""

import os
import sys
import json
import pandas as pd

# Configuración de salida en consola para caracteres especiales
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def normalizar_nombre_ies(nombre):
    """Normaliza variantes ortográficas de nombres de Institutos de Educación Superior."""
    if not isinstance(nombre, str):
        return "OTRA INSTITUCIÓN"
    n = nombre.upper()
    if 'SUDAMERICANO' in n:
        return 'Instituto Superior Tecnológico Sudamericano'
    if 'ILADES' in n or 'LOS ANDES DE ESTUDIOS' in n:
        return 'Instituto Superior Tecnológico ILADES'
    if 'RUMIÑAHUI' in n:
        return 'Instituto Superior Tecnológico Rumiñahui'
    if 'ITI' in n or 'INTERNACIONAL ITI' in n:
        return 'Instituto Superior Tecnológico Internacional ITI'
    if 'YAVIRAC' in n:
        return 'Instituto Superior Tecnológico Turismo y Patrimonio Yavirac'
    if 'PACIFICO' in n or 'PACÍFICO' in n:
        return 'Instituto Superior Tecnológico El Pacífico'
    if 'JAPON' in n or 'JAPÓN' in n:
        return 'Instituto Superior Tecnológico Japón'
    if 'ISMAC' in n:
        return 'Instituto Superior Tecnológico ISMAC'
    if 'CENESTUR' in n:
        return 'Instituto Superior Tecnológico Cenestur'
    if 'UNIVERSITEC' in n:
        return 'Instituto Superior Tecnológico Universitec'
    return nombre.strip().title()


def extraer_titulados_senescyt(ruta_excel_o_csv, terminos_busqueda, provincia_objetivo="PICHINCHA"):
    """
    Procesa las bases de títulos de la SENESCYT buscando coincidencias de términos
    en el título profesional y segregando por nivel y territorio.
    """
    print(f"[SENESCYT] Analizando títulos registrados para términos: {terminos_busqueda}")
    print(f"           Provincia de análisis: {provincia_objetivo}")

    if not os.path.exists(ruta_excel_o_csv):
        print(f"[SENESCYT] Error: No se localizó el archivo {ruta_excel_o_csv}.")
        return None

    # Si es Excel (formato consolidado SENESCYT)
    if ruta_excel_o_csv.endswith('.xlsx'):
        try:
            print("[SENESCYT] Cargando hoja 'Por Carrera y Título'...")
            df_carrera = pd.read_excel(ruta_excel_o_csv, sheet_name='Por Carrera y Título')
            print("[SENESCYT] Cargando hoja 'Por Universidad (IES)'...")
            df_ies = pd.read_excel(ruta_excel_o_csv, sheet_name='Por Universidad (IES)')
            
            df_carrera['TOT_TITULOS'] = pd.to_numeric(df_carrera['TOT_TITULOS'], errors='coerce').fillna(0).astype(int)
            ies_prov = df_ies[['nombre_universidad', 'provincia_final', 'tipo_ies']].drop_duplicates()
            df = pd.merge(df_carrera, ies_prov, on='nombre_universidad', how='left')
        except Exception as e:
            print(f"[SENESCYT] Error leyendo archivo Excel: {e}")
            return None
    else:
        # Si es CSV
        df = pd.read_csv(ruta_excel_o_csv, sep=';', encoding='latin1', low_memory=False)
        if 'TOT_TITULOS' not in df.columns and 'TOTAL' in df.columns:
            df['TOT_TITULOS'] = df['TOTAL']
        df['TOT_TITULOS'] = pd.to_numeric(df['TOT_TITULOS'], errors='coerce').fillna(0).astype(int)

    # Construir patrón regex de búsqueda
    patron = "|".join(terminos_busqueda)
    
    col_titulo = 'nombre_titulo' if 'nombre_titulo' in df.columns else 'TITULO'
    col_nivel = 'nivel_formacion' if 'nivel_formacion' in df.columns else 'NIVEL'
    col_prov = 'provincia_final' if 'provincia_final' in df.columns else 'PROVINCIA'
    col_ies = 'nombre_universidad' if 'nombre_universidad' in df.columns else 'INSTITUCION'

    # Filtrar coincidencias en el título
    match = df[df[col_titulo].astype(str).str.contains(patron, case=False, na=False)].copy()
    
    # Segregar por nivel
    tech = match[match[col_nivel].astype(str).str.contains('TECN', case=False, na=False)].copy()
    grado = match[match[col_nivel].astype(str).str.contains('GRADO|TERCER NIVEL|LICENCIATURA|INGENIERIA', case=False, na=False)].copy()

    # Totales Nacionales
    total_tech_nacional = int(tech['TOT_TITULOS'].sum())
    total_grado_nacional = int(grado['TOT_TITULOS'].sum())
    total_disciplina_nacional = int(match['TOT_TITULOS'].sum())

    # Totales Provinciales
    tech_prov = tech[tech[col_prov].astype(str).str.upper() == provincia_objetivo.upper()].copy()
    grado_prov = grado[grado[col_prov].astype(str).str.upper() == provincia_objetivo.upper()].copy()
    
    total_tech_prov = int(tech_prov['TOT_TITULOS'].sum())
    total_grado_prov = int(grado_prov['TOT_TITULOS'].sum())

    # Desglose por Instituto en la provincia
    tech_prov['ies_normalizada'] = tech_prov[col_ies].apply(normalizar_nombre_ies)
    desglose_ies = tech_prov.groupby('ies_normalizada')['TOT_TITULOS'].sum().sort_values(ascending=False).to_dict()

    print(f"[SENESCYT] Resultados Consolidados:")
    print(f"           - Titulados Tecnológicos Nacional: {total_tech_nacional:,}")
    print(f"           - Titulados Tecnológicos en {provincia_objetivo}: {total_tech_prov:,}")
    print(f"           - Titulados Universitarios en {provincia_objetivo}: {total_grado_prov:,}")

    # Verificar si el término exacto es cero (ej. Barismo)
    termino_especifico = terminos_busqueda[0] if len(terminos_busqueda) > 0 else ""
    match_especifico = df[df[col_titulo].astype(str).str.contains(termino_especifico, case=False, na=False)]
    titulos_especificos = int(match_especifico['TOT_TITULOS'].sum())

    resultado = {
        "metadatos": {
            "fuente": "SENESCYT - Sistema Nacional de Información de la Educación Superior del Ecuador (SNIESE 2025)",
            "provincia": provincia_objetivo,
            "terminos_busqueda": terminos_busqueda,
            "termino_especifico_propuesta": termino_especifico
        },
        "totales_disciplina_macro": {
            "nacional_tecnologico": total_tech_nacional,
            "nacional_universitario_grado": total_grado_nacional,
            "nacional_total": total_disciplina_nacional,
            "provincial_tecnologico": total_tech_prov,
            "provincial_universitario_grado": total_grado_prov,
            "provincial_total": total_tech_prov + total_grado_prov
        },
        "desglose_institutos_tecnologicos_provincia": desglose_ies,
        "evaluacion_carrera_especifica": {
            "titulados_historicos_carrera_especifica": titulos_especificos,
            "es_carrera_nueva_sin_titulados": (titulos_especificos == 0),
            "nota_aclaratoria": (
                f"La propuesta específica registra exactamente {titulos_especificos} titulados históricos "
                f"en los registros oficiales de SENESCYT, lo que fundamenta su carácter innovador y vacancia "
                f"absoluta de oferta en el territorio. Las cifras macro reportadas corresponden al área afín de formación."
            )
        }
    }

    return resultado


def ejecutar_mineria_senescyt(ruta_base, terminos, provincia, ruta_salida_json):
    """Ejecuta la extracción de SENESCYT y exporta a JSON."""
    resultado = extraer_titulados_senescyt(ruta_base, terminos, provincia_objetivo=provincia)
    if resultado:
        os.makedirs(os.path.dirname(ruta_salida_json), exist_ok=True)
        with open(ruta_salida_json, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
        print(f"[SENESCYT] Reporte guardado en: {ruta_salida_json}")
    return resultado


if __name__ == "__main__":
    EXCEL_SENESCYT = r"BD\Titulos Nacionales y Extranjeros\Datos_Senescyt_2025\Titulos_Senescyt_Ecuador_2025.xlsx"
    OUT_JSON = r"guia_bot_pertinencia\datos_extraidos\senescyt_titulados_consolidado.json"
    
    # Términos para el área de Barismo y Gastronomía
    TERMINOS = ['BARISMO', 'GASTRONOM', 'CULINAR', 'COCIN', 'ALIMENTOS Y BEBIDAS']
    ejecutar_mineria_senescyt(EXCEL_SENESCYT, TERMINOS, provincia="PICHINCHA", ruta_salida_json=OUT_JSON)

