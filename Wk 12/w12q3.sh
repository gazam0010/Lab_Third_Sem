if [ -z "$1" ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

USERNAME=$1
PASSWORD=$(openssl rand -base64 12)  

useradd -m "$USERNAME"

echo "$USERNAME:$PASSWORD" | chpasswd

echo "User $USERNAME created with password: $PASSWORD"
