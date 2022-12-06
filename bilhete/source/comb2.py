#hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#ref = ['0','0','0','0']

class Comb2():
    def __init__(self):
        self.numbers = []
    
    def comb(self, lchar=[], lref=[]):
        
        if not lchar or not lref:
            return []
        
        i = 0
        while 1:
            self.numbers.append(''.join(map(str, lref[::-1])))    
            
            if lref[i] != lchar[-1]:
                try:
                
                    lref[i] = lchar[lchar.index(lref[i])+1]
                except ValueError:
                    print("\nErro nos valores da lista, verifique se \ntodos os caracteres de referência estão na \nlista de caracteres.\n")
                    break    
            else:
                while lref[i] == lchar[-1]:
                    lref[i] = lchar[0]
                    i += 1
                
                    if i >= len(lref):
                        break
                if len(lref) > i:    
                    
                    lref[i] = lchar[lchar.index(lref[i])+1]
                    i = 0
                else:
                    break  
                      
        return self.numbers
