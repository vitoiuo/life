# Conway's Game of Life

<details>
  <summary> Rules </summary>

### For a space that is populated

- Each cell with one or no neighbors die;
- Each cell with four or more neighbors dies;
- Each cell with two or three neighbors survives.

### For a space that is empty or unpopulated

- Each cell with three neighbors becomes populated.

</details>

## This repository

This repository has two versions of Conway's Game of Life, one of them (the Vue one) can be acessed via this repository github page.

![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/home/victorbarreto/Documentos/busertech-tony/life/assets/life.gif?version%3D1671843195113)


## Setup guide

```bash

Python Version (uses python v.3.10.0)

cd life-py

# (optional) activate a environment for project dependencies

pip install -r requirements.txt

python life.py
```

```bash
Vue version

cd life-vue

npm install

# for local initialization
npm run serve

# for local build
npm run build
```
