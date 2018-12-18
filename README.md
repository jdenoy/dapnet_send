# DAPNET Send


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
A linux or cygwin environment running python 2.x or 3.X

### Installing
Install all python requirements :

```
sudo pip install -r requirements.txt
```

## Usage

note : values in between '[' ']' are optional

* dapnet_send.py
```
dapnet_send.py callsign "message" [debug]
```
* dapnet_bulk_send.py
```
dapnet_bulk_send.py callsign_file_list "message" [debug]
```
callsign_file_list is a file containing one callsign per line. End of line being in 'LF' mode.
Ex :
```
callsign1
callsign2
callsign3
```

* dapnet_rubric_send.py
```
dapnet_rubric_send.py rubric "message" [debug]
```

## Authors

* **Johan DENOYER** - *Initial work* - [jdenoy](https://github.com/jdenoy)


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
