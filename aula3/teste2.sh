echo -n "Indique qual a directoria que pretende "
read n

din=`find $n -name ficha* -printf "%s "`
soma=0
for i in $din
do
     soma=$((soma+i))

done
echo $soma