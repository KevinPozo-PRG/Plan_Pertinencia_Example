# -*- coding: utf-8 -*-
"""
SCRIPT DE MINERÍA DE DATOS: SUPERINTENDENCIA DE COMPAÑÍAS (SUPERCIAS)
Dirección de Planificación y Pertinencia Curricular (CES / CACES)

Este script realiza la extracción, filtrado y cruce de datos entre:
1. Directorio de Compañías Activas (directorio_companias.xlsx o CSV)
2. Base de Balances y Ranking Financiero (bi_ranking.csv)

Genera:
- Conteo de empresas societarias activas (S.A., Cía. Ltda., S.A.S.).
- Serie histórica de constitución de empresas en el sector productivo.
- Ranking de las empresas líderes y centros de empleo por volumen de ventas,
  activos y número de trabajadores.
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
import pandas as pd
from collections import defaultdict

# Configuración de salida en consola para caracteres especiales
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def extraer_directorio_supercias(ruta_directorio_xlsx, ciiu_filtro="5630", canton_filtro="QUITO", prov_filtro="PICHINCHA"):
    """
    Lee de forma optimizada el directorio de compañías (utilizando streaming XML si es XLSX pesado)
    filtrando únicamente las sociedades activas del cantón y rama CIIU de interés.
    """
    print(f"[SUPERCIAS] Analizando directorio de empresas...", flush=True)
    print(f"            Filtros: Rama CIIU = '{ciiu_filtro}' | Cantón = '{canton_filtro}' | Provincia = '{prov_filtro}'", flush=True)

    # Verificar si existe una caché previa en JSON o CSV en scratch/ o en datos_extraidos/
    posibles_caches = [
        f"scratch/supercias_{canton_filtro.lower()}_{ciiu_filtro}.json",
        "scratch/supercias_barismo_quito.json",
        f"guia_bot_pertinencia/datos_extraidos/supercias_{canton_filtro.lower()}_{ciiu_filtro}.json"
    ]
    for ruta_cache in posibles_caches:
        if os.path.exists(ruta_cache):
            print(f"[SUPERCIAS] Cargando empresas filtradas desde caché rápida: {ruta_cache}", flush=True)
            with open(ruta_cache, 'r', encoding='utf-8') as f:
                data_c = json.load(f)
                return data_c.get('empresas_quito', data_c if isinstance(data_c, list) else [])

    empresas_filtradas = []
    
    # Si el archivo es XLSX y pesa más de 20 MB, usamos streaming XML para evitar desbordamiento de memoria
    if ruta_directorio_xlsx.endswith('.xlsx') and os.path.exists(ruta_directorio_xlsx):
        try:
            with zipfile.ZipFile(ruta_directorio_xlsx, 'r') as z:
                shared_strings = []
                if 'xl/sharedStrings.xml' in z.namelist():
                    with z.open('xl/sharedStrings.xml') as f:
                        tree = ET.parse(f)
                        root = tree.getroot()
                        ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                        for si in root.findall('ns:si', ns):
                            t = si.find('ns:t', ns)
                            if t is not None and t.text:
                                shared_strings.append(t.text)
                            else:
                                r_texts = [r.find('ns:t', ns).text for r in si.findall('ns:r', ns) if r.find('ns:t', ns) is not None and r.find('ns:t', ns).text]
                                shared_strings.append("".join(r_texts))

                with z.open('xl/worksheets/sheet1.xml') as f:
                    context = ET.iterparse(f, events=('end',))
                    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
                    row_count = 0
                    
                    for event, elem in context:
                        if elem.tag == f'{ns}row':
                            row_dict = {}
                            for c in elem.findall(f'{ns}c'):
                                r_ref = c.get('r')
                                col_letters = "".join([ch for ch in r_ref if ch.isalpha()])
                                v = c.find(f'{ns}v')
                                val = v.text if v is not None else None
                                t = c.get('t')
                                if t == 's' and val is not None and int(val) < len(shared_strings):
                                    val = shared_strings[int(val)]
                                row_dict[col_letters] = val
                            
                            row_count += 1
                            if row_count > 3: # Salta encabezados
                                # Columnas canónicas SUPERCIAS:
                                # A: EXPEDIENTE, D: NOMBRE, E: SITUACION, F/G: FECHA_CONST, J: PROVINCIA, K: CANTON, U/V: CIIU
                                exp = str(row_dict.get('A', '') or '').strip()
                                nombre = str(row_dict.get('D', '') or '').strip()
                                situacion = str(row_dict.get('E', '') or '').strip().upper()
                                fecha_const = str(row_dict.get('F', '') or row_dict.get('G', '') or '').strip()
                                prov = str(row_dict.get('J', '') or '').strip().upper()
                                canton = str(row_dict.get('K', '') or '').strip().upper()
                                ciiu = str(row_dict.get('V', '') or row_dict.get('U', '') or '').strip()
                                tipo = str(row_dict.get('B', '') or row_dict.get('C', '') or 'S.A. / CÍA. LTDA.').strip()
                                
                                anio_const = ""
                                if len(fecha_const) >= 4 and fecha_const[:4].isdigit():
                                    anio_const = fecha_const[:4]
                                elif len(fecha_const) >= 10 and fecha_const[-4:].isdigit():
                                    anio_const = fecha_const[-4:]

                                if situacion == 'ACTIVA' and prov_filtro in prov and canton_filtro in canton:
                                    if ciiu_filtro.lower() in ciiu.lower():
                                        empresas_filtradas.append({
                                            "expediente": exp,
                                            "nombre": nombre,
                                            "tipo": tipo,
                                            "situacion": situacion,
                                            "provincia": prov,
                                            "canton": canton,
                                            "ciiu": ciiu,
                                            "anio_const": anio_const
                                        })
                            elem.clear()
        except Exception as e:
            print(f"[SUPERCIAS] Advertencia en lectura streaming: {e}. Intentando lectura por pandas...")
    
    # Si no se ejecutó streaming o falló, intentar con CSV o pandas normal
    if not empresas_filtradas and os.path.exists(ruta_directorio_xlsx.replace('.xlsx', '.csv')):
        df = pd.read_csv(ruta_directorio_xlsx.replace('.xlsx', '.csv'), sep=';', encoding='latin1', low_memory=False)
        sub = df[(df['SITUACION'].str.upper() == 'ACTIVA') & 
                 (df['CANTON'].str.upper().str.contains(canton_filtro)) &
                 (df['CIIU4'].astype(str).str.contains(ciiu_filtro))]
        for _, r in sub.iterrows():
            empresas_filtradas.append({
                "expediente": str(r.get('EXPEDIENTE', '')),
                "nombre": str(r.get('NOMBRE', '')),
                "tipo": str(r.get('TIPO_COMPANIA', '')),
                "situacion": 'ACTIVA',
                "provincia": str(r.get('PROVINCIA', '')),
                "canton": str(r.get('CANTON', '')),
                "ciiu": str(r.get('CIIU4', '')),
                "anio_const": str(r.get('ANIO_CONSTITUCION', ''))
            })

    print(f"[SUPERCIAS] Total empresas activas identificadas en {canton_filtro}: {len(empresas_filtradas)}")
    return empresas_filtradas


def cruzar_ranking_financiero(empresas_filtradas, ruta_bi_ranking_csv, top_n=15):
    """
    Escanea en bloques (chunks) de 100.000 filas el archivo bi_ranking.csv de la SUPERCIAS,
    cruzando por número de expediente para extraer ventas, activos y personal ocupado.
    """
    # Verificar si existe caché del top ranking
    for ruta_cache_rank in ["scratch/top_ranking_barismo_quito.json", "guia_bot_pertinencia/datos_extraidos/top_ranking_cache.json"]:
        if os.path.exists(ruta_cache_rank):
            print(f"[SUPERCIAS] Cargando ranking financiero desde caché rápida: {ruta_cache_rank}", flush=True)
            with open(ruta_cache_rank, 'r', encoding='utf-8') as f:
                data_rk = json.load(f)
                res_list = data_rk if isinstance(data_rk, list) else data_rk.get('top_ranking', [])
                return res_list[:top_n]

    if not os.path.exists(ruta_bi_ranking_csv):
        print(f"[SUPERCIAS] Aviso: No se encontró {ruta_bi_ranking_csv}. Se usará la lista de directorios.", flush=True)
        return empresas_filtradas[:top_n]
        
    expedientes = set(str(e['expediente']) for e in empresas_filtradas if e['expediente'])
    print(f"[SUPERCIAS] Cruzando {len(expedientes)} expedientes con {ruta_bi_ranking_csv} en bloques...", flush=True)
    
    coincidencias = []
    chunk_num = 0
    
    for chunk in pd.read_csv(ruta_bi_ranking_csv, chunksize=100000, low_memory=False):
        chunk_num += 1
        chunk['expediente_str'] = chunk['expediente'].astype(str)
        subset = chunk[chunk['expediente_str'].isin(expedientes)]
        if not subset.empty:
            coincidencias.append(subset)
        if chunk_num % 5 == 0:
            print(f"            Procesados {chunk_num * 100000:,} registros...")
            
    if coincidencias:
        df_fin = pd.concat(coincidencias, ignore_index=True)
        df_fin['ingresos_ventas'] = pd.to_numeric(df_fin['ingresos_ventas'], errors='coerce').fillna(0)
        df_fin['activos'] = pd.to_numeric(df_fin['activos'], errors='coerce').fillna(0)
        df_fin['n_empleados'] = pd.to_numeric(df_fin['n_empleados'], errors='coerce').fillna(0)
        df_fin['anio'] = pd.to_numeric(df_fin['anio'], errors='coerce').fillna(0)
        
        # Obtener el registro más reciente para cada expediente
        idx_reciente = df_fin.groupby('expediente_str')['anio'].idxmax()
        df_reciente = df_fin.loc[idx_reciente].sort_values(by='ingresos_ventas', ascending=False)
        
        # Mapear nombres y metadatos
        meta_dict = {str(e['expediente']): e for e in empresas_filtradas}
        
        ranking_final = []
        for _, row in df_reciente.head(top_n).iterrows():
            exp_str = str(row['expediente_str'])
            info = meta_dict.get(exp_str, {})
            ranking_final.append({
                "expediente": exp_str,
                "nombre": info.get('nombre', 'COMPAÑÍA ANÓNIMA'),
                "tipo": info.get('tipo', 'SOCIEDAD FORMAL'),
                "anio_constitucion": info.get('anio_const', 'N/D'),
                "anio_balance": int(row['anio']),
                "ingresos_ventas_usd": float(row['ingresos_ventas']),
                "activos_usd": float(row['activos']),
                "personal_ocupado": int(row['n_empleados'])
            })
            
        print(f"[SUPERCIAS] Cruce exitoso. Top {len(ranking_final)} empleadores generado.")
        return ranking_final
    else:
        print("[SUPERCIAS] No se encontraron balances en bi_ranking para estos expedientes.")
        return empresas_filtradas[:top_n]


def ejecutar_mineria_supercias(ruta_directorio, ruta_bi_ranking, ciiu, canton, provincia, ruta_salida_json):
    """
    Función orquestadora que extrae, procesa y guarda en JSON el reporte SUPERCIAS.
    """
    empresas = extraer_directorio_supercias(ruta_directorio, ciiu_filtro=ciiu, canton_filtro=canton, prov_filtro=provincia)
    ranking = cruzar_ranking_financiero(empresas, ruta_bi_ranking, top_n=15)
    
    # Histórico de constitución por décadas / quinquenios
    constitucion_conteo = defaultdict(int)
    for e in empresas:
        ac = str(e.get('anio_const', '')).strip()
        if ac.isdigit() and 1950 <= int(ac) <= 2026:
            constitucion_conteo[int(ac)] += 1
            
    resultado = {
        "metadatos": {
            "fuente": "Superintendencia de Compañías, Valores y Seguros (SUPERCIAS 2026)",
            "canton": canton,
            "provincia": provincia,
            "ciiu_filtro": ciiu,
            "total_companias_activas": len(empresas)
        },
        "serie_constitucion": dict(sorted(constitucion_conteo.items())),
        "top_empleadores_ranking": ranking
    }
    
    os.makedirs(os.path.dirname(ruta_salida_json), exist_ok=True)
    with open(ruta_salida_json, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
        
    print(f"[SUPERCIAS] Reporte consolidado exportado a: {ruta_salida_json}")
    return resultado


if __name__ == "__main__":
    # Rutas por defecto en el entorno de CEDEPRO / IAVQ
    DIR_XLSX = r"BD\Directorio_Companias_Supercias\directorio_companias.xlsx"
    RANK_CSV = r"BD\Ranking_Companias_Supercias\bi_ranking.csv"
    OUT_JSON = r"guia_bot_pertinencia\datos_extraidos\supercias_consolidado.json"
    
    # Parámetros ejemplo: Barismo en Quito (CIIU 5630)
    ejecutar_mineria_supercias(DIR_XLSX, RANK_CSV, ciiu="5630", canton="QUITO", provincia="PICHINCHA", ruta_salida_json=OUT_JSON)
