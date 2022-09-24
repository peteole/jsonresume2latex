if [ $# -eq 0 ]
  then
    echo "Pleasy specify a tag!"
    exit 1
fi
docker build -t olepetersen/jsonresume2latex:$1 .
docker push olepetersen/jsonresume2latex:$1