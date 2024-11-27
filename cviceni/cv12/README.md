# Cvičení 12

## Příprava
> [!Warning] Chyba při instalaci knihovny `transformers`
```bash	
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\jaros\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages\\transformers\\models\\deprecated\\trajectory_transformer\\convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

- [enable-long-paths-in-windows-10](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later)


Spusťtě PowerShell jako správce a zadejte následující příkaz:
```PowerShell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

## Cuda

### Windows

- [CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/)