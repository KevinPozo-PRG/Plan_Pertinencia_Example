# -*- coding: utf-8 -*-
"""
SCRIPT DE AUDITORÍA AUTOMÁTICA DEL DOSSIER (CES / CACES)

Verifica los siguientes estándares de calidad:
1. Conteo exacto de páginas (24 páginas oficiales).
2. Existencia de IDs canónicos por página.
3. Tablas con formato reglamentario 'word-table'.
4. Inicialización de gráficos de soporte en Chart.js.
5. Cero enlaces externos en cuerpo y tablas (enlaces restringidos a Referencias).
6. Trazabilidad de hipervínculos oficiales en el Capítulo 8.
"""

import os
import re
from bs4 import BeautifulSoup

def auditar_documento(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] Archivo no encontrado: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    print(f"=== AUDITORÍA TÉCNICA DEL DOSSIER: {os.path.basename(file_path)} ===")

    # 1. Total de páginas
    pages = soup.find_all("div", class_="word-page")
    total_pages = len(pages)
    print(f"1. Total de Páginas Encontradas: {total_pages} (Esperado: 24)")

    # 2. Verificación de IDs canónicos
    expected_ids = [
        "page-01-cover", "page-02-indice", "page-03-intro", "page-04-social-1", "page-05-social-2",
        "page-06-econ-1", "page-07-econ-2", "page-08-supercias", "page-09-enemdu-edu", "page-10-enemdu-iess",
        "page-11-enemdu-salario", "page-12-acad-1", "page-13-acad-2", "page-14-cultural", "page-15-pnd",
        "page-16-territorial", "page-17-solucion", "page-18-demanda-emp-1", "page-19-demanda-emp-2",
        "page-20-brecha", "page-21-estudiantil-1", "page-22-malla", "page-23-conclusiones", "page-24-referencias"
    ]
    missing_ids = [pid for pid in expected_ids if not soup.find(id=pid)]
    print(f"2. Páginas con IDs faltantes: {missing_ids if missing_ids else 'NINGUNO (100% Correcto)'}")

    # 3. Tablas formales
    tables = soup.find_all("table", class_="word-table")
    print(f"3. Tablas Formales con clase 'word-table': {len(tables)}")

    # 4. Gráficos Canvas
    canvases = soup.find_all("canvas")
    print(f"4. Gráficos Canvas Registrados: {len(canvases)}")

    # 5. Enlaces externos en cuerpo vs Capítulo 8
    body_external_links = []
    ch8_external_links = []

    for a in soup.find_all("a"):
        href = a.get("href", "")
        if href.startswith("http://") or href.startswith("https://"):
            parent_page = a.find_parent("div", class_="word-page")
            if parent_page and parent_page.get("id") == "page-24-referencias":
                ch8_external_links.append((a.text.strip(), href))
            else:
                body_external_links.append((a.text.strip(), href, parent_page.get("id") if parent_page else "desconocido"))

    print(f"5. Enlaces externos prohibidos en cuerpo/tablas (Págs 1 a 23): {len(body_external_links)}")
    if body_external_links:
        for txt, hr, pid in body_external_links:
            print(f"   [ALERTA] Página {pid}: '{txt}' -> {hr}")
    else:
        print("   [OK] Limpieza total: 0 enlaces externos en narrativa o tablas.")

    print(f"6. Enlaces oficiales en Capítulo 8 (Referencias): {len(ch8_external_links)}")
    for txt, hr in ch8_external_links:
        print(f"   - {txt[:35]}... -> {hr}")

    es_valido = (total_pages == 24 and len(missing_ids) == 0 and len(body_external_links) == 0)
    print("\n=== RESULTADO DE AUDITORÍA ===")
    print("ESTADO:", "APROBADO (Listo para presentación CACES)" if es_valido else "OBSERVADO")
    return es_valido

if __name__ == "__main__":
    # Ruta al archivo HTML del repositorio
    repo_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "dossier_barismo_iavq_vista_word.html"))
    auditar_documento(repo_file)
