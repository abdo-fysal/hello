from graphviz import Digraph
from scanner import*

class parser:
    def __init__(self,tokens):
        self.next_token=tokens
        self.i=0
        self.g = Digraph('G')
        self.left=" "
        self.right=" "
        self.parent=" "
        self.child=" "
        self.ii=0
        self.o=0



    def match(self,token,s):
        if(token==s):


            return s
        else:
            return False



    def program(self):
        if(self.stmt_sequence()!=False):
            f = open('output.txt', 'a')
            f.write('\n' + "stmt-sequence found")
            f.close()
            return True
        else:
            return False

    def stmt_sequence(self):
        left2 = " "
        right2 = " "
        t2=self.statement()


        if(t2!=False):

            left2=t2

            f = open('output.txt', 'a')
            f.write('\n' + "statement found")
            f.close()
            parent2=left2
            while (self.i<len(self.next_token)):
                if self.next_token[self.i][0] == ";":
                    print("pisoo")
                    self.i=self.i+1
                    print(self.next_token[self.i][0])

                    p=self.statement()

                    if(p!=False):

                        right2=p
                        print(right2)
                        parent2=";"
                        self.g.node(left2[0],left2[1])
                        self.g.node(right2[0],right2[1])
                        with self.g.subgraph() as c:
                            c.attr(rank='same')
                            c.edge(left2[0],right2[0])
                        left2=right2
                    else:
                        break

                else:
                    break


                    #return False
            return left2

        else:
            return  False

    def statement(self):
        if(self.i<len(self.next_token)):



            if(self.next_token[self.i][0]=="if"):
                ht=self.IF_stmt()
                if(ht!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "if-statement found")
                    f.close()
                    return ht
                else:
                    return False



            elif(self.next_token[self.i][0]=="repeat"):
                t=self.repeat_stmt()
                if(t!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "repeat-statement found")
                    f.close()
                    return t
                else:
                    return False


            elif(self.next_token[self.i][0]=="identifier"):
                t=self.assign_stmt()

                if(t!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "assign-statement found")
                    f.close()
                    return t
                else:
                    return False






            elif (self.next_token[self.i][0]=="read"):
                print("hiii")
                tt=self.read_stmt()

                if(tt!=False):

                    f = open('output.txt', 'a')
                    f.write('\n' + "read-statement found")
                    f.close()
                    return tt
                else:
                    return False




            elif (self.next_token[self.i][0]== "write"):
                t=self.write_stmt()
                if(t!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "write-statement found")
                    f.close()
                    return t
                else:
                    return False
            else:

                return False
        else:
            return " "


    def IF_stmt(self):
        if(self.match(self.next_token[self.i][0], "if")):



            self.i=self.i+1
            x=self.next_token[self.i][0]
            ex3=self.exp()


            if(ex3!=False):
                f = open('output.txt', 'a')
                f.write('\n' + "expression found")
                f.close()
                self.i=self.i-1
                print(self.next_token[self.i][0])

                if(self.match(self.next_token[self.i][0], "then")):
                    self.i = self.i + 1
                    st3=self.stmt_sequence()

                    if(st3!=False):

                        f = open('output.txt', 'a')
                        f.write('\n' + "stmt-sequence found")
                        f.close()
                        self.g.node('if','if')
                        self.g.node(ex3[0],ex3[1])
                        self.g.node(st3[0],st3[1])
                        self.g.edge('if',ex3[0])
                        self.g.edge('if',st3[0])
                        parent="if"


                        if (self.next_token[self.i] == "else"):

                            self.match(self.next_token[self.i][0], "else")
                            self.i=self.i+1
                            st2=self.stmt_sequence()

                            if(st2!=False):
                                f = open('output.txt', 'a')
                                f.write('\n' + "stmt-sequence found")
                                f.close()
                                #self.i=self.i-1
                                self.g.node('el','else')
                                self.g.node(st2[0],st2[1])
                                self.g.edge('if','e1')
                                self.g.edge('if',st2[0])
                                parent = "if"


                            else:
                                return False
                        if (self.match(self.next_token[self.i][0], "end")):

                            print("[")
                            self.i=self.i+1

                            return ['if','if']
                        else:

                            return False
                    else:
                        return False


                else:
                    return False

            else:
                return False


    def repeat_stmt(self):
        x=0
        if(self.match(self.next_token[self.i][0], "repeat")):
            print("jojo")
            self.i = self.i + 1
            stt=self.stmt_sequence()

            if(stt!=False):
                f = open('output.txt', 'a')
                f.write('\n' + "stmt-sequence found")
                f.close()
                #self.i=self.i+1



                if(self.match(self.next_token[self.i][0], "until")):

                    self.i = self.i + 1
                    exx=self.exp()

                    if(exx!=False):
                        f = open('output.txt', 'a')
                        f.write('\n' + "expession found")
                        f.close()
                        self.i = self.i -1
                        print("kkk")
                        print(self.next_token[self.i][0])
                        self.g.node('re','repeat')
                        self.g.node(stt[0],stt[1])
                        self.g.node(exx[0],exx[1])
                        self.g.node('l','until')
                        self.g.edge('l',exx[0])
                        self.g.edge('re',stt[0])
                        self.g.edge('re','l')

                        self.parent="repeat"
                        x1=self.o
                        self.o+=self.o

                        return ['re','repeat']
                    else :
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def assign_stmt(self):
        n=0
        if(self.match(self.next_token[self.i][0], "identifier")):

            gj = self.next_token[self.i][1]
            self.i = self.i + 1

            if(self.match(self.next_token[self.i][0], ":=")):


                self.i = self.i + 1




                t=self.exp()

                if(t!=False):
                    self.g.node('='+str(self.o),'=')
                    self.g.node('l2'+str(self.o),gj)
                    self.g.node(t[0],t[1])


                    self.g.edge('='+str(self.o),'l2'+str(self.o))
                    self.g.edge('='+str(self.o),t[0])
                    print("nono")
                    print(self.next_token[self.i][1])



                    f = open('output.txt', 'a')
                    f.write('\n' + "expression found")
                    f.close()

                    print(self.next_token[self.i][1])
                    parentt="="
                    n=self.o
                    self.o+=self.o
                    return ['='+str(n),'=']

                else:
                    return False
            else:
                return False
        else:
            return False


    def read_stmt(self):
        if(self.match(self.next_token[self.i][0], "read")):
            parenty = "read"
            self.g.node('r','read')

            self.i = self.i + 1


            if(self.match(self.next_token[self.i][0], "identifier")):
                self.g.node('c1',self.next_token[self.i][1])
                self.g.edge('r','c1')
                parenty = "read"

                self.i = self.i + 1

                return  ['r','read']
            else:
                return False
        else:
            return False

    def write_stmt(self):
        if(self.match(self.next_token[self.i][0], "write")):
            self.parent="write"
            self.g.node('w','write')

            self.i=self.i+1
            t5=self.exp()
            if(t5!=False):
                self.child=t5
                f = open('output.txt', 'a')
                f.write('\n' + "expression found")
                f.close()
                self.g.node(self.child[0], self.child[1])

                #self.i = self.i + 1
                self.g.edge('w',self.child[0])
                self.parent="write"

                return ['w','write']
            else:
                return False
        else:
            return False

    def exp(self):
        xx=0
        t55=self.simple_exp()
        print(t55)

        if(t55!=False):
            left4=t55


            f = open('output.txt', 'a')
            f.write('\n' + "simple-exp found")
            f.close()
            parent4=left4

            while(self.next_token[self.i][0]=="<" or self.next_token[self.i][0]=="="):
                h1=self.comparison_op()

                if(h1!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "comparison-operation found")
                    f.close()
                    parent4=h1

                    l1=self.simple_exp()

                    if(l1!=False):
                        right4=l1
                        f = open('output.txt', 'a')
                        f.write('\n' + "simple-exp found")
                        f.close()

                        self.g.node(parent4[0]+str(self.o),parent4[1])
                        self.g.node(left4[0]+str(self.o)+str(6),left4[1])

                        
                        #print(self.left)
                        #print(self.right)
                        #print(self.parent)

                        self.g.edge(parent4[0]+str(self.o),left4[0]+str(self.o)+str(6))
                        self.g.node(right4[0] + str(self.o), right4[1])
                        self.g.edge(parent4[0]+str(self.o),right4[0]+str(self.o))



                        print("pipo")
                        print(left4)
                        print(right4)
                        print(parent4)
                        xx=self.o


                        left4=parent4
                        left4[0]=left4[0]+str(xx)
                        self.o+=15

                        self.i = self.i + 1

                    else:
                        return False
                else:
                    return False

            #print(self.parent)

            return parent4
        else:
            return False

    def comparison_op(self):
        v=0
        if(self.match(self.next_token[self.i][0],"<")):
            y=self.next_token[self.i][0]

            self.i = self.i + 1
            v=self.o
            self.o+=self.o

            return [y+str(v),y]
        elif(self.match(self.next_token[self.i][0],"=")):
            y=self.next_token[self.i][0]

            self.i = self.i + 1
            v = self.o
            self.o += self.o
            print("hi")

            return [y+str(v),y]
        else:
            return False



    def simple_exp(self):
        t6=self.term()

        if(t6!=False):
            #self.left=t

            f = open('output.txt', 'a')
            f.write('\n' + "term found")
            f.close()
            h6=t6
            while(self.next_token[self.i][0]=="+" or self.next_token[self.i][0]=="-" ):
                h6=self.addop()
                if(h6!=False):
                    #self.parent=h
                    f = open('output.txt', 'a')
                    f.write('\n' + "addop found")
                    f.close()
                    k6=self.term()

                    if(k6!=False):
                        #self.right=k
                        self.g.node(h6[0],h6[1])
                        self.g.node(t6[0]+str(7),t6[1])
                        self.g.node(k6[0]+str(6),k6[1])
                        self.g.edge(h6[0],t6[0]+str(7))
                        self.g.edge(h6[0], k6[0]+str(6))
                        #self.left=sh6[elf.parent
                        t6=h6

                        #self.i = self.i + 1
                        continue

                    else:
                        return False
                else:
                    return False
            return h6


        else:
            return False

    def addop(self):
        e=0
        if(self.match(self.next_token[self.i][0],"+")):
            y=self.next_token[self.i][0]
            self.i = self.i + 1
            e=self.o
            self.o+=1

            return ['+'+str(e),y]
        elif(self.match(self.next_token[self.i][0],"-")):
            y=self.next_token[self.i][0]
            self.i = self.i + 1
            e = self.o
            self.o += 1
            return  ['-'+str(e),y]
        else:
            return False

    def term(self):
        m=0
        left0=self.factor()

        self.g.node('a',left0)
        if(left0!=False):
            f = open('output.txt', 'a')
            f.write('\n' + "factor found")
            f.close()
            t7=left0
            while(self.next_token[self.i][0]=="*" or self.next_token[self.i][0]=="/" ):
                t7=self.mulop()
                if(t7!=False):
                    f = open('output.txt', 'a')
                    f.write('\n' + "mulop found")
                    f.close()
                    parent0=t7
                    print(t7)
                    right0 = self.factor()
                    print("this is")
                    print('a'+str(self.o))
                    print(t7)
                    self.g.node('a'+str(self.o),t7)
                    self.g.node('b'+str(self.o),left0)
                    self.g.node('c'+str(self.o),right0)
                    self.g.edge('a'+str(self.o),'b'+str(self.o))
                    self.g.edge('a'+str(self.o),'c'+str(self.o))
                    left0=t7
                    m=self.o
                    self.o += self.o



                    if(right0!=False):
                        self.i = self.i


                    else:
                        return False
                else:
                    return False
            print(t7)

            return ['a'+str(m),t7]


        else:
            return False

    def mulop(self):
        z=0
        if(self.match(self.next_token[self.i][0],"*")):
            y=self.next_token[self.i][0]

            self.i=self.i+1
            z=self.o
            self.o+=1

            return y
        elif(self.match(self.next_token[self.i][0],"/")):
            y=self.next_token[self.i][0]

            self.i=self.i+1

            z = self.o
            self.o += 1

            return y
        else:
            return False

    def factor(self):

        if (self.next_token[self.i][0]=="("):

            if(self.match(self.next_token[self.i][0],"(")):

                self.i = self.i + 1

                if(self.exp()):

                    f = open('output.txt', 'a')
                    f.write('\n' + "expression found")
                    f.close()

                    if(self.match(self.next_token[self.i][0],")")):

                        self.i = self.i + 1

                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        elif(self.next_token[self.i][0]=="number"):

            if(self.match(self.next_token[self.i][0],"number")):
                y=self.next_token[self.i][1]

                self.i = self.i + 1

                return str(y)
            else:
                return False


        elif (self.next_token[self.i][0] == "identifier"):
            if(self.match(self.next_token[self.i][0], "identifier")):
                y= self.next_token[self.i][1]

                print(y)

                self.i = self.i + 1
                print(self.next_token[self.i][1])
                return y
            else:
                return False

    def parse(self):

        if(self.program()!=False):
            f = open('output.txt', 'a')
            f.write('\n' + "program found")
            f.close()
            self.g.view()
            return True

f = open('Input.txt', 'r')
text=f.read()
f.close()
s=scanner(text)

parse_input=s.scan()
print(parse_input)
p =parser(parse_input)

p.parse()



















