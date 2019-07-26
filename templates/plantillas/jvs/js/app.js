function sumar(){
    let total =0;
    $(".monto").each(function(){
        if(isNaN(parseFloat($(this).val()))){
            total +=0;
        }else{
            total +=parseFloat($(this).val());
        }
    });
    document.getElementById('spTotal').innerHTML = total;
}







