"""#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------"""
import string
a=list(string.ascii_lowercase)
def print_rangoli(size):
    alpha=a[0:size]
    alpha.reverse()
    down=[]
    for j in range(0,size):
            up=[]
            if j == 0:
                up.append(alpha[0].center(4*size-3,'-'))
            else:
                up.append(alpha[0].rjust(2*size-1-j*2,'-'))

                for i in range(j):
                        if i>0:
                            up.append(alpha[i].rjust(2,'-'))

                if j >0:
                        up.append(alpha[j].center(3,'-'))

                for i in range(j):
                        if i >0:
                                up.append(alpha[j-i].ljust(2,'-'))

                up.append(alpha[0].ljust(size*2-1-j*2,'-'))

            up=''.join(up)
            down.append(up)
            print(up)
    down.pop()
    down.reverse()
    for i in range(len(down)):
        print(down[i])




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
