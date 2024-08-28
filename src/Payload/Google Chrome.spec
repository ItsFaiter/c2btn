# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bot.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Google Chrome',
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
    icon=['Google-Chrome-Logo-1536x1536-3017027129.ico'],
)
app = BUNDLE(
    exe,
    name='Google Chrome.app',
    icon='Google-Chrome-Logo-1536x1536-3017027129.ico',
    bundle_identifier=None,
)
