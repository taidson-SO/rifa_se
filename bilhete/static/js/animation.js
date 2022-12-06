var img;

function animate(id){
    alert("entrei2"+document.getElementById(id).value);
    
    if(document.getElementById('gif-img') == null){
        img = document.createElement('img');
        img.src = document.getElementById('pic-src').value;
        img.id = 'gif-img';
        
        document.getElementById(id).appendChild(img);
        setTimeout(function(){console.log(10)},5000);
    }
    else{
        img = document.getElementById('gif-img');
    }

    setTimeout(function(){
         document.getElementById(id).parentNode.remove();
    },200);
   
}

function execExplotion(id, r){
    
    if(document.getElementById(id).value != r){
        animate(id);
    }
}