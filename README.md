# bot-wallapop-AI

API
- [x] Dado un nuevo link de wallapop, que cree un nuevo archivo csv para cada producto, y si existe que vaya a buscar el archivo
- [x] Cambiar params.txt .env
- [x] Arreglar bug de que si no hay elementos que no pete
- [x] Meter limitador de anuncios, en el .env (aun no implementado en el codigo)
- [x] Meter en el .env el tiempo que tarda en buscar los elementos
- [x] Cuando no existen productos con ese nombre, envia un mensaje avisando al usuario y borra el csv creado anteriormente
- [x] Optimizar donde poner el driver.quit()
- [x] Optimizar los sleeps de las animaciones en open_web
----------
PARTE ENCARGADA DE GESTIONAR AL BOT
- [x] Crear nuevo proyecto independiente a la API para controlar el comportamiento del bot
- [x] Crear una carpeta para cada nuevo usuario, con su chatid como titulo. Comprobar a los nuevos usuarios
- [x] Crear automaticamente un archivo links en la carpeta de cada usuario para que cada usuario puedo almacenar sus links
- [x] Automatizar sistema de creado de ficheros csv para cada usuario, los ficheros se almacenarán en su respectiva carpeta
- [x] Añadir un set de instrucciones
- [x] Establecer una contraseña para nuevos usuarios
- [x] CURRENT Filtrar todos los nombres de las carpetas en usuarios (chatid de cada usuario) y guardarlos como usuarios autorizados para que no introduzcan la contraseña con cada reseteo
- [ ] Establecer trial
- [ ] Poder omitir anuncios de ciertos usuarios o cirtos titulos
----------
MODIFICACIONES API PARA FUNCIONAR JUNTO AL BOT
- [x] Modificar bucle principal para que ejecute buscar_productos() de todos los links de todos los usuarios.
- [x] Editar sistema de generado de csv con tal de que cree los archivos en la carpeta de cada usuario.
- [x] Establecer que la primera vez que se añaden los productos al csv no se notifique al usuario para evitar flood.
----------
IMPLEMENTACION DE IA
