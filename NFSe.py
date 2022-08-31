# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# VERSAO
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from binaries.module import *
ver = "2.1.0"


# ///////////////////////////////////////////////////////////////
# MESSAGEBOX
# ///////////////////////////////////////////////////////////////

version = f"""///////////////////////////////////////////////////////////////

{program_name} {main_name} V{ver}

///////////////////////////////////////////////////////////////"""

if __name__ == "__main__":
    print(version)
    window = App()
    window.login_window()
    window.mainloop()
