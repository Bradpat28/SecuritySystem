#!/bin/bash
function uninstall {
	echo "Removing the Security System..."
	rm -r ./.securesys 2> /dev/null
	echo "Finished Removing the Security System"
}

echo -n "Are you sure you want to uninstall the Security System? (y/n): "
read response
case $response in 
	y|y) uninstall ;;
esac
