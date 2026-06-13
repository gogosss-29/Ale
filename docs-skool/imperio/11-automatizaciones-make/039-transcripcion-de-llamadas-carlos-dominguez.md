# Transcripción de Llamadas | Carlos Dominguez

> Ruta: Automatizaciones Make › Transcripción de Llamadas | Carlos Dominguez

**🎬 Vídeo (10.3 min):** https://www.loom.com/share/04aca068ef8340789156e756b1330e69?sid=fdfe5795-ef30-465f-adc7-b179aa438428

**📎 Recursos:**
- Plantilla 1
- Plantilla 2

---

[**Carlos Dominguez**](https://www.skool.com/@carlos-dominguez-6330?g=imperio-digital)

![CleanShot 2025-04-01 at 17.32.32.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e9a21f6bcbaa4f7dbcc3eb8749f33c08aa8ac44036e146039d39aa55d90fd8cc)

[**Carlos Dominguez**](https://www.skool.com/@carlos-dominguez-6330?g=imperio-digital)

"Hoy les comparto una automa tización que me ha funcionado de maravilla para transcribir llamadas automáticamente 🎧➡️📄 sin consumir miles de operaciones en Make ⚙️. El problema era detectar nuevos archivos en Drive sin depender de un trigger por intervalo ⏱️. La solución: un Apps Script que monitorea carpetas específicas y lanza un webhook apenas detecta un nuevo archivo 🚀. Así evito que Make esté revisando constantemente y ahorro un montón 💰.

![CleanShot 2025-04-01 at 17.32.44.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1d33ee73d3b44fd49f3e8c8bc9ef8bb6a2e1f783a018479a9dce4aee7c224f65)

Una vez que se sube la llamada (.wav), identifico al usuario y la carpeta correspondiente, la paso por Whisper para obtener la transcripción sin modificar nada , y luego uso un asistente tipo Firefly AI para generar un resumen en HTML . Al final, mando el resultado por correo . Esta lógica evolucionó hacia una integración directa con el API del software de llamadas, pero si quieren automatizar sin gastar de más, el combo de webhook + Apps Script 💡 es lo más útil. ¡Espero que les sirva! 🙌Y si pueden, échenme la mano con un like ❤️ para llegar al nivel 6 antes de que se acabe el tiempo ⏳😄

PD: Les dejo los 2 blueprints y el Apps Script

Apps Script en Notion: [https://www.notion.so/upperedgepm/Apps-Script-para-Google-Drive-y-Make-com-1c8a415047ad80859a37f519c3a4065f?pvs=4](https://www.notion.so/upperedgepm/Apps-Script-para-Google-Drive-y-Make-com-1c8a415047ad80859a37f519c3a4065f?pvs=4)  
  


```
const webhookUrl = '<https://hook.us1.make.com/qobesg1fers134u5jpfyfoqil1i1e7u9>'; 
```

➡️ Define la URL del webhook de Make (antes Integromat), que recibirá la información de los archivos nuevos.

> const foldersToMonitor = [
> 
> { id: '1n_KJmdDk-hpAdKDcFpjscVbWW-xDk', name: 'Red' },
> 
> { id: '1_2HymW0yHiqaVNzerPnpr-RxP2sIj', name: 'Green' },
> 
> { id: '1YA1WZgor1OEhgWGNL-vT4LkoJdFnp', name: 'Blue' },
> 
> { id: '1p_HShU1jl8dogXZGTARJmi5LHzAKE7', name: 'Yellow' },
> 
> { id: '1W_YSL9q_U_GJtvDg2yXgApQxRlIwRW', name: 'Test' }
> 
> ];

➡️ Lista de carpetas de Google Drive que se van a monitorear. Cada carpeta tiene un id y un nombre.

> const cache = CacheService.getScriptCache();
> 
> ➡️ Se accede al servicio de caché de Google Apps Script para evitar procesar el mismo archivo varias veces.

> function isRecentlyCreated(file) {
> 
> const now = new Date();
> 
> const threshold = 60 * 1000; // last 60 seconds
> 
> return now - file.getDateCreated() < threshold;
> 
> }

➡️ Función que determina si un archivo es reciente, es decir, si fue creado hace menos de 60 segundos.

> function checkForNewFiles() {
> 
> let newFilesFound = false;

➡️ Función principal. Inicializa una bandera para saber si se encontraron archivos nuevos.  


```
foldersToMonitor.forEach(folderObj => {
```

➡️ Recorre cada carpeta definida en foldersToMonitor.

```
const folder = DriveApp.getFolderById(folderObj.id); const files = folder.getFiles();
```

![➡️](None)

➡️ Obtiene la carpeta desde Drive y luego los archivos dentro de esa carpeta.

> while (files.hasNext()) {
> 
>   const file = [files.next](http://files.next)();
> 
>   const fileId = file.getId();

![➡️](None)

 ➡️Recorre cada archivo dentro de la carpeta y obtiene su id.

>   if (!cache.get(fileId) && isRecentlyCreated(file)) {

➡️ Verifica que el archivo no esté en caché (no ha sido procesado) y que sea reciente (menos de 60 segundos de antigüedad).

>    const payload = {
> 
>       folderName: folderObj.name,
> 
>       folderId: folderObj.id,
> 
>       fileId: fileId,
> 
>       name: file.getName(),
> 
>       url: file.getUrl(),
> 
>       mimeType: file.getMimeType(),
> 
>       createdAt: file.getDateCreated()
> 
>     };

![➡️](None)

 ➡️Se arma un objeto con los datos del archivo, que será enviado al webhook.

> try {
> 
>       const res = UrlFetchApp.fetch(webhookUrl, {
> 
>         method: 'post',
> 
>         contentType: 'application/json',
> 
>         payload: JSON.stringify(payload),
> 
>         muteHttpExceptions: true
> 
>       });

➡️ Se hace la petición POST al webhook con los datos del archivo en formato JSON.  


> Logger.log(`✅ Sent file from ${[folderObj.name](http://folderObj.name)}: ${fileId}`);
> 
>       cache.put(fileId, 'processed', 60 * 60); // cache for 1 hour
> 
>       newFilesFound = true;

➡️ Si el envío fue exitoso, se guarda el ID en caché por una hora y se indica que se encontró al menos un archivo nuevo.

> } catch (err) {
> 
>       Logger.log(`❌ Error for file ${fileId}: ${err}`);
> 
>     }

➡️ Si hay un error al enviar al webhook, se registra en los logs.

> if (!newFilesFound) {
> 
> Logger.log("📭 No new files found in any folder.");
> 
> }
> 
> }

➡️ Si no se encontró ningún archivo nuevo en ninguna carpeta, se registra un mensaje informativo.

> const webhookUrl = '[https://hook.us1.make.com/xxxxxxxxxxxxxxxxxx](https://hook.us1.make.com/xxxxxxxxxxxxxxxxxx)';
> 
> const foldersToMonitor = [
> 
>   { id: '1n_KJmdDk-hpAdKDcFpjscVbWW-xDkH', name: 'Red' },
> 
>   { id: '1_2HymW0yHiqaVNzerPnpr-R2ywXsIj', name: 'Green' },
> 
>   { id: '1YA1WZgor1OEhgWGNL-vT4Lk4tUdFnp', name: 'Blue' },
> 
>   { id: '1p_HShU1jl8dogXZGTARJmqLHzAKE7', name: 'Yellow' },
> 
>   { id: '1W_YSL9q_U_GJtvDg2yXWpQxRlIwRW', name: 'Test' }
> 
> ];
> 
> const cache = CacheService.getScriptCache();
> 
> function isRecentlyCreated(file) {
> 
>   const now = new Date();
> 
>   const threshold = 60 * 1000; // last 60 seconds
> 
>   return now - file.getDateCreated() < threshold;
> 
> }
> 
> function checkForNewFiles() {
> 
>   let newFilesFound = false;
> 
>   foldersToMonitor.forEach(folderObj => {
> 
>     const folder = DriveApp.getFolderById([folderObj.id](http://folderObj.id));
> 
>     const files = folder.getFiles();
> 
>     while (files.hasNext()) {
> 
>       const file = [files.next](http://files.next)();
> 
>       const fileId = file.getId();
> 
>       if (!cache.get(fileId) && isRecentlyCreated(file)) {
> 
>         const payload = {
> 
>           folderName: [folderObj.name](http://folderObj.name),
> 
>           folderId: [folderObj.id](http://folderObj.id),
> 
>           fileId: fileId,
> 
>           name: file.getName(),
> 
>           url: file.getUrl(),
> 
>           mimeType: file.getMimeType(),
> 
>           createdAt: file.getDateCreated()
> 
>         };
> 
>         try {
> 
>           const res = UrlFetchApp.fetch(webhookUrl, {
> 
>             method: 'post',
> 
>             contentType: 'application/json',
> 
>             payload: JSON.stringify(payload),
> 
>             muteHttpExceptions: true
> 
>           });
> 
>           Logger.log(`✅ Sent file from ${[folderObj.name](http://folderObj.name)}: ${fileId}`);
> 
>           cache.put(fileId, 'processed', 60 * 60); // cache for 1 hour
> 
>           newFilesFound = true;
> 
>         } catch (err) {
> 
>           Logger.log(`❌ Error for file ${fileId}: ${err}`);
> 
>         }
> 
>       }
> 
>     }
> 
>   });
> 
>   if (!newFilesFound) {
> 
>     Logger.log("📭 No new files found in any folder.");
> 
>   }
> 
> }
