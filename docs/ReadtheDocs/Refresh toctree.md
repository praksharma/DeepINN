# Refresh `toctree`

Once Sphinx build a `rst` or `md` file it doesn't rebuild its `toctree` to save build time. If you have renamed/ modified some files, than you might still see the older names.

The solution is to delete `_build` and again use `make run`.