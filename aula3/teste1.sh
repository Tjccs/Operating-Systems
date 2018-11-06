din=`find . -name ficha* -printf "%s "`
soma=0
for i in $din
do
     soma=$((soma+i))

done
echo $soma