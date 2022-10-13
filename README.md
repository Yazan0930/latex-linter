to import a tex file from the host to docker continer
use: docker cp file.name c92c843d5e88:root/files

One specific file can be copied FROM the container like:
docker cp c92c843d5e88:root/y updated_latex_file


