// Obtener el protocol
const protocol = window.location.protocol;
// Obtener el host name
const hostName = window.location.hostname;
// Obtener el número de puerto
const port = window.location.port;
// Obtener el dominio completo (host + puerto si existe)
const domain = window.location.host;
// Obtener la URL completa
const fullUrl = window.location.href;
// Obtener la ruta después del hostname y puerto (grupo-campbell/login)
const path = window.location.pathname.substring(1); // Remover el primer "/"
// Obtener el protocolo, hostname y puerto (http://192.168.122.51:8045)
const baseUrl = `${protocol}//${hostName}${port ? `:${port}` : ''}/${path}`;
// Crear una instancia de URLSearchParams utilizando la parte de búsqueda de la URL
const params = new URLSearchParams(window.location.search);

function encodeBase64(encode)
{
    const enc = btoa(encode);
    return enc;
}

function decodeBase64(decode)
{
    const dec = atob(decode);
    return dec;
}
// console.log(`Protocol: ${protocol}`);
// console.log(`Host Name: ${hostName}`);
// console.log(`Port: ${port}`);
// console.log(`Domain: ${domain}`);
// console.log(`Path: ${path}`);
// console.log(`Base URL: ${baseUrl}`);
// console.log(`Params: ${params}`);

const analyzeNote = async (params) => {
    const note = params;
    const data = {medical_note: note};
    //
    const response = await fetch('',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    const result = await response.json();
    console.log(result);
    // return result;
}