import pywinauto, time
from pywinauto import *
web_address = 'https://www.baidu.com'
app = application.Application(backend='uia').start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe {}".format(web_address))
wins = app.windows().waitFor(1)
print(wins)
# dlg = app.window(title="无标题 - 记事本")
# dlg.print_control_identifiers()
