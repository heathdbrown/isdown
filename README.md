# isdown
> Uses python, rich, and click to check the status of a website.

![Screenshot 2023-01-25 094210](https://user-images.githubusercontent.com/618460/214607921-f188bb8a-1291-4018-b206-0d5e3eabd991.png)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install isdown

```

## Running

- Just with a site argument, can be as many as you want.

```console
isdown check https://github.com https://google.com
```

- With an input filel

```console
isdown check --input_file sites.txt
```

- with both input file and sites as args
```console
isdown check https://github.com --input_file sites.txt
```

## License

`isdown` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
