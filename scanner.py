class scanner:


    def __init__(self,inp):
        self.input=inp
        self.start=1
        self.innum=2
        self.inassign=3
        self.incomment=4
        self.done=5
        self.currentstate=6
        self.inid=7

        self.currentstate=self.start
        self.out=[]




    def is_digit(self,s):
        if s.isdigit():
            return 1
        else:
            return 0


    def is_letter(self,s):
        if s.isalpha():
            return 1
        else:
            return 0

    def is_other(self, s):
        if self.is_digit(s) or self.is_letter(s) or s == ":":
            return 0
        else:
            return 1


    def is_reserved(self,s):
        if s=="if" or s=="then" or s=="else" or s=="end" or s=="repeat" or s=="until" or s=="read" or s=="write":
            return 1
        else:
            return 0

    def is_symbol(self, s):
        if s == "+" or s == "-" or s == "*" or s == "/" or s == "=" or s == "<" or s == "()" or s == ";" or s == ":=":
            return 1
        else:
            return 0

    def scan(self):
        i=0
        word=""

        while i<len(self.input):




            if self.currentstate!=self.done:

                if self.currentstate==self.start:

                    if self.input[i]==" ":
                          self.currentstate=self.start
                          i=i+1


                    elif self.input[i] == "{":
                          self.currentstate=self.incomment
                          i=i+1


                    elif self.is_digit(self.input[i]) == 1:
                         self.currentstate=self.innum
                         word=word+self.input[i]
                         i = i + 1


                    elif self.is_letter(self.input[i]) == 1:
                         self.currentstate=self.inid
                         word = word + self.input[i]
                         i = i + 1


                    elif self.input[i] ==":":

                        self.currentstate=self.inassign
                        word = word + self.input[i]
                        i = i + 1
                    else:

                        self.currentstate=self.done
                        word = word + self.input[i]






                elif self.currentstate==self.innum:


                    if self.is_digit(self.input[i]) == 1:
                         self.currentstate=self.innum
                         word = word + self.input[i]
                         i = i + 1


                    else:

                         self.currentstate=self.done
                         i=i-1





                elif self.currentstate==self.inid:


                     if self.is_letter(self.input[i]) == 1:
                        self.currentstate=self.inid
                        word = word + self.input[i]
                        i = i + 1


                     else:

                         self.currentstate=self.done
                         i=i-1;






                elif self.currentstate==self.inassign:


                    if self.input[i] == "=":
                         self.currentstate=self.done
                         word = word + self.input[i]




                    else:

                        self.currentstate=self.done
                        i=i-1



                elif self.currentstate==self.incomment:


                    if self.input[i] == "}":
                        self.currentstate=self.start
                        i = i + 1


                    else:

                        self.currentstate=self.incomment
                        i=i+1

            else:
                 self.currentstate=self.start


                 if self.is_reserved(word) :
                     self.out.append([word,word])
                     f = open('output_scanner.txt', 'a')
                     f.write('\n' + word+" : "+"reserved")
                     f.close()







                 elif self.is_symbol(word):
                     self.out.append([word,word])

                     f = open('output_scanner.txt', 'a')
                     f.write('\n' + word + " : " + "special symbol")
                     f.close()




                 elif word[0].isalpha():
                     self.out.append(["identifier",word])

                     f = open('output_scanner.txt', 'a')
                     f.write('\n' + word + " : " + "identifier")
                     f.close()






                 elif word[0].isdigit():
                     self.out.append(["number",word])

                     f = open('output_scanner.txt', 'a')
                     f.write('\n' + word + " : " + "number")
                     f.close()





                 word=""
                 i=i+1
        return self.out










