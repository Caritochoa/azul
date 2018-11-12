
var i = 0;
        var imagenes = [];
        var time = 3000;//intervalo de tiempo entre las imagenes
    
    //creo un array llamado imagenes
    imagenes[0]='yoga-banner.jpg';
    imagenes[1]='chacras.jpg';
    imagenes[2]='product.jpg';
    imagenes[3]='images.jpeg';

    function changeImg(){//funcion para cambiar de imagen
        document.slide.src = imagenes[i];
        if(i < imagenes.length-1){
            i++;
        } else {
            i=0;
        }         
    //metodo para que corra la funcion changeImg con el 
    //intervalo establecido 
    setTimeout(changeImg, time);l 
    }

    window.onload = changeImg;//carga en la ventana
