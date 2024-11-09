THRESHOLD=0

USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Warning: Disk usage has reached $USAGE%, exceeding the threshold of $THRESHOLD%."
fi
