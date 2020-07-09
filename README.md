# Tourism recommendation system

A toy example.

### Requirements

* [conda](https://www.anaconda.com/products/individual)

### Install database

**Step 1**: Install neo4j-community package (Archlinux): 

```bash
yay -S neo4j-community
```

**Step 2**: Disable SERVER authentication.

1. Edit config file:
```bash
vim /etc/conf/neo4j.conf
```
2. Change `dbms.security.auth_enabled` to `false`.

**Step 3**: Start server.

```bash
sudo systemctl restart neo4j
```

### Setup project


**Step 1**: Create conda environment to run project notebook.

```bash
conda env create -f environment.yml
```

**Step 2**: Enable installed environment.

```bash
conda activate neo4j-recomendations
```

**Step 3**: Install a upyter extension required to support a progress bar in a notebook.

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### Getting started

**Step 1**: Enable installed environment.

```bash
conda activate neo4j-recomendations
```

**Step 2**: run jypiter lab IDE:

```bash
jupyter lab
```

**Step 3**: Open [toy-example](toy-example.ipynb) jypiter notebook.

**Note**: Can use query browser from http://localhost:7474.
