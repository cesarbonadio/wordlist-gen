
import sys,itertools,os,time

os.system("clear") 
                                                                                                                                 
 
if len(sys.argv)>=5:

    try:
        min_lenght=int(sys.argv[1])
        max_lenght=int(sys.argv[2])
        chars=sys.argv[3]
        file=open(sys.argv[4], "w")

        for n in range(min_lenght, max_lenght + 1):
            for xs in itertools.product(chars, repeat=n):

                string=''.join(xs)
                file.write(string + "\n")
                sys.stdout.write('\r[+] saving character `%s`' % string)
                sys.stdout.flush()

        print "\n[+] Wordlist creada : " + sys.argv[4]
        print ('\n[-] End time: %s' % time.strftime('%H:%M:%S'))
        file.close()

    except KeyboardInterrupt:
        print "\n[x] Saliendo ..."

else:
    print "\nUso : python gen.py min_l max_l string output_file"
