var count = 0;
var aposta = document.getElementById('aposta');
if((count == 0) && (document.getElementById('win')== null)) aposta.innerHTML = " R$"+count+",00";

function chekedbtn(id){
    var btn = document.getElementById(id);

    if(btn.checked){
        
        if(count >= 10){
            alert("Quantidade máxima de números selecionados para este bilhete.")
            btn.checked = !btn.checked;
            return
        }        
        count++; 
        var num = document.createElement('li');
        num.id = 'li'+btn.id;
        num.innerHTML = btn.value;
        document.getElementById('numbers').appendChild(num);
    } 
    else{
        document.getElementById('li'+btn.id).remove();
        count--;
    } 
    if (count > 0){
        document.getElementById('zero').style.display = 'none';
    }
    else{
        document.getElementById('zero').style.display = 'inline-block';
    }
    aposta.innerHTML = " R$"+count+",00"
}
