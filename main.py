from collections import defaultdict
from typing import Dict, Any


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        solicitudes = 0
        metodos_http = defaultdict(int)
        codigos_respuesta = defaultdict(int)
        urls = defaultdict(int)
        tamano_total = 0

        with open(self.nombre_archivo, 'r', encoding="utf-8") as archivo:
            while True:
                ip_line = archivo.readline()
                if not ip_line:
                    break
                fecha_line = archivo.readline()
                metodo_line = archivo.readline()
                url_line = archivo.readline()
                codigo_line = archivo.readline()
                tamano_line = archivo.readline()

                metodo = metodo_line.split(': ')[1].strip()
                codigo = int(codigo_line.split(': ')[1].strip())
                url = url_line.split(': ')[1].strip()
                tamano = int(tamano_line.split(': ')[1].strip())

                solicitudes += 1
                metodos_http[metodo] += 1
                codigos_respuesta[codigo] += 1
                urls[url] += 1
                tamano_total += tamano

        urls_ordenadas = sorted(urls.items(), key=lambda x: x[1], reverse=True)[:10]
        tamano_promedio = tamano_total / solicitudes if solicitudes > 0 else 0

        return {
            'solicitudes': solicitudes,
            'metodos_http': dict(metodos_http),
            'codigos_respuesta': dict(codigos_respuesta),
            'tamano_total': tamano_total,
            'tamano_promedio': tamano_promedio,
            'urls_top_10': urls_ordenadas,
        }


# Uso de la clase AnalizadorLogs
nombre_archivo = 'ejemplo_logs.txt'  # Cambiado a 'ejemplo_logs.txt'
analizador = AnalizadorLogs(nombre_archivo)
informe = analizador.procesar_logs()

# Imprimir el informe
for clave, valor in informe.items():
    print(f"{clave}: {valor}")