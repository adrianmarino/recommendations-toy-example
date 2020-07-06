### Install database
1. `yay -S neo4j-community`
2. `sudo systemctl start neo4j`
3. disable SERVER authentication:
     1. `vim /etc/conf/neo4j.conf`
     2. Change `dbms.security.auth_enabled=false`

### Setup project
3. `conda env create -f environment.yml`
4. `conda activate neo4j-recomendations`
5. `jupyter labextension install @jupyter-widgets/jupyterlab-manager`


### Getting started

1. `conda activate neo4j-recomendations`
2. `jupyter lab`
3. Open **toy-example.ipynb** notebook.
4. Query browser: http://localhost:7474
