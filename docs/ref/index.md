---
---cription: |
--- API documentation for modules: ref.

---g: en

---ssoption: oneside
---metry: margin=1in
---ersize: a4

---kcolor: blue
---ks-as-notes: true
---


--- 
---odule `ref` {#ref}

---use this module just use the main function at the top of your code




--- 
---Functions


--- 
--- Function `main` {#ref.main}




---   def main(
---       __builtins__: module,
---       restrictwrite: bool = False,
---       level: int = 0
---   ) ‑> NoneType


---sage

---### Basic usage

---py
---ort ref
---.main(__builtins__)
---

---### Additional options

---<code>restrictwrite</code> allows you to prevent Python files from using open to overwrite files.

---trictwrite: `bool | default False`

---<code>level</code> allows you to choose a specific level of restriction

---el: `int | default 0`



-----
---erated by *pdoc* 0.9.2 (<https://pdoc3.github.io>).
