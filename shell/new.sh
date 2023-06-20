echo "Enter file path:"
read path
perm=`stat -c %a $path`
echo "Current file permissions are:" $perm
echo "Do you want to change file permissions ?(yes/no) : "
read decision
if [[ $decision=="yes" ]]
then
    echo "Enter the permisions you want to give (eg:746) :"
    read newperm
    `sudo chmod $newperm $path`
    nperm=`stat -c %a $path`
    echo "permissions updated successfully, new permissions for the file are:" $nperm
else
    echo "exiting.."
fi



