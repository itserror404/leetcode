class Solution:
    def generate(self, rows: int) -> List[List[int]]:
        output= [[1]*i for i in range(1,rows+1)]
        
        i= 1
        while i<rows:
                 for j in range(1, len(output[i-1])):
                     output[i][j]= output[i-1][j]+output[i-1][j-1]
                i+=1
        return output

                
            
