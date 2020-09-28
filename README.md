# Ranking 

## Proceso
El primer paso que realice fue crear las conexiones de servidor y puerto para poder mandar informacion directamente al localhost. (los files utilizados para ello fueron Server.py, Config.py, src.database.py y app.py).
Después, cree una funcion parseada con la que poder importar a MongoDB, todos los documentos recogidos en la API de GitHub. La función te permite importa los datos una a una, introduciendo el numero de página que toque, y teniendo en cuenta que cada una de ellas contiene un un maximo de 100 documentos.
Posteriormente, creé una carpeta src en la que se encuentran (a parte de files dedicados a la conexion con el localhost), los helpers y los controllers con los que crear los endpoints.

## Controllers
Los controllers creados permiten generar nuevos students y labs dentro de la BBDD mediante los endpoints: ("/student/create/<nombre student>") y ("/student/create/<nombre lab>") respectivamente, y obtener una lista con todos los students y labs contenidos en la BBDD, mediante los enpoints ("/student/all") y ("/labs/all"). 
  
  
  
  
  
## Trabajo en tiemoo "extra" :)
Al no querer quedarme atrás en este tema, estoy "mejorando" mi trabajo, con un fin de aprendizaje más que de sacar buena nota en el proyecto. Durante el día de hoy, y apoyándome en proyectos de compañeros, he creado un par de funciones cuya finalidad es obtener de manera limpia, los nombres de los labs, y y de los estudiantes. Estas funciones se encuentran en el archivo "src.functions.py". Posteriormente, se aplican estas funciones a la función "getpull()", ubicada en el archivo "cleaning.py", para obtener de la API de github, la informacion optima que exportar a despues a MongoDB.

