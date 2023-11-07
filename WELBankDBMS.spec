# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['win_01_WelcomeLogin.py', 'win_02_1_CusServDashboard.py', 'win_02_2_HRDashboard.py', 'win_02_3_QueryInterface_CS.py', 'win_02_3_QueryInterface_HR.py', 'win_03_1_1_CusTable.py', 'win_03_1_2_AccTable.py', 'win_03_1_3_CardsTable.py', 'win_03_1_4_TxnTable.py', 'win_03_1_5_LoansTable.py', 'win_03_1_6_LnpayTable.py', 'win_03_2_1_empTable.py', 'win_03_2_2_jobsTable.py', 'win_03_2_3_depTable.py', 'win_03_2_4_brchTable.py', 'win_03_2_5_locTable.py', 'win_03_2_6_regTable.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WELBankDBMS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['bank.ico'],
)
