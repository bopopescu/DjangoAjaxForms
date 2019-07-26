function calculo()

{

    var dias = parseInt(document.getElementById('dias').value);
    var horas = parseFloat(document.getElementById('horas').value);
    var dias_base  = parseInt(document.getElementById('const_dias').value);
    var horas_base  = parseFloat(document.getElementById('const_horas').value);

    dias_base -= dias;
    horas_base -= horas;
    
    document.getElementById('const_dias').value = dias_base;
    document.getElementById('const_horas').value = horas_base;

    

} console.log(calculo);






