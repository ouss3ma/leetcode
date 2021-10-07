class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        #choisir numero en commun
        nbr = 0
        for i in range (1,7):
            #trouver les correspandance
            n = 0
            for j in range (len(tops)):
                if tops[j] == i or bottoms[j] ==i:
                    n+=1
            if n == len(tops):
                nbr = i
                break
        
        #get nbre of double
        double = 0
        for i in range(len(tops)):
            if tops[i] == bottoms[i] and tops[i] == nbr:
                double += 1
        
        
        if nbr == 0:
            itr = -1
        else:
            itr_tops = tops.count(nbr)
            itr_bottoms = bottoms.count(nbr)
            itr = min([itr_tops,itr_bottoms]) - double
            
        return itr 
