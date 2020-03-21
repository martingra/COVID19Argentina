COVID-19 En Argentina

# Introducción
Lamentablemente el gobierno argentino no ofrece datos completos en tiempo real sobre la situación de la pandemia en nuestro país.

Por eso, hace unos días me propuse generar un registro en csv con los casos día por día, provincia por provincia. Para esto, utilicé los reportes diarios emitidos por el Ministerio de Salud de la nación y los periódicos más importantes para cubrir las incosistencias o falta de información de los reportes.

Para completar, hice sencillos gráficos consumiendo esta información, y la infromación a nivel global ofrecida en https://github.com/CSSEGISandData

Te invito a que participes, ya sea actualizando o corrigiendo datos, aprotando nuevos análisis de la información o simplemente con sugerencias e ideas.

Gracias!!!

# Descripción

Incluyo los archivos .py y ademas las Notebooks para poder trabajar rapidamente y ver los resultados planteados directamente del navegador. Las notebooks son:

- Argentina (Casos locales por día y por provincia): https://github.com/martingra/COVID19Argentina/blob/master/COVID19Argentina.ipynb
- Argentina vs mundo: https://github.com/martingra/COVID19Argentina/blob/master/COVID19ArgentinaWorld.ipynb
- Argentina vs región: https://github.com/martingra/COVID19Argentina/blob/master/COVID19ArgentinaLatinamerica.ipynb  
- Argentina diario del lunes (comparación con Italia y España): https://github.com/martingra/COVID19Argentina/blob/master/COVID19ArgentinaMondayMorningQuarterback.ipynb

# Dependencias

  Las siguientes dependencias son necesarias para correr los scripts localmente

    NumPy
    Matplotlib
	Pandas

# Datos de Argentina

La carpeta "data" contiene los datos de Argentina cargados manualmente.

- time_series_19-covid-Confirmed.csv: Contiene los datos acumulados día por día, provincia por provincia.
- time_series_19-covid-Confirmed-Day by day.csv: Contiene los datos de cada día (no acumulado) por provincia.

# Nota 
  Los datos por región y por día de Argentina los cargué yo manualmente, leyendo los informes diarios del Ministerio de Salud y los diarios argentinos de cada fecha. Los datos pueden tener errores (muy probablemente) por lo que si podes corregirlos o verificarlos estarás haciendo un valorable aporte.
  
  GRACIAS!
