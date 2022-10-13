to import a tex file from the host to docker continer
use: docker cp file.name 369e644036bf:root

One specific file can be copied FROM the container like:
docker cp 369e644036bf:root/y/file.name file.name


