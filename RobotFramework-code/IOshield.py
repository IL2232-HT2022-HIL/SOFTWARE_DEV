import subprocess
class IOshield():
    COMPONENTS = ['LED1', 'Button1', 'Switch1']
    #to save commands in a .txt file, not needed for now
    #def text_save(content,filename,mode='a'):
        # Try to save a list variable in txt file.
        #file = open(filename,mode)
        #for i in range(len(content)):
        #    file.write(str(content[i])+'\n')
        #file.close()
    def ping(self,host):
        command = ['ping','-c', '2', host]
        print(subprocess.call(command))
    def print_number(self, number):
        print(number)
    def push(self, components):
        if components not in self.COMPONENTS:
            raise ValueError('Invalid component!')
        else:
            self.print_number(components)
            self.ping('google.com')
            #self.text_save(components, 'test.txt')

if __name__=="__main__":
    a = IOshield()
    IOlist=a.COMPONENTS
    test=a.push('LED1')
    print(IOlist)
    a.ping('google.com')