# SPDX-FileCopyrightText: 2023-present Heath Brown <heathd.brown@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from .cli import isdown

    sys.exit(isdown())
