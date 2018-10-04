if [[ "$1" == "-h" ]]; then
    exec /usr/libexec/s2i/usage
fi

echo "---> Installing application source"

COPY . /app

WORKDIR /app
