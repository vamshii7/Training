#!/bin/bash
echo "Enter a group name to search"
read grp
members=`getent group $grp`
echo "Members of the group are:\n $members"