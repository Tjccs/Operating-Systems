#!/bin/sh


if [ $# -eq 0 ]
            then echo "Falta argumentos"
            exit 1
fi

int=0
neg=0
zero=0
a = 0
for i in $*
    do
        
        a=$((a+i))
        re='^[0-9]+$'
        if ![[ $i =~ $re2 ]] ;
            then echo "String" >&2; exit 1
        elif [ $i -lt 0 ]
            then echo "$i eh um numero inteiro negativo"
            neg=$((neg+1))
        elif [ $i -eq 0 ]
            then echo "$i eh o numero zero"
            zero=$((zero+1))
              
        else echo "$i eh um numero inteiro positivo"
            int=$((int+1))
        fi
        
    done
echo $neg
echo $zero
echo $int
echo $a



