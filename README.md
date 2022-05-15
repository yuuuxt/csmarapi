# Installable csmarapi python package

[Original package documentation](https://cn.gtadata.com/#/support/doc) is to some extent ambiguous, e.g. 

- python 3.6 only;
- windows only;
- requires `websocket`.

This modified package is just installable like a normal package. If it's installed then it works.

It is finished in a rush and hasn't been tested, but should be working.

# How it's done

- Grabbed source data from csmar;
- Specify dependencies;
- Make it a package.

**No other changes are made.** Or you can do it by yourself by checking commit history.

Current version is based on csmarapi.rar SHA1: 7EA9D274FFE7CBBF11A254879B941D7FBDAEC0B4

# How to use

Download as zip, `cd` to the extracted folder, and run 

`pip install -e .` 

Here `-e`  means it's an editable installation, so 

- in the future you can sync with updates from original package (manually);
- **don't delete the extracted files otherwise it no longer works**;
- or you can just run `pip install .` to have a default installation.

# ref
- [pip doc](https://pip.pypa.io/en/stable/cli/pip_install/#options)
- [csmar](https://cn.gtadata.com/#/support/doc)
