"""
This file contains gets the environment variables from the system.

Author: @marekkoc

Created: 2025-03-15
Modified: 2025-03-15
"""

import os

class EnvVars:
    """
    This class contains the environment variables for the project.
    """
    env_vars = os.environ

    @classmethod
    def get_env_var(cls, var_name):
        return cls.env_vars[var_name]
    
    @classmethod
    def get_mk_projekty(cls):
        if "MK_PROJEKTY" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa MK_PROJEKTY nie istnieje")
        return cls.get_env_var("MK_PROJEKTY")

    @classmethod
    def get_mk_pakiety(cls):
        if "MK_PAKIETY" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa MK_PAKIETY nie istnieje")
        return cls.get_env_var("MK_PAKIETY")
     
    @classmethod
    def get_mk_cytaty(cls):
        if "MK_CYTATY" not in cls.env_vars:
            raise KeyError("Zmienna środowiskowa MK_CYTATY nie istnieje")
        return cls.get_env_var("MK_CYTATY")


if __name__ == "__main__":
    print()
    print(EnvVars.get_mk_projekty())
    print(EnvVars.get_mk_pakiety())
    print(EnvVars.get_mk_cytaty())
    print()


