from django.shortcuts import render, HttpResponse
from .source.comb2 import Comb2
from copy import deepcopy
import random


#ref is the number of digits in a raffle number
ref = ['0','0']
#ref = ['0','0','0']

#hex is representation of the digits in a raffle number
hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# hex = ['0','1','2','3','4','5','6','7','8','9']

#Create a list of numbers in a raffle
numbers = Comb2().comb(hex,ref)

#price is the value for a number selected in raffle
price = range(2,22,2)

#Start view rendering 
def rifa(request):    
    return render(request, 'rifa.html', {'numbers': numbers[:240], 'price': price})

def gerarNumero(request):
    #select random number.
    num_s = numbers[:240]
    num_r = deepcopy(num_s)
    random.shuffle(num_r)
    num_r = random.choice(num_r)
    
    #verify selected numbers
    if request.method == 'POST':
        selected = request.POST.getlist('buttonnnumber')
        # for i in selected:
        #     if i not in num_s:
        #         return HttpResponse("deu erro")
        if selected == []:
            print("entrou")
            return render(request, 'rifa.html', {'numbers': num_s,'price':price,'selected':selected})
    
    if num_r in selected:
        # pagar pix ao jogador
        
        win = True
    else:
        # receber pix do jogador
        win = False
    return render(request, 'rifa.html', {'numbers': num_s,'price':price,'random':num_r,'selected':selected, 'win':win, 'valor':price[len(selected)-1]})
