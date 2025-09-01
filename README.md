# modbustcp-flood

A tiny CLI tool to stress-test a Modbus/TCP endpoint by rapidly opening TCP sessions to the target host. Useful for validating rate-limits, connection handling, and resilience of Modbus gateways and PLC front-ends in a lab environment.

---

## Installation

```bash
pipx install git+https://github.com/CoLorenzo/modbustcp-flood
```

> `pipx` installs the app in an isolated environment and exposes the `modbustcp-flood` command on your PATH.

Upgrade later with:

```bash
pipx upgrade modbustcp-flood
```

Uninstall:

```bash
pipx uninstall modbustcp-flood
```

---

## Usage

```text
usage: modbustcp-flood [-h] -a ADDRESS [-p PORT]

options:
  -h, --help            show this help message and exit
  -a, --address ADDRESS
                        Server Address
  -p, --port PORT       Server port (optional; default: 502)
```

### Examples

Run against a device at `192.168.1.50` on the default Modbus/TCP port:

```bash
modbustcp-flood -a 192.168.1.50
```

Use a non-standard port (e.g., 1502):

```bash
modbustcp-flood -a 192.168.1.50 -p 1502
```

Stop with `Ctrl+C`.

---
