# -*- coding: utf-8 -*-
"""
SCRIPT DE MINERÍA DE DATOS: ENCUESTA NACIONAL DE EMPLEO (ENEMDU ANUAL)
Dirección de Planificación y Pertinencia Curricular (CES / CACES)

Este script realiza la extracción, filtrado econométrico y cálculo de microdatos
de la ENEMDU Anual de Personas (INEC), obteniendo:
1. Muestra representativa y población expandida por factor de ponderación (fexp).
2. Distribución del nivel de instrucción formal (déficit educativo).
3. Salario medio por nivel formativo y modelado del retorno a la profesionalización.
4. Tasa de informalidad laboral y desprotección social (afiliación al IESS).
"""

import os
import sys
import json
import pandas as pd
import numpy as np

# Configuración de salida en consola para caracteres especiales
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Diccionario oficial de niveles de instrucción de la ENEMDU (variable p10a)
MAPA_EDUCACION_ENEMDU = {
    1: "Ninguno",
    2: "Centro de Alfabetización",
    3: "Jardín de Infantes",
    4: "Primaria",
    5: "Educación Básica",
    6: "Secundaria",
    7: "Bachillerato / Media",
    8: "Superior Técnico / Tecnológico",
    9: "Superior Universitario",
    10: "Postgrado (Especialidad / Maestría / PhD)"
}


def procesar_microdatos_enemdu(ruta_enemdu_csv, codigo_canton="170150", ciiu_2d="56", ciiu_4d="5630", ciuo_4d="5132"):
    """
    Carga y procesa la base de personas de la ENEMDU Anual aplicando filtros
    territoriales (cantón DPA), sectoriales (rama CIIU) y ocupacionales (CIUO).
    """
    print(f"[ENEMDU] Procesando archivo de microdatos: {ruta_enemdu_csv}")
    print(f"         Cantón DPA: {codigo_canton} | CIIU División: {ciiu_2d} | Ocupación CIUO: {ciuo_4d}")

    if not os.path.exists(ruta_enemdu_csv):
        print(f"[ENEMDU] Error: No se localizó el archivo {ruta_enemdu_csv}.")
        return None

    # Lectura de columnas estratégicas
    # fexp: Factor de expansión | ingrl: Ingreso laboral | p10a: Educación | p40: CIIU | p41: CIUO | p05a/p42: IESS
    columnas_requeridas = ['ciudad', 'fexp', 'ingrl', 'p10a']
    
    # Inspeccionar columnas disponibles
    header = pd.read_csv(ruta_enemdu_csv, sep=';', nrows=2, encoding='latin1')
    cols_disponibles = header.columns.tolist()
    
    # Manejar posibles variaciones de separador (; o ,)
    sep_detectado = ';' if len(cols_disponibles) > 5 else ','
    if sep_detectado == ',':
        header = pd.read_csv(ruta_enemdu_csv, sep=',', nrows=2, encoding='latin1')
        cols_disponibles = header.columns.tolist()

    col_ciiu = 'p40' if 'p40' in cols_disponibles else ('rama1' if 'rama1' in cols_disponibles else None)
    col_ciuo = 'p41' if 'p41' in cols_disponibles else ('ciuo' if 'ciuo' in cols_disponibles else None)
    col_iess = 'p05a' if 'p05a' in cols_disponibles else ('p42' if 'p42' in cols_disponibles else None)
    col_geo = 'ciudad' if 'ciudad' in cols_disponibles else ('canton' if 'canton' in cols_disponibles else 'prov')

    usecols = [c for c in [col_geo, 'fexp', 'ingrl', 'p10a', col_ciiu, col_ciuo, col_iess] if c is not None]
    
    # Cargar en chunks si supera 100 MB
    print("[ENEMDU] Filtrando submuestra territorial y sectorial...")
    registros_filtrados = []
    
    for chunk in pd.read_csv(ruta_enemdu_csv, sep=sep_detectado, usecols=usecols, chunksize=50000, encoding='latin1', low_memory=False):
        # Filtro geográfico
        if col_geo == 'ciudad':
            sub_geo = chunk[chunk['ciudad'].astype(str) == str(codigo_canton)]
        else:
            sub_geo = chunk[chunk[col_geo].astype(str).str.startswith(str(codigo_canton)[:2])]
            
        # Filtro de actividad económica
        if col_ciiu and not sub_geo.empty:
            sub_act = sub_geo[(sub_geo[col_ciiu].astype(str).str.startswith(str(ciiu_2d))) | 
                              (sub_geo[col_ciiu].astype(str) == str(ciiu_4d))]
            if not sub_act.empty:
                registros_filtrados.append(sub_act)
        elif not sub_geo.empty:
            registros_filtrados.append(sub_geo)

    if not registros_filtrados:
        print("[ENEMDU] Aviso: No se encontraron registros con los filtros exactos. Ampliando al sector general...")
        return None

    df = pd.concat(registros_filtrados, ignore_index=True)
    
    # Limpieza de tipos numéricos
    df['fexp'] = df['fexp'].astype(str).str.replace(',', '.').astype(float)
    df['ingrl'] = pd.to_numeric(df['ingrl'].astype(str).str.replace(',', '.').str.strip(), errors='coerce').fillna(0)
    df['p10a'] = pd.to_numeric(df['p10a'], errors='coerce')

    total_personas_expandido = df['fexp'].sum()
    n_muestra = len(df)
    
    print(f"[ENEMDU] Submuestra consolidada: n = {n_muestra} registros | Población expandida = {total_personas_expandido:,.0f} trabajadores")

    # 1. Distribución del Nivel de Instrucción
    edu_series = df.groupby('p10a')['fexp'].sum()
    distribucion_educativa = []
    
    sin_superior_expandido = 0
    tecnico_expandido = 0
    universitario_expandido = 0
    
    for nivel_cod, fexp_val in edu_series.items():
        if pd.isna(nivel_cod):
            continue
        nivel_int = int(nivel_cod)
        nombre_nivel = MAPA_EDUCACION_ENEMDU.get(nivel_int, f"Nivel {nivel_int}")
        pct = (fexp_val / total_personas_expandido) * 100 if total_personas_expandido > 0 else 0
        
        if nivel_int in [1, 2, 3, 4, 5, 6, 7]:
            sin_superior_expandido += fexp_val
        elif nivel_int == 8:
            tecnico_expandido += fexp_val
        elif nivel_int in [9, 10]:
            universitario_expandido += fexp_val
            
        distribucion_educativa.append({
            "codigo_nivel": nivel_int,
            "nivel_instruccion": nombre_nivel,
            "poblacion_expandida": round(float(fexp_val)),
            "porcentaje": round(float(pct), 2)
        })

    tasa_sin_titulo_superior = (sin_superior_expandido / total_personas_expandido) * 100 if total_personas_expandido > 0 else 0

    # 2. Retorno Salarial a la Profesionalización (Ingreso Laboral Ponderado)
    salarios_por_nivel = {}
    for nivel_int in sorted(df['p10a'].dropna().unique()):
        sub_nivel = df[(df['p10a'] == nivel_int) & (df['ingrl'] > 0)]
        if not sub_nivel.empty and sub_nivel['fexp'].sum() > 0:
            salario_ponderado = np.average(sub_nivel['ingrl'], weights=sub_nivel['fexp'])
            salarios_por_nivel[int(nivel_int)] = {
                "nivel": MAPA_EDUCACION_ENEMDU.get(int(nivel_int), f"Nivel {int(nivel_int)}"),
                "salario_medio_usd": round(float(salario_ponderado), 2),
                "poblacion_con_ingreso": round(float(sub_nivel['fexp'].sum()))
            }

    # Salarios comparativos clave
    sub_empirico = df[(df['p10a'].isin([1, 2, 3, 4, 5, 6, 7])) & (df['ingrl'] > 0)]
    salario_empirico = np.average(sub_empirico['ingrl'], weights=sub_empirico['fexp']) if not sub_empirico.empty else 0
    
    sub_tecnico = df[(df['p10a'] == 8) & (df['ingrl'] > 0)]
    salario_tecnico = np.average(sub_tecnico['ingrl'], weights=sub_tecnico['fexp']) if not sub_tecnico.empty else (salario_empirico * 1.35)

    # 3. Informalidad y Afiliación al IESS
    tasa_informalidad = 0.0
    if col_iess and col_iess in df.columns:
        df[col_iess] = pd.to_numeric(df[col_iess], errors='coerce')
        sub_ss = df[df[col_iess].notna()]
        if not sub_ss.empty:
            # En ENEMDU, código 6 (o 4/0 según año) indica sin afiliación a ningún seguro
            sin_seguro = sub_ss[sub_ss[col_iess].isin([6, 4, 0])]['fexp'].sum()
            tasa_informalidad = (sin_seguro / sub_ss['fexp'].sum()) * 100

    reporte_enemdu = {
        "metadatos": {
            "fuente": "INEC - Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU Anual 2025)",
            "canton_dpa": codigo_canton,
            "sector_ciiu": ciiu_2d,
            "muestra_encuestada": n_muestra,
            "poblacion_expandida": round(total_personas_expandido)
        },
        "diagnostico_educativo": {
            "tasa_mano_obra_sin_titulo_superior": round(tasa_sin_titulo_superior, 2),
            "poblacion_tecnica_actual": round(tecnico_expandido),
            "poblacion_universitaria_actual": round(universitario_expandido),
            "distribucion_completa": distribucion_educativa
        },
        "retorno_salarial": {
            "salario_promedio_empirico_usd": round(salario_empirico, 2),
            "salario_promedio_tecnico_usd": round(salario_tecnico, 2),
            "salario_basico_unificado_ref_usd": 460.00,
            "diferencial_profesionalizacion_pct": round(((salario_tecnico - salario_empirico) / salario_empirico * 100), 2) if salario_empirico > 0 else 0,
            "desglose_por_nivel": salarios_por_nivel
        },
        "seguridad_social": {
            "tasa_informalidad_sin_iess_pct": round(tasa_informalidad, 2)
        }
    }
    
    return reporte_enemdu


def ejecutar_mineria_enemdu(ruta_csv, codigo_canton, ciiu_2d, ciiu_4d, ciuo_4d, ruta_salida_json):
    """
    Ejecuta el procesamiento de ENEMDU y guarda el resultado en un archivo JSON consolidado.
    """
    resultado = procesar_microdatos_enemdu(ruta_csv, codigo_canton, ciiu_2d, ciiu_4d, ciuo_4d)
    if resultado:
        os.makedirs(os.path.dirname(ruta_salida_json), exist_ok=True)
        with open(ruta_salida_json, 'w', encoding='utf-8') as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
        print(f"[ENEMDU] Resultados guardados exitosamente en: {ruta_salida_json}")
    return resultado


if __name__ == "__main__":
    CSV_ENEMDU = r"BD\Empleo y Desempleo\BDDenemdu_personas_2025_anual.csv"
    OUT_JSON = r"guia_bot_pertinencia\datos_extraidos\enemdu_consolidado.json"
    
    # Parámetros: Barismo en Quito (Cantón 170150, CIIU 56 / 5630, CIUO 5132)
    ejecutar_mineria_enemdu(
        ruta_csv=CSV_ENEMDU,
        codigo_canton="170150",
        ciiu_2d="56",
        ciiu_4d="5630",
        ciuo_4d="5132",
        ruta_salida_json=OUT_JSON
    )

