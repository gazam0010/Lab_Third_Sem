# Usage: w12q1.sh <source> <destination>
# $1, $2,..., $n: They are special positional variables (are called positional parameters), values from the command line interface are automatically mapped
# to the variables in order.

tar -czf "$2/backup_$(date +%Y%m%d_%H%M%S).tar.gz" -C "$1" .
