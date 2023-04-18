# tensorflow-playground

_Python 3.10.11_

### Environment setup

_for MacOS with Apple Silicon_

1. create virtual environment

```shell
python3 -m venv ~/tf-env
source ~/tf-env/bin/activate
python -m pip install -U pip
```

2. clone repository and enter

```shell
git clone <URL>
cd tensorflow-playground
```

3. install dependencies

```shell
pip install -r requirements.txt
```

_to update dependencies run `pip freeze > requirements.txt`_

### Start server

1. run `server.py`

```shell
flask --app server --debug run
```

_use `--debug` flag during development to auto-reload server on save_

### Resolve server not updating

1. run flask app _(port 500 by default)_

```shell
flask --app server --debug run
```

2. find process ID

```shell
netstat -vn | grep -E "options|5000"
```

3. kill process with process id _(i.e. 541)_

```shell
sudo kill 541
```

4. confirm process killed

```shell
netstat -vn | grep -E "options|5000"
```
