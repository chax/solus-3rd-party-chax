# Personal 3rd party Solus repo
Disclaimer: install this at your own risk. This is unofficial Solus 3rd party repo and Solus team doesn't claim any responsibility for content of this repository, as neither do I as the maintainer of this repository.

## Installing packages
To install a package just follow instructions...
Git clone this repo, change directory to package you want to install, then execute these commands:

```sh
sudo eopkg.py3 bi --ignore-safety pspec.xml
sudo eopkg it *.eopkg;sudo rm *.eopkg
```

If you want to install it without cloning this git repository, just use url instead `pspec.xml` file path:
```
https://raw.githubusercontent.com/chax/solus-3rd-party-chax/master/{path_to_package}/pspec.xml
```
