file=open('w2p4.txt','r')
# lines=file1.readlines()
# count=0
# with open(r'a.txt', 'r') as data:
#     text=data.read()

lines=file.readlines()
count1=1
# lc=100
lcList=[]
allSubstrings=[]
emot=[['STOP','ADD','SUB','MULT','MOVER','MOVEM','COMP','BC','DIV','READ','PRINT','START','END','ORIGIN','EQU','LTORG','DS','DC','AREG','BREG','CREG','EQ','LT','GT','NE','ANY'],[1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,2,2,4,4,4,5,5,5,5,5],['00','01','02','03','04','05','06','07','08','09','10','01','02','03','04','05','01','02','01','02','03','01','02','03','04','05']]
symbolTable=[]
sym_lc=[]
symbls=[]
literal_table=[]
literal_add=[]
literals=[]
pool_table=[]
classfield=['IS','DL','AD','RG','CC']

lc=0
pool_no=0
sys=0
lits=0
litlc=[]
litrls=0
for line in lines:
    if 'START' in line:
        line=line.replace(',',' ')
        line=line.replace('\t',' ')
        line=line.strip()
        lc=int(line.split(' ')[1])-1
lit_count=0
for line in lines:
    line=line.replace(',',' ')
    line=line.replace('\t',' ')
    line=line.strip()
    if '=' in line:
        literal=line.split('=')
        literals.append("="+literal[1])
        lit_count+=1
        litlc.append(lc)
    substrings=line.split(' ')
    allSubstrings.append(substrings)
    if 'ORIGIN' in line:
        line=line.replace('+',' ')
        ori=line.split(' ')
        idx=symbls.index(ori[1])
        lc=sym_lc[idx]+int(ori[2])-1
        # print("origin wala lc=",lc)
  
    if 'LTORG' in line:
        for i in range(lit_count):
                literal_add.append(lc)
                lc+=1
        pool_table.append(pool_no)
        pool_no+=lit_count
        lc-=1
        litlc=[]
    lcList.append(lc)
    if substrings[0] not in emot[0]:
        sym_lc.append(lc)
        symbls.append(substrings[0])
    
    tokens=line.split(' ')
    string=""
    for i in tokens:
            if i not in emot[0] and tokens[0]==i:
                pass
            else:
                string+='('
                if i=='LTORG':
                    for i in range(lit_count):
                         string+="DL,02)"
                         if lit_count>1:
                            string+="( C,"+str(literals[litrls])+")"
                         else:
                            string+="( C,"+str(literals[litrls])
                         litrls+=1

                    lit_count=0
                    
                elif i in emot[0]:
                    idx=emot[0].index(i)
                    string+= classfield[emot[1][idx]-1]+" "
                    string+=emot[2][idx]
                elif i in literals:
                    string+=" L,"
                    string+=str(lits)
                    lits+=1
                elif i in symbls and i==tokens[-1] or i.isalpha():
                    string+=" S,"
                    string+=str(sys)
                    sys+=1
                else:
                    string+= " C,"
                    string+=str(lc+1)

                string+=' )'

    print(string)   
    lc+=1
    
symbolTable.append(symbls)
symbolTable.append(sym_lc)
length=[]
for i in range(len(symbolTable[0])):
            length.append(1)
symbolTable.append(length)
literal_table.append(literals)
if lit_count>0:
    for i in range(lit_count):
        literal_add.append(lc-1)
        lc+=1
literal_table.append(literal_add)
for line in lines:
    if 'EQU' in line:
        line=line.strip()
        find_lit=line.split(' ')
        idx=symbolTable[0].index(find_lit[2])
        lc=symbolTable[1][idx]
        idx1=symbolTable[0].index(find_lit[0])
        symbolTable[1][idx1]=lc
print("symbol table=",symbolTable)
print("Literal table=",literal_table)
print("pool table=",pool_table)
for line in lines:
        line=line.replace(',',' ')
        line=line.replace('\t',' ')
        line=line.strip()
        


