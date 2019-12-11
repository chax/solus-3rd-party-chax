# Personal 3rd party Solus repo
Disclaimer: install this at your own risk. This is unofficial Solus 3rd party repo and Solus team doesn't claim any responsibility for content of this repository, as neither do I as the maintainer of this repository.

## Installing packages
To install a package just follow instructions...

### Teams
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/chax/solus-3rd-party-chax/master/network/im/teams/pspec.xml
sudo eopkg it teams-*.eopkg;sudo rm teams-*.eopkg
```

### ObinsKit
```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/chax/solus-3rd-party-chax/master/system/utils/obinskit/pspec.xml
sudo eopkg it obinskit-*.eopkg;sudo rm obinskit-*.eopkg
```