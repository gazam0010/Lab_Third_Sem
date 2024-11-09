
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <pattern> <filename>"
    exit 1
fi

PATTERN=$1
FILENAME=$2

if grep -q "$PATTERN" "$FILENAME"; then
    grep "$PATTERN" "$FILENAME"
else
    echo "No matches found for '$PATTERN' in $FILENAME."
fi
