#!/usr/bin/env python3

import json
import os
import sys
from pathlib import Path


CONFIG_NAME = "LeeHollowRustDesk.toml"
CONFIG2_NAME = "LeeHollowRustDesk2.toml"


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def optional_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def toml_string(value: str) -> str:
    return json.dumps(value)


id_server = require_env("RUSTDESK_ID_SERVER")
public_key = require_env("RUSTDESK_PUBLIC_KEY")
relay_server = optional_env("RUSTDESK_RELAY_SERVER")
api_server = optional_env("RUSTDESK_API_SERVER")
output_dir = Path(optional_env("RUSTDESK_CONFIG_OUTPUT_DIR") or "rustdesk")

if not output_dir.exists():
    print(f"Could not find output directory: {output_dir}", file=sys.stderr)
    sys.exit(1)

options = {
    "custom-rendezvous-server": id_server,
    "key": public_key,
}
if relay_server:
    options["relay-server"] = relay_server
if api_server:
    options["api-server"] = api_server

config_path = output_dir / CONFIG_NAME
config2_path = output_dir / CONFIG2_NAME

# The primary config is intentionally empty. The bundled server settings live in
# Config2's options table, matching RustDesk's stored server-option location.
config_path.write_text("", encoding="utf-8")

config2_lines = ["[options]"]
for key in sorted(options):
    config2_lines.append(f"{toml_string(key)} = {toml_string(options[key])}")
config2_path.write_text("\n".join(config2_lines) + "\n", encoding="utf-8")

print("Prepared bundled RustDesk server configuration:")
print(f"  {config_path}")
print(f"  {config2_path}")
print("  custom-rendezvous-server = [set]")
print(f"  relay-server = {'[set]' if relay_server else '[not set]'}")
print(f"  api-server = {'[set]' if api_server else '[not set]'}")
print("  key = [set]")
