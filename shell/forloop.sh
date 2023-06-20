echo "Enter the text you want to print:"
read text
echo "how may times you want to print the text ?"
read times
if [[ "$times" =~ ^[0-9]+$ && "$times" -gt 0 ]]
    then
        for (( i=0; i<times; i++ ))
            do
            echo $text
            sleep 1
            done
else
echo "Error : Invalid Input"
exit
fi