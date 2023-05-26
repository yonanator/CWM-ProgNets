#!/usr/bin/env python3

import re

from scapy.all import *

class P4calc(Packet):
    name = "P4calc"
    fields_desc = [ StrFixedLenField("P", "P", length=1),
                    StrFixedLenField("Four", "4", length=1),
                    XByteField("version", 0x01),
                    IntField("operand_0", 0),
                    IntField("operand_1", 0),
                    IntField("operand_2", 0),
                    IntField("operand_3", 0),
                    IntField("operand_4", 0),
                    IntField("operand_5", 0),
                    IntField("operand_6", 0),
                    IntField("operand_7", 0),
                    IntField("operand_8", 0),
                    IntField("result", 0xDEADBABE)]

bind_layers(Ether, P4calc, type=0x1234)

'''class NumParseError(Exception):
    pass'''

'''class OpParseError(Exception):
    pass '''

''' class Token:
    def __init__(self,type,value = None):
        self.type = type
        self.value = value '''

'''def num_parser(s, i, ts):
    pattern = "^\s*([0-9]+)\s*"
    match = re.match(pattern,s[i:])
    if match:
        ts.append(Token('num', match.group(1)))
        return i + match.end(), ts
    raise NumParseError('Expected number literal.') '''


''' def op_parser(s, i, ts):
    pattern = "^\s*([-+&|^])\s*"
    match = re.match(pattern,s[i:])
    if match:
        ts.append(Token('num', match.group(1)))
        return i + match.end(), ts
    raise NumParseError("Expected binary operator '-', '+', '&', '|', or '^'.")'''


''' def make_seq(p1, p2):
    def parse(s, i, ts):
        i,ts2 = p1(s,i,ts)
        return p2(s,i,ts2)
    return parse '''

def get_if():
    ifs=get_if_list()
    iface= "enx0c37965f8a27" # "h1-eth0"
    #for i in get_if_list():
    #    if "eth0" in i:
    #        iface=i
    #        break;
    #if not iface:
    #    print("Cannot find eth0 interface")
    #    exit(1)
    #print(iface)
    return iface

def main():

    '''p = make_seq(num_parser, make_seq(op_parser,num_parser))'''
    s = ''
    #iface = get_if()
    iface = "enx0c37965f8a27"
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr1 = ['','','','','','','','','']
    '''arr3 = [[1,2,3,4,5]/['o', 'x', 'o', 'x', 'o']]'''
    while True:
        print("choose your box between 0 and 8")
        s = int(input('> '))
        if s == "quit":
            break
          
        elif (s > 8 or s < 0):
            print("Invalid")
            continue
            
        elif arr[s] == 1 or arr[s] == 2:
            print(" that box has already been chosen")
            continue
       
            
        
       
        arr[s] = 1
        
        
        
        
                              
        try:
            pkt = Ether(dst='00:04:00:00:00:00', type=0x1234) / P4calc(operand_0=arr[0],
                                              operand_1=arr[1],
                                              operand_2= arr[2],
                                              operand_3 = arr[3],
                                              operand_4 = arr[4],
                                              operand_5 = arr[5],
                                              operand_6 = arr[6],
                                              operand_7 = arr[7],
                                              operand_8 = arr[8])

            pkt = pkt/' '

            #pkt.show()
            resp = srp1(pkt, iface=iface,timeout=5, verbose=False)
            if resp:
                p4calc=resp[P4calc]
                if p4calc:
                    
                    
                    if (p4calc.result < 9):
                      print("switch has gone for box ", p4calc.result)
                      arr[p4calc.result] = 2
                    
                    if arr[0] == 0:
                      arr1[0] = ' '
                    elif arr[0] == 1:
                      arr1[0] = 'X'
                    elif arr[0] == 2:
                      arr1[0] = 'O'
                    
                    
                      
                    if arr[1] == 0:
                      arr1[1] = ' '
                    elif arr[1] == 1:
                      arr1[1] = 'X'
                    elif arr[1] == 2:
                      arr1[1] = 'O'
                      
                    if arr[2] == 0:
                      arr1[2] = ' '
                    elif arr[2] == 1:
                      arr1[2] = 'X'
                    elif arr[2] == 2:
                      arr1[2] = 'O'
                      
                    if arr[3] == 0:
                      arr1[3] = ' '
                    elif arr[3] == 1:
                      arr1[3] = 'X'
                    elif arr[3] == 2:
                      arr1[3] = 'O'
                      
                    if arr[4] == 0:
                      arr1[4] = ' '
                    elif arr[4] == 1:
                      arr1[4] = 'X'
                    elif arr[4] == 2:
                      arr1[4] = 'O'
                      
                    if arr[5] == 0:
                      arr1[5] = ' '
                    elif arr[5] == 1:
                      arr1[5] = 'X'
                    elif arr[5] == 2:
                      arr1[5] = 'O'
                      
                    if arr[6] == 0:
                      arr1[6] = ' '
                    elif arr[6] == 1:
                      arr1[6] = 'X'
                    elif arr[6] == 2:
                      arr1[6] = 'O'
                      
                    if arr[7] == 0:
                      arr1[7] = ' '
                    elif arr[7] == 1:
                      arr1[7] = 'X'
                    elif arr[7] == 2:
                      arr1[7] = 'O'
                      
                    if arr[8] == 0:
                      arr1[8] = ""
                    elif arr[8] == 1:
                      arr1[8] = "X"
                    elif arr[8] == 2:
                      arr1[8] = "O"
                      
                    
                   
                    print(arr1[0], "|", arr1[1], "|", arr1[2])
                    print("__________")
                    print(arr1[3],"|", arr1[4],"|", arr1[5])
                    print("__________")
                    print(arr1[6],"|", arr1[7],"|", arr1[8])
                    
                   
                    if (arr[0] == 1) and (arr[1] == 1) and (arr[2] == 1):   #gjhgkjer
                      print("well done you won")
                      break
                    elif arr[3] == 1 and arr[4] == 1 and arr[5] == 1:
                      print("well done you won")
                      break
                    elif arr[6] == 1 and arr[7] == 1 and arr[8] == 1:
                      print("well done you won")
                      break
                    elif arr[0] == 1 and arr[3] == 1 and arr[6] == 1:
                      print("well done you won")
                      break
                    elif arr[1] == 1 and arr[4] == 1 and arr[7] == 1:
                      print("well done you won")
                      break
                    elif arr[2] == 1 and arr[5] == 1 and arr[8] == 1:
                      print("well done you won")
                      break
                    elif arr[0] == 1 and arr[4] == 1 and arr[8] == 1:
                      print("well done you won")
                      break
                    elif arr[2] == 1 and arr[4] == 1 and arr[6] == 1:
                      print("well done you won")
                      break 
                    elif arr[0] == 2 and arr[1] == 2 and arr[2] == 2:
                      print("the switch won")
                      break
                    elif arr[3] == 2 and arr[4] == 2 and arr[5] == 2:
                      print("the switch won")
                      break
                    elif arr[6] == 2 and arr[7] == 2 and arr[8] == 2:
                      print("the switch won")
                      break
                    elif arr[0] == 2 and arr[3] == 2 and arr[6] == 2:
                      print("the switch won")
                      break
                    elif arr[1] == 2 and arr[4] == 2 and arr[7] == 2:
                      print("the switch won")
                      break
                    elif arr[2] == 2 and arr[5] == 2 and arr[8] == 2:
                      print("the switch won")
                      break
                    elif arr[0] == 2 and arr[4] == 2 and arr[8] == 2:
                      print("the switch won")
                      break
                    elif arr[2] == 2 and arr[4] == 2 and arr[6] == 2:
                      print("the switch won")
                      break
                    else:
                      check = 0
                      for i in range(9):
                        if arr[i] == 0: 
                          check = check + 1
                      if check == 0:
                        print("all boxes have been used, end of game")
                        break
                      
                    
                  
                      
                   
                   
                    
                    
                else:
                    print("cannot find P4calc header in the packet")
            else:
                print("Didn't receive response")
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()


