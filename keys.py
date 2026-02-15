var1="""SET keys TO $'''$hello'''
SET progman TO $'''c:\\windows\\system32\\$notepad.exe'''
System.RunApplication.RunApplication ApplicationPath: progman WindowStyle: System.ProcessWindowStyle.Maximized ProcessId=> AppProcessId
WAIT 5
MouseAndKeyboard.SendKeys.FocusAndSendKeys TextToSend: keys DelayBetweenKeystrokes: 10 SendTextAsHardwareKeys: False
"""
print("\033c\033[40;37m\n give me windows program to run like 'notepad.exe' ? ")
a=input()
print("\033[40;37m\n give me text to send to app  ? ")
b=input()
var1=var1.replace("$hello",b)
var1=var1.replace("$notepad.exe",a)
print("\n"+"-"*80 +"\n")
print(var1)