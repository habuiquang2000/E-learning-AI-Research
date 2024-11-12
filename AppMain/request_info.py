# https://stackoverflow.com/questions/13203868/how-to-write-to-csv-and-not-overwrite-past-text
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
from datetime import datetime
# import csv
from LogsHistory.models import Log, LogStatus


# def write_log_csv(req, time, msg):
#     header = ["ip", "time"]
#     row = [
#         [req, time, msg]
#     ]
#     # open the file in the write mode
#     # with open("logs.csv", "w") as f:
#     with open("logs.csv", "a") as f:
#         # f = open("path/to/csv_file", "w")
#         # create the csv writer
#         writer = csv.writer(f)

#         # write a row to the csv file
#         writer.writerows(row)
#         # writer.writerow(row)

#         # close the file
#         # f.close()


def get_server_name(request):
    return request.META.get("COMPUTERNAME")


def get_client_ip(request):
    # https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # ip = x_forwarded_for.split(",")[-1].strip()
        return x_forwarded_for.split(",")[0]
    else:
        return request.META.get("REMOTE_ADDR")


def get_client_info(request):
    return request.META.get("HTTP_USER_AGENT")


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        log_status = LogStatus.SUCCESS

        ip = get_client_ip(request)
        machine_name = get_server_name(request)
        machine_info = get_client_info(request)

        now = datetime.now()
        # return request.META.get()
        META = request.META
        # special variables
        # function variables
        # 'ALLUSERSPROFILE': 'C:\\ProgramData'
        # 'ANDROID_HOME': 'D:\\SetNewWin\\Portable\\Android\\Sdk'
        # 'APPDATA': 'C:\\Users\\anmqu\\AppData\\Roaming'
        # 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_2172_TNIPNOOKUVJOKPRN'
        # 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files'
        # 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files'
        # 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files'
        # 'COMPUTERNAME': 'ANM-02'
        # 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe'
        # 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData'
        # 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer'
        # 'FPS_BROWSER_USER_PROFILE_STRING': 'Default'
        # 'HOMEDRIVE': 'C:'
        # 'HOMEPATH': '\\Users\\anmqu'
        # 'JAVA_HOME': 'D:\\SetNewWin\\Portable\\Java\\jdk-20'
        # 'LOCALAPPDATA': 'C:\\Users\\anmqu\\AppData\\Local'
        # 'LOGONSERVER': '\\\\ANM-02'
        # 'NUMBER_OF_PROCESSORS': '12'
        # 'NVM_HOME': 'D:\\SetNewWin\\Portable\\nvm'
        # 'NVM_SYMLINK': 'C:\\Program Files\\nodejs'
        # 'ONEDRIVE': 'C:\\Users\\anmqu\\OneDrive'
        # 'ONEDRIVECONSUMER': 'C:\\Users\\anmqu\\OneDrive'
        # 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined'
        # 'OS': 'Windows_NT'
        # 'PATH': 'D:\\___Product\\Viu-documents-search\\.venv\\Scripts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\dotnet\\;D:\\SetNewWin\\Portable\\flutter\\bin;D:\\SetNewWin\\Portable\\flutter;D:\\SetNewWin\\Portable\\nvm;C:\\Program Files\\nodejs;D:\\SetNewWin\\Portable\\Python39;D:\\SetNewWin\\Portable\\Python39\\Scripts;D:\\SetNewWin\\Portable\\Android\\Sdk;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;D:\\SetNewWin\\Portable\\Java\\jdk-20\\bin;C:\\Program Files\\Cloudflare\\Cloudflare WARP\\;D:\\SetNewWin\\Portable\\Android\\Sdk\\platform-tools;D:\\SetNewWin\\Portable\\Git\\bin;D:\\SetNe...
        # 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW'
        # 'PROCESSOR_ARCHITECTURE': 'AMD64'
        # 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD'
        # 'PROCESSOR_LEVEL': '23'
        # 'PROCESSOR_REVISION': '6001'
        # 'PROGRAMDATA': 'C:\\ProgramData'
        # 'PROGRAMFILES': 'C:\\Program Files'
        # 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)'
        # 'PROGRAMW6432': 'C:\\Program Files'
        # 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\PowerShell\\Modules\\'
        # 'PUBLIC': 'C:\\Users\\Public'
        # 'SESSIONNAME': 'Console'
        # 'SYSTEMDRIVE': 'C:'
        # 'SYSTEMROOT': 'C:\\WINDOWS'
        # 'TEMP': 'C:\\Users\\anmqu\\AppData\\Local\\Temp'
        # 'TMP': 'C:\\Users\\anmqu\\AppData\\Local\\Temp'
        # 'USERDOMAIN': 'ANM-02'
        # 'USERDOMAIN_ROAMINGPROFILE': 'ANM-02'
        # 'USERNAME': 'anmqu'
        # 'USERPROFILE': 'C:\\Users\\anmqu'
        # 'VIRTUAL_ENV': 'D:\\___Product\\Viu-documents-search\\.venv'
        # 'WINDIR': 'C:\\WINDOWS'
        # 'TERM_PROGRAM': 'vscode'
        # 'TERM_PROGRAM_VERSION': '1.84.2'
        # 'LANG': 'en_US.UTF-8'
        # 'COLORTERM': 'truecolor'
        # 'GIT_ASKPASS': 'd:\\SetNewWin\\Portable\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh'
        # 'VSCODE_GIT_ASKPASS_NODE': 'D:\\SetNewWin\\Portable\\Microsoft VS Code\\Code.exe'
        # 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node'
        # 'VSCODE_GIT_ASKPASS_MAIN': 'd:\\SetNewWin\\Portable\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js'
        # 'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-10eb646350-sock'
        # '_OLD_VIRTUAL_PATH': 'C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\dotnet\\;D:\\SetNewWin\\Portable\\flutter\\bin;D:\\SetNewWin\\Portable\\flutter;D:\\SetNewWin\\Portable\\nvm;C:\\Program Files\\nodejs;D:\\SetNewWin\\Portable\\Python39;D:\\SetNewWin\\Portable\\Python39\\Scripts;D:\\SetNewWin\\Portable\\Android\\Sdk;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\150\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;D:\\SetNewWin\\Portable\\Java\\jdk-20\\bin;C:\\Program Files\\Cloudflare\\Cloudflare WARP\\;D:\\SetNewWin\\Portable\\Android\\Sdk\\platform-tools;D:\\SetNewWin\\Portable\\Git\\bin;D:\\SetNewWin\\Portable\\Git;D:\\SetNewWin\\Portable\\MongoDB\...
        # 'SECRET_KEY': 'django-insecure-kd27)6+rnct2483%e&ykk$p7)x#&c(9@)of&7b#i=#4ke9(t&('
        # 'TEMPLATES_DIRS': './templates,'
        # 'DATABASE_ENGINE': 'django.db.backends.postgresql_psycopg2'
        # 'DATABASE_HOST': 'localhost'
        # 'DATABASE_NAME': 'viu-document'
        # 'DATABASE_USER': 'anmquangw'
        # 'DATABASE_PASSWORD': 'Nha2812002'
        # 'DATABASE_PORT': '5432'
        # 'LANGUAGE_CODE': 'vi'
        # 'TIME_ZONE': 'Asia/Ho_Chi_Minh'
        # 'APPLICATION_INSIGHTS_NO_DIAGNOSTIC_CHANNEL': '1'
        # 'ELECTRON_RUN_AS_NODE': '1'
        # 'PROMPT': '(.venv) $P$G'
        # 'PYTHONIOENCODING': 'utf-8'
        # 'PYTHONUNBUFFERED': '1'
        # 'VSCODE_AMD_ENTRYPOINT': 'vs/workbench/api/node/extensionHostProcess'
        # 'VSCODE_CODE_CACHE_PATH': 'C:\\Users\\anmqu\\AppData\\Roaming\\Code\\CachedData\\1a5daa3a0231a0fbba4f14db7ec463cf99d7768e'
        # 'VSCODE_CRASH_REPORTER_PROCESS_TYPE': 'extensionHost'
        # 'VSCODE_CWD': 'D:\\___Product\\Viu-documents-search'
        # 'VSCODE_HANDLES_UNCAUGHT_ERRORS': 'true'
        # 'VSCODE_IPC_HOOK': '\\\\.\\pipe\\de43b0c067030b0923ceab36f72783fe-1.84.2-main-sock'
        # 'VSCODE_NLS_CONFIG': '{"locale":"en-us","osLocale":"en-us","availableLanguages":{},"_languagePackSupport":true}'
        # 'VSCODE_PID': '2172'
        # '_OLD_VIRTUAL_PROMPT': '$P$G'
        # 'PYDEVD_USE_FRAME_EVAL': 'NO'
        # 'DJANGO_SETTINGS_MODULE': 'AppMain.settings.developement'
        # 'RUN_MAIN': 'true'
        # 'SERVER_NAME': 'ANM-02'
        # 'GATEWAY_INTERFACE': 'CGI/1.1'
        # 'SERVER_PORT': '8080'
        # 'REMOTE_HOST': ''
        # 'CONTENT_LENGTH': ''
        # 'SCRIPT_NAME': ''
        # 'SERVER_PROTOCOL': 'HTTP/1.1'
        # 'SERVER_SOFTWARE': 'WSGIServer/0.2'
        # 'REQUEST_METHOD': 'GET'
        # 'PATH_INFO': '/'
        # 'QUERY_STRING': ''
        # 'REMOTE_ADDR': '192.168.1.1'
        # 'CONTENT_TYPE': 'text/plain'
        # 'HTTP_HOST': 'anmquangw.ddns.net:8080'
        # 'HTTP_CONNECTION': 'keep-alive'
        # 'HTTP_CACHE_CONTROL': 'max-age=0'
        # 'HTTP_UPGRADE_INSECURE_REQUESTS': '1'
        # 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        # 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        # 'HTTP_ACCEPT_ENCODING': 'gzip, deflate'
        # 'HTTP_ACCEPT_LANGUAGE': 'vi,en-US;q=0.9,en;q=0.8'
        # 'HTTP_COOKIE': 'csrftoken=j1m66A2I6F14uCuGMyIkMDfwnXGYGGWb; sessionid=raibkr9t4gxhznartilvmxnuwvcoo05v'
        # 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x0000014CA82D1730>
        # 'wsgi.errors': <_pydevd_bundle.pydevd_io.IORedirector object at 0x0000014CA5658880>
        # 'wsgi.version': (1, 0)
        # 'wsgi.run_once': False
        # 'wsgi.url_scheme': 'http'
        # 'wsgi.multithread': True
        # 'wsgi.multiprocess': False
        # 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>
        # len(): 114

        # current_time = now.strftime("%H:%M:%S %d/%m/%Y")

        log = Log(
            STATUS=log_status,
            METHOD=request.method,
            SCHEME=request.scheme,
            DOMAIN=request.META.get('HTTP_HOST'),
            ENDPOINT=request.path,
            TIME=now,
            IP=ip,
            MACHINENAME="machine_name",
            MACHINEINFO=machine_info,
        )
        log.save()

        # write_log_csv(request, current_time, ip)

        # print(f"{current_time} - {ip}")
        # print("="*10)

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware


# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         response = self.get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response


# middleware_sample/middlewares.py
# class DemoMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         response = self.get_response(request)
#         print("This is demo middleware in Django")
#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

#     def process_exception(self, request, exception):
#         pass

#     def process_template_response(self, request, response):
#         pass
