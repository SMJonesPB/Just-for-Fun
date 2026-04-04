; WarInstaller.iss

#define MyAppVersion "1.0.0"
AppVersion={#MyAppVersion}

[Setup]
AppName=War
AppVersion={#MyAppVersion}
DefaultDirName={pf}\War
DefaultGroupName=War
OutputDir=installer
OutputBaseFilename=WarSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\War\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\War"; Filename: "{app}\War.exe"
Name: "{commondesktop}\War"; Filename: "{app}\War.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"

[Run]
Filename: "{app}\War.exe"; Description: "Launch War"; Flags: nowait postinstall skipifsilent