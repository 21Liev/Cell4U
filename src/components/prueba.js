fetch("celulares.json")
    .then(response => response.json())
    .then(data => {console.log(data); // Ver los datos en la consola
});