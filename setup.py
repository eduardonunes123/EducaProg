import cx_Freeze

executables = [cx_Freeze.Executable('personagem.py')]

cx_Freeze.setup(
    name="Jogo sobre programacao",
    options={'build_exe': {'packages': ['pygame'],
                           'include_files': ['imagens', 'audio']}},

    executables=executables

)
