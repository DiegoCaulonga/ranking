# Ranking 

## Proceso
El primer paso que realice fue crear las conexiones de servidor y puerto para poder mandar informacion directamente al localhost. (los files utilizados para ello fueron Server.py, Config.py, src.database.py y app.py).
Después, cree una funcion parseada con la que poder importar a MongoDB, todos los documentos recogidos en la API de GitHub. La función te permite importa los datos una a una, introduciendo el numero de página que toque, y teniendo en cuenta que cada una de ellas contiene un un maximo de 100 documentos.
Posteriormente, creé una carpeta src en la que se encuentran (a parte de files dedicados a la conexion con el localhost), los helpers y los controllers con los que crear los endpoints.

## Controllers
Los controllers creados permiten generar nuevos students y labs dentro de la BBDD mediante los endpoints: ("/student/create/<nombre student>") y ("/student/create/<nombre lab>") respectivamente, y obtener una lista con todos los students y labs contenidos en la BBDD, mediante los enpoints ("/student/all") y ("/labs/all"). 

