#!/usr/bin/env python3

import os
import re
import sys
from pathlib import Path


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


id_server = require_env("RUSTDESK_ID_SERVER")
public_key = require_env("RUSTDESK_PUBLIC_KEY")

config_path = Path("libs/hbb_common/src/config.rs")

if not config_path.exists():
    print(f"Could not find {config_path}", file=sys.stderr)
    sys.exit(1)

text = config_path.read_text(encoding="utf-8")

text = re.sub(
    r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\[[^\]]*\];',
    f'pub const RENDEZVOUS_SERVERS: &[&str] = &["{id_server}"];',
    text,
)

text = re.sub(
    r'pub const RS_PUB_KEY: &str = "[^"]*";',
    f'pub const RS_PUB_KEY: &str = "{public_key}";',
    text,
)

config_path.write_text(text, encoding="utf-8")

print("Patched RustDesk self-host defaults:")
print(f"  RENDEZVOUS_SERVERS = {id_server}")
print("  RS_PUB_KEY = [set]")
