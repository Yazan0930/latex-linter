docker build -t latex-linter .

docker run -it latex-linter /bin/bash

liter -h


To se image ID RUN: docker ps

to import a tex file from the host to docker continer
use: docker cp file.name/ 4dc905048d36:root/files

One specific file can be copied FROM the container like:
docker cp 4dc905048d36:root/files/(file.name or folder) (file.name or folder)


