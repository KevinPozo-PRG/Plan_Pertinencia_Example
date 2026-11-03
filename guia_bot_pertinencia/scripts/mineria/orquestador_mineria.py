# -*- coding: utf-8 -*-
"""
ORQUESTADOR GENERAL DE LA FASE DE MINERÍA DE DATOS
Dirección de Planificación y Pertinencia Curricular (CES / CACES)

Este script ejecuta de manera secuencial los módulos de minería y extracción
de datos sobre las bases oficiales del Estado ecuatoriano:
1. mineria_supercias.py      -> Directorio y Balances de Compañías
2. mineria_enemdu.py         -> Encuesta de Empleo, Educación y Salarios
3. mineria_senescyt.py       -> Oferta Académica y Titulados Históricos
4. mineria_mineduc_amie.py   -> Matrícula Histórica de 3ro de Bachillerato
5. mineria_reem_sri.py       -> Registro de Empresas y Plazas de Trabajo
6. mineria_encuestas.py      -> Muestreo Cochran, Demanda Laboral y Estudiantil

Genera una carpeta centralizada 'datos_extraidos/' con todos los resúmenes JSON
listos para alimentar 'config_parametros.py' y los generadores del dossier HTML.
"""

import os
import sys
import json
import time

# Configuración de salida en consola para caracteres especiales
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Importar los submódulos de minería
try:
    from mineria_supercias import ejecutar_mineria_supercias
    from mineria_enemdu import ejecutar_mineria_enemdu
    from mineria_senescyt import ejecutar_mineria_senescyt
    from mineria_mineduc_amie import ejecutar_mineria_amie
    from mineria_reem_sri import ejecutar_mineria_reem
    from mineria_encuestas import ejecutar_mineria_encuestas
except ImportError:
    # Soporte para ejecución desde la raíz o scripts/
    sys.path.append(os.path.dirname(__file__))
    from mineria_supercias import ejecutar_mineria_supercias
    from mineria_enemdu import ejecutar_mineria_enemdu
    from mineria_senescyt import ejecutar_mineria_senescyt
    from mineria_mineduc_amie import ejecutar_mineria_amie
    from mineria_reem_sri import ejecutar_mineria_reem
    from mineria_encuestas import ejecutar_mineria_encuestas


def ejecutar_pipeline_completo(ruta_raiz_bd="BD", carpeta_salida="guia_bot_pertinencia/datos_extraidos", config_proyecto=None):
    """
    Ejecuta el pipeline de minería completo para un proyecto curricular.
    """
    inicio = time.time()
    print("================================================================================")
    print("PIPELINE DE MINERÍA DE DATOS Y EXTRACCIÓN OFICIAL (CES / CACES - ECUADOR)")
    print("================================================================================")

    if config_proyecto is None:
        # Configuración por defecto: Barismo y Gestión de Cafeterías en Quito
        config_proyecto = {
            "carrera": "Técnico Superior en Barismo y Gestión de Cafeterías",
            "canton": "QUITO",
            "canton_dpa": "170150",
            "provincia": "PICHINCHA",
            "ciiu_seccion": "I",
            "ciiu_division": "56",
            "ciiu_clase": "5630",
            "ciuo_ocupacion": "5132",
            "terminos_titulos": ['BARISMO', 'GASTRONOM', 'CULINAR', 'COCIN', 'ALIMENTOS Y BEBIDAS']
        }

    os.makedirs(carpeta_salida, exist_ok=True)
    reporte_general = {}

    # 1. MINERÍA SUPERCIAS
    print("\n--- PASO 1: MINERÍA DE SUPERINTENDENCIA DE COMPAÑÍAS ---")
    xlsx_super = os.path.join(ruta_raiz_bd, "Directorio_Companias_Supercias", "directorio_companias.xlsx")
    csv_rank = os.path.join(ruta_raiz_bd, "Ranking_Companias_Supercias", "bi_ranking.csv")
    out_super = os.path.join(carpeta_salida, "supercias_consolidado.json")
    try:
        reporte_general["supercias"] = ejecutar_mineria_supercias(
            xlsx_super, csv_rank, 
            ciiu=config_proyecto["ciiu_clase"], 
            canton=config_proyecto["canton"], 
            provincia=config_proyecto["provincia"], 
            ruta_salida_json=out_super
        )
    except Exception as e:
        print(f"[ERROR] En minería SUPERCIAS: {e}")

    # 2. MINERÍA ENEMDU
    print("\n--- PASO 2: MINERÍA DE ENCUESTA NACIONAL DE EMPLEO (ENEMDU) ---")
    csv_enemdu = os.path.join(ruta_raiz_bd, "Empleo y Desempleo", "BDDenemdu_personas_2025_anual.csv")
    out_enemdu = os.path.join(carpeta_salida, "enemdu_consolidado.json")
    try:
        reporte_general["enemdu"] = ejecutar_mineria_enemdu(
            ruta_csv=csv_enemdu,
            codigo_canton=config_proyecto["canton_dpa"],
            ciiu_2d=config_proyecto["ciiu_division"],
            ciiu_4d=config_proyecto["ciiu_clase"],
            ciuo_4d=config_proyecto["ciuo_ocupacion"],
            ruta_salida_json=out_enemdu
        )
    except Exception as e:
        print(f"[ERROR] En minería ENEMDU: {e}")

    # 3. MINERÍA SENESCYT / SNIESE
    print("\n--- PASO 3: MINERÍA DE OFERTA ACADÉMICA Y TITULADOS (SENESCYT) ---")
    excel_senescyt = os.path.join(ruta_raiz_bd, "Titulos Nacionales y Extranjeros", "Datos_Senescyt_2025", "Titulos_Senescyt_Ecuador_2025.xlsx")
    out_senescyt = os.path.join(carpeta_salida, "senescyt_titulados_consolidado.json")
    try:
        reporte_general["senescyt"] = ejecutar_mineria_senescyt(
            ruta_base=excel_senescyt,
            terminos=config_proyecto["terminos_titulos"],
            provincia=config_proyecto["provincia"],
            ruta_salida_json=out_senescyt
        )
    except Exception as e:
        print(f"[ERROR] En minería SENESCYT: {e}")

    # 4. MINERÍA MINEDUC (AMIE)
    print("\n--- PASO 4: MINERÍA DE COHORTE DE BACHILLERATO (MINEDUC) ---")
    excel_amie = os.path.join(ruta_raiz_bd, "MINEDUC Administracion", "registro-administrativo-historico_2009-2024-fin.xlsx")
    out_amie = os.path.join(carpeta_salida, "amie_bachilleres_consolidado.json")
    try:
        reporte_general["amie"] = ejecutar_mineria_amie(
            ruta_excel=excel_amie,
            canton=config_proyecto["canton"],
            provincia=config_proyecto["provincia"],
            ruta_salida_json=out_amie
        )
    except Exception as e:
        print(f"[ERROR] En minería AMIE: {e}")

    # 5. MINERÍA REEM / SRI
    print("\n--- PASO 5: MINERÍA DE EMPRESAS FORMALES (REEM) ---")
    csv_reem = os.path.join(ruta_raiz_bd, "Registro Estadístico de Empresas (REEM)", "DATOS_ABIERTOS_REEM_2025", "BDD_DATOS_ABIERTOS_EMPRESAS", "EMPRESAS_periodo_2025.csv")
    out_reem = os.path.join(carpeta_salida, "reem_empresas_consolidado.json")
    try:
        reporte_general["reem"] = ejecutar_mineria_reem(
            ruta_reem=csv_reem,
            canton=config_proyecto["canton_dpa"],
            ciiu_letra=config_proyecto["ciiu_seccion"],
            ciiu_div=config_proyecto["ciiu_division"],
            ruta_salida_json=out_reem
        )
    except Exception as e:
        print(f"[ERROR] En minería REEM: {e}")

    # 6. MODELADO ECONOMÉTRICO Y ENCUESTAS
    print("\n--- PASO 6: MODELADO ECONOMÉTRICO DE DEMANDA (ENCUESTAS) ---")
    universo_emp = reporte_general.get("reem", {}).get("metadatos", {}).get("universo_empresas_formal_n", 16673)
    universo_bach = reporte_general.get("amie", {}).get("metadatos", {}).get("universo_bachilleres_base", 41728)
    out_demanda = os.path.join(carpeta_salida, "mercado_demanda_consolidado.json")
    try:
        reporte_general["mercado_demanda"] = ejecutar_mineria_encuestas(
            universo_emp=universo_emp,
            universo_bach=universo_bach,
            out_json=out_demanda
        )
    except Exception as e:
        print(f"[ERROR] En modelado de encuestas: {e}")

    duracion = round(time.time() - inicio, 2)
    print("\n================================================================================")
    print(f"PIPELINE DE MINERÍA FINALIZADO CON ÉXITO EN {duracion} SEGUNDOS")
    print(f"Archivos JSON generados en: '{carpeta_salida}'")
    print("================================================================================")

    # Guardar índice maestro
    with open(os.path.join(carpeta_salida, "indice_datos_mineria.json"), 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "duracion_segundos": duracion,
            "carrera": config_proyecto["carrera"],
            "territorio": f"{config_proyecto['canton']}, {config_proyecto['provincia']}",
            "archivos_generados": [
                "supercias_consolidado.json",
                "enemdu_consolidado.json",
                "senescyt_titulados_consolidado.json",
                "amie_bachilleres_consolidado.json",
                "reem_empresas_consolidado.json",
                "mercado_demanda_consolidado.json"
            ]
        }, f, indent=2, ensure_ascii=False)

    return reporte_general


if __name__ == "__main__":
    ejecutar_pipeline_completo()

