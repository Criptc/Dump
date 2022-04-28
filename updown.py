Al='.py'
Ak='Directory listing for %s'
Aj='video/'
Ai='content-length'
Ah='referer'
Ag='HTTP/1.0'
Af=b'\r\n'
Ae='strict'
Ad='latin-1'
Ac='keep-alive'
Ab='Connection'
Aa=ConnectionResetError
AZ=filter
AY=TypeError
AX=KeyError
AW=IndexError
A0='text/plain'
A8='\n'
z='='
x='content-type'
w='_headers_buffer'
v='close'
A7='2big'
u=OSError
A6=UnicodeDecodeError
A5=Exception
A4=open
m='HTTP/0.9'
a='?'
r='text/html; charset=%s'
q='surrogateescape'
Z='.'
W=hasattr
P=int
f='surrogatepass'
e='utf-8'
Y='Content-type'
X=ValueError
V='Content-Length'
M=True
L=''
J=print
H=str
G=len
F='/'
E=False
C=None
Q='G:\\'
A1=6969
A9=L.encode(e)
R='G:/py-server/'
AA=['send2trash']
from subprocess import call
import sys as O,tempfile as AB,random,string as A2,os as B,shutil as o,pkg_resources as AC
AD=[A.key for A in AC.working_set]
j=E
for n in AA:
	if n not in AD:call([O.executable,'-m','pip','install','--disable-pip-version-check','--quiet',n])
from send2trash import send2trash as AE,TrashPermissionError as AF
y=AB.gettempdir()+'/zip_temp/'
T=dict()
c=[]
o.rmtree(y,ignore_errors=M)
try:B.mkdir(path=y)
except FileExistsError:pass
if not B.path.isdir(R):
	try:B.mkdir(path=R)
	except:R='./'
A3='\n<!DOCTYPE HTML>\n\n<html>\n<meta http-equiv="Content-Type" content="text/html; charset=%s">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n</head>\n\n<title>%s</title>\n\n<script>\nfunction request_reload()\n{\n    fetch(\'/?reload?\');\n}\n</script>\n\n\n\n\n<style type="text/css">\nbody{\n  position: relative;\n  min-height: 100vh;\n}\n\nhtml, body, input, textarea, select, button {\n    border-color: #736b5e;\n    color: #e8e6e3;\n    background-color: #181a1b;\n}\n* {\n    scrollbar-color: #0f0f0f #454a4d;\n}\na{\n  line-height: 200%%;\n  font-size: 20px;\n  font-weight: 600;\n  font-family: \'Gill Sans, Gill Sans MT, Calibri, Trebuchet MS, sans-serif\';\n  text-decoration: none;\n  color: #00BFFF;\n}\n\n.all_link{\nword-wrap: break-word;\n}\n\n.link{\n  color: #1589FF;\n  /* background-color: #1589FF; */\n}\n\n.vid{\n  color: #8A2BE2;\n  font-weight: 300;\n}\n\n.file{\n  font-weight: 300;\n  color: #c07cf7;\n  font-weight: 400;\n}\n\n\n#footer {\n  position: absolute;\n  bottom: 0;\n  width: 100%%;\n  height: 2.5rem;\t\t\t/* Footer height */\n}\n\n\n.overflowHidden {\n\toverflow: hidden !important\n}\n\n\n/* POPUP CSS */\n\n.modal_bg{\n  display: inherit;\n  position: fixed;\n  z-index: 1;\n  padding-top: inherit;\n  left: 0;\n  top: 0;\n  width: 100%%;\n  height: 100%%;\n  overflow: auto;\n}\n\n.popup{\n    position: fixed;\n    z-index: 99;\n    left: 50%%;\n    top: 50%%;\n    width: 100%%;\n    height: 100%%;\n    overflow: auto;\n    transition: all 300ms ease-in-out;\n    transform: translate(-50%%, -50%%) scale(1)\n}\n\n#popup-box {\n    display: block;\n    position: fixed;\n    top: 50%%;\n    left: 50%%;\n    color: #AAA;\n    transition: all 300ms ease-in-out;\n    background: #222;\n    width: 95%%;\n    max-width: 600px;\n    z-index: 1;\n    text-align: center;\n    padding: 10px;\n    box-sizing: border-box;\n    font-family: "Open Sans", sans-serif;\n    max-height: 800px;\n    height:max-content;\n    min-height: 400px;\n}\n\n#popup-content{\n\tmax-width:95%%;\n\toverflow: scroll;;\n}\n\n.popup-close-btn {\n    cursor: pointer;\n    position: absolute;\n    right: 20px;\n    top: 20px;\n    width: 30px;\n    height: 30px;\n    background: #222;\n    color: #fff;\n    font-size: 25px;\n    font-weight: 600;\n    line-height: 30px;\n    text-align: center;\n    border-radius: 50%%\n}\n\n.popup:not(.active){\n    transform: translate(-50%%, -50%%) scale(0);\n}\n\n\n.popup.active #popup-box{\n    transform: translate(-50%%, -50%%) scale(1);\n}\n\n\n\n.pagination {\n  cursor: pointer;\n    width: 150px;\n    max-width: 800px\n}\n\n.pagination {\n    font: bold 20px Arial;\n    text-decoration: none;\n    background-color: #8a8b8d6b;\n    color: #1f83b6;\n    padding: 2px 6px;\n    border-top: 1px solid #828d94;\n    box-shadow: 4px 4px #5050506b;\n    border-left: 1px solid #828D94;\n}\n\n.pagination:hover {\n    background-color:  #4e4f506b;\n    color: #00b7ff;\n    box-shadow: 4px 4px #8d8d8d6b;\n    border: none;\n    border-right: 1px solid #959fa5;\n    border-bottom: 1px solid #959fa5\n}\n\n.pagination:active {\n    margin-top: 4px;\n    margin-left: 4px;\n    box-shadow: none\n}\n\n\n</style>\n</head> \n<body>\n\n\n    \n<div class="popup", id="popup-0">\n    <div id="popup-bg" class="modal_bg" style="background-color:rgba(0, 0, 0, 0.7);" onclick="popup_msg.togglePopup()"></div>\n    <div id="popup-box">\n        <div class="popup-close-btn" onclick="popup_msg.togglePopup()">&times;</div>\n    \n        <h1 id="popup-header"></h1>\n        <hr width="95%%" id="popup-hr">  <!-- if needed -->\n        \n        <div id="popup-content"></div>\n    </div>\n</div>\n\n<h1 style="word-wrap: break-word;">%s</h1>\n<hr>\n\n\n'
AG='\n</ul>\n<hr>\n<div class=\'pagination\' onclick = "request_reload()">reload</div><br>\n\n<div class=\'pagination\' onclick = "Show_folder_maker()">Create Folder</div><br>\n\n<br><hr><br><h2>Upload file</h2>\n        <form ENCTYPE="multipart/form-data" method="post">\n        \n  <p>PassWord:&nbsp;&nbsp;</p><input name="txt" type="text" label="Password"><br>\n  <p>Load File:&nbsp;&nbsp;</p><input name="file" type="file" multiple/><br><br>\n\n  <input type="submit" value="⭱ upload" style="background-color: #555; height: 30px; width: 100px"></form>\n\n<hr>\n<script>\n\nconst r_li = %s;\nconst f_li = %s;\n\n\nfunction toggle_scroll() {\n    document.body.classList.toggle(\'overflowHidden\');\n}\n\nfunction go_link(typee, locate){\n  // function to generate link for different types of actions\n  return typee+"%%3F"+locate;}\n\n// getting all the links in the directory\n\nconst linkd_li = document.getElementsByTagName(\'ul\')[0];\n\nfor (let i = 0; i < r_li.length; i++) {\n  // time to customize the links according to their formats\n\n  let ele = document.createElement(\'li\');\n\tlet r= r_li[i];\n\tlet r_ = r.slice(1);\n\tlet name = f_li[i];\n\tlet link = document.createElement(\'a\');\n\tlink.href = r_;\n\tlink.classList.add(\'all_link\');\n\n\tif(r.startsWith(\'d\')){\n\t// add DOWNLOAD FOLDER OPTION in it\n\t// TODO: add download folder option by zipping it\n\t// currently only shows folder size and its contents\n\tlink.innerHTML = "📂" + name;\n\tlink.classList.add(\'link\');\n\n\tele.appendChild(link);\n\n\tlet dl = document.createElement(\'a\');\n\tdl.innerHTML= \'<span style="color: black; background-color: #40A4F7;"><b>〘↓〙</b></span>\';\n\tdl.href = go_link(\'dl\', r_);  // download folder link: parent/dl?folder_name\n\tdl.style.paddingLeft= \'50px\';\n\n\tele.insertAdjacentElement("beforeend",dl);\n\t}\n\n\tif(r.startsWith(\'v\')){\n\t// if its a video, add play button at the end\n\t// that will redirect to the video player\n\t// clicking main link will download the video instead\n\n\tlink.innerHTML = \'🎥\' + name;\n\tlink.classList.add(\'vid\');\n\tele.appendChild(link);\n\n\n\tlet play = document.createElement(\'A\');\n\tplay.innerHTML= \'<span style="color: black; background-color: #40A4F7;"><b>&nbsp▶&nbspPLAY&nbsp</b></span>\';\n\tplay.href = go_link(\'vid\', r_);  // video player link: parent/vid?video_name\n\tplay.style.paddingLeft= \'50px\';\n\n\tele.insertAdjacentElement("beforeend",play);\n\t}\n\n\tif(r.startsWith(\'f\')){\n\tlink.innerHTML = \'📄\' + name;\n\tlink.classList.add(\'file\');\n\tele.appendChild(link);\n\n\t}\n\tif(r.startsWith(\'h\')){\n\tlink.innerHTML = \'🔗\' + name;\n\tlink.classList.add(\'html\');\n\tele.appendChild(link);\n\n\t}\n\n\tif(true){\n\t\t// recycling option for the files and folder\n\t\t// files and folders are handled differently\n\n\t\tif(r.startsWith(\'d\')){\n\t\t\tvar xxx = "D";\n\t\t}\n\t\telse{\n\t\t\tvar xxx = "F";\n\t\t}\n\tconst del = document.createElement(\'a\');\n\tdel.innerHTML= \'<span style="color: black; background-color: #40A4F7;"><b> ♻&nbsp;</b></span>\';\n\tdel.onclick = run_recyle(go_link(\'recycle\' + xxx, r_)); // recycle link: parent/recycle*?file_or_folder_name\n    del.style.paddingLeft= \'50px\';\n\n\tele.insertAdjacentElement("beforeend",del);\n\t}\n\n\t\n  linkd_li.appendChild(ele);\n}\n\n\nclass Popup_Msg {\n  constructor() {\n\t  this.popup_obj = document.getElementById(\'popup-0\');\n\t  this.header = document.getElementById(\'popup-header\');\n\t  this.content = document.getElementById(\'popup-content\');\n\t  this.hr = document.getElementById(\'popup-hr\');\n  }\n\n  togglePopup(indx=0, on_or_off = null) {\n\t  this.popup_obj.classList.toggle("active");\n\t  toggle_scroll();\n  }\n\n  createPopup(header, content, hr=true) {\n\t\t\t\t   while (this.header.firstChild) {\n    this.header.removeChild(this.header.lastChild);\n  }\n  \t\t\t\twhile (this.content.firstChild) {\n    this.content.removeChild(this.content.lastChild);\n  }\n  \t\t\t\t\n\t\t\t\t  this.header.innerHTML = header;\n\t\t\t\t  this.content.innerHTML = content;\n\t\t\t\t  if(hr){\n\t\t\t\t\t  this.hr.style.display = "block";\n\t\t\t\t  }else{\n\t\t\t\t\t  this.hr.style.display = "none";\n\t\t\t\t  }\n\t\t\t  }\n}\n\n\nlet popup_msg = new Popup_Msg();\n\nfunction Show_folder_maker(){\n    popup_msg.createPopup("Create Folder", "Enter folder name: <input id=\'folder-name\' type=\'text\'><br><br><div class=\'pagination\' onclick=\'create_folder()\'>Create</div>");\n    popup_msg.togglePopup();\n}\n\nfunction show_response(url, add_reload_btn=true){\n  var xhr = new XMLHttpRequest();\n    xhr.onreadystatechange = function() {\n        if (xhr.readyState == XMLHttpRequest.DONE) {\n            let msg = xhr.responseText;\n\t\t\tif(add_reload_btn){\n\t\t\t\tmsg = msg + "<br><br><div class=\'pagination\' onclick=\'window.location.reload()\'>Reload🔄️</div>";\n\t\t\t}\n            popup_msg.createPopup("Result", msg);\n            popup_msg.togglePopup();\n        }\n    }\n    xhr.open(\'GET\', url , true);\n    xhr.send(null);\n}\n\nfunction create_folder(){\n    let folder_name = document.getElementById(\'folder-name\').value;\n    let folder_link = go_link(\'mkdir\', folder_name);\n\n    popup_msg.togglePopup();\n    show_response(folder_link);\n}\n\nfunction reload(){\n    show_response("?reload?");\n}\n\nfunction run_recyle(url){\n    return function(){\n        show_response(url);\n    }\n}\n\n</script>\n\n</body>\n</html>\n'
__version__='0.6'
__all__=['HTTPServer','ThreadingHTTPServer','BaseHTTPRequestHandler','SimpleHTTPRequestHandler','CGIHTTPRequestHandler']
import copy,datetime as p,email.utils,html as U,http.client,io as d,mimetypes as b,posixpath as g,select as s,shutil as o,socket as I,socketserver as S,sys as O,time as k,urllib.parse,contextlib as AH
from functools import partial
from subprocess import call
from http import HTTPStatus as D
import re
def AI(start_path=Z,limit=C,return_list=E,full_dir=M):
	H=limit;F=start_path;D=return_list
	if D:I=[]
	A=0;F=F[:-1]
	for (L,N,M) in B.walk(F,onerror=J):
		for K in M:
			G=B.path.join(L,K)
			if D:I.append(G if full_dir else K)
			if not B.path.islink(G):A+=B.path.getsize(G)
			if H!=C and A>H:
				J('counted upto',A)
				if D:return A7,E
				return A7
	if D:return A,I
	return A
def AJ(B):
	B=B;A=1024;D=A**2;E=A**3;F=A**4;C=L
	if B>=F:C+='%i TB  '%(B//F);B%=F
	if B>=E:C+='%i GB  '%(B//E);B%=E
	if B>=D:C+='%i MB  '%(B//D);B%=D
	if B>=A:C+='%i KB  '%(B//A);B%=A
	if B>0:C+='%i bytes'%B
	return C
def AK(infile,outfile,start=C,stop=C,bufsize=16*1024):
	D=bufsize;B=start;A=infile
	if B is not C:A.seek(B)
	while 1:
		F=min(D,stop+1-A.tell()if stop else D);E=A.read(F)
		if not E:break
		outfile.write(E)
AL=re.compile('bytes=(\\d+)-(\\d+)?$')
def AM(byte_range):
	F='Invalid byte range %s';A=byte_range
	if A.strip()==L:return C,C
	D=AL.match(A)
	if not D:raise X(F%A)
	E,B=[A and P(A)for A in D.groups()]
	if B and B<E:raise X(F%A)
	return E,B
AN='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n\t\t"http://www.w3.org/TR/html4/strict.dtd">\n<html>\n\t<head>\n\t\t<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n\t\t<title>Error response</title>\n\t</head>\n\t<body>\n\t\t<h1>Error response</h1>\n\t\t<p>Error code: %(code)d</p>\n\t\t<p>Message: %(message)s.</p>\n\t\t<p>Error code explanation: %(code)s - %(explain)s.</p>\n\t</body>\n</html>\n'
AO='text/html;charset=utf-8'
class HTTPServer(S.TCPServer):
	allow_reuse_address=1
	def server_bind(A):S.TCPServer.server_bind(A);B,C=A.server_address[:2];A.server_name=I.getfqdn(B);A.server_port=C
class ThreadingHTTPServer(S.ThreadingMixIn,HTTPServer):daemon_threads=M
class BaseHTTPRequestHandler(S.StreamRequestHandler):
	sys_version='Python/'+O.version.split()[0];server_version='BaseHTTP/'+__version__;error_message_format=AN;error_content_type=AO;default_request_version=m
	def parse_request(A):
		Q='HTTP/1.1';A.command=C;A.request_version=J=A.default_request_version;A.close_connection=M;K=H(A.raw_requestline,'iso-8859-1');K=K.rstrip('\r\n');A.requestline=K;B=K.split()
		if G(B)==0:return E
		if G(B)>=3:
			J=B[-1]
			try:
				if not J.startswith('HTTP/'):raise X
				R=J.split(F,1)[1];I=R.split(Z)
				if G(I)!=2:raise X
				I=P(I[0]),P(I[1])
			except (X,AW):A.send_error(D.BAD_REQUEST,'Bad request version (%r)'%J);return E
			if I>=(1,1)and A.protocol_version>=Q:A.close_connection=E
			if I>=(2,0):A.send_error(D.HTTP_VERSION_NOT_SUPPORTED,'Invalid HTTP version (%s)'%R);return E
			A.request_version=J
		if not 2<=G(B)<=3:A.send_error(D.BAD_REQUEST,'Bad request syntax (%r)'%K);return E
		N,T=B[:2]
		if G(B)==2:
			A.close_connection=M
			if N!='GET':A.send_error(D.BAD_REQUEST,'Bad HTTP/0.9 request type (%r)'%N);return E
		A.command,A.path=N,T
		try:A.headers=http.client.parse_headers(A.rfile,_class=A.MessageClass)
		except http.client.LineTooLong as O:A.send_error(D.REQUEST_HEADER_FIELDS_TOO_LARGE,'Line too long',H(O));return E
		except http.client.HTTPException as O:A.send_error(D.REQUEST_HEADER_FIELDS_TOO_LARGE,'Too many headers',H(O));return E
		S=A.headers.get(Ab,L)
		if S.lower()==v:A.close_connection=M
		elif S.lower()==Ac and A.protocol_version>=Q:A.close_connection=E
		U=A.headers.get('Expect',L)
		if U.lower()=='100-continue'and A.protocol_version>=Q and A.request_version>=Q:
			if not A.handle_expect_100():return E
		return M
	def handle_expect_100(A):A.send_response_only(D.CONTINUE);A.end_headers();return M
	def handle_one_request(A):
		try:
			A.raw_requestline=A.rfile.readline(65537)
			if G(A.raw_requestline)>65536:A.requestline=L;A.request_version=L;A.command=L;A.send_error(D.REQUEST_URI_TOO_LONG);return
			if not A.raw_requestline:A.close_connection=M;return
			if not A.parse_request():return
			B='do_'+A.command
			if not W(A,B):A.send_error(D.NOT_IMPLEMENTED,'Unsupported method (%r)'%A.command);return
			C=getattr(A,B);C();A.wfile.flush()
		except I.timeout as E:A.log_error('Request timed out: %r',E);A.close_connection=M;return
	def handle(A):
		A.close_connection=M;A.handle_one_request()
		while not A.close_connection:A.handle_one_request()
	def send_error(A,code,message=C,explain=C):
		N='???';J=explain;F=message;B=code
		try:K,L=A.responses[B]
		except AX:K,L=N,N
		if F is C:F=K
		if J is C:J=L
		A.log_error('code %d, message %s',B,F);A.send_response(B,F);A.send_header(Ab,v);I=C
		if B>=200 and B not in(D.NO_CONTENT,D.RESET_CONTENT,D.NOT_MODIFIED):M=A.error_message_format%{'code':B,'message':U.escape(F,quote=E),'explain':U.escape(J,quote=E)};I=M.encode('UTF-8','replace');A.send_header('Content-Type',A.error_content_type);A.send_header(V,H(G(I)))
		A.end_headers()
		if A.command!='HEAD'and I:A.wfile.write(I)
	def send_response(A,code,message=C):A.log_request(code);A.send_response_only(code,message);A.send_header('Server',A.version_string());A.send_header('Date',A.date_time_string())
	def send_response_only(A,code,message=C):
		D=code;B=message
		if A.request_version!=m:
			if B is C:
				if D in A.responses:B=A.responses[D][0]
				else:B=L
			if not W(A,w):A._headers_buffer=[]
			A._headers_buffer.append(('%s %d %s\r\n'%(A.protocol_version,D,B)).encode(Ad,Ae))
	def send_header(A,keyword,value):
		C=keyword;B=value
		if A.request_version!=m:
			if not W(A,w):A._headers_buffer=[]
			A._headers_buffer.append(('%s: %s\r\n'%(C,B)).encode(Ad,Ae))
		if C.lower()=='connection':
			if B.lower()==v:A.close_connection=M
			elif B.lower()==Ac:A.close_connection=E
	def end_headers(A):
		if A.request_version!=m:A._headers_buffer.append(Af);A.flush_headers()
	def flush_headers(A):
		if W(A,w):A.wfile.write(b''.join(A._headers_buffer));A._headers_buffer=[]
	def log_request(B,code='-',size='-'):
		A=code
		if isinstance(A,D):A=A.value
		B.log_message('"%s" %s %s',B.requestline,H(A),H(size))
	def log_error(A,format,*B):A.log_message(format,*B)
	def log_message(A,format,*B):
		D='%s - - [%s] %s\n';O.stderr.write(D%(A.address_string(),A.log_date_time_string(),format%B))
		with A4(R+'log.txt','a+')as C:C.write('\n\n'+D%(A.address_string(),A.log_date_time_string(),format%B))
	def version_string(A):return A.server_version+' '+A.sys_version
	def date_time_string(B,timestamp=C):
		A=timestamp
		if A is C:A=k.time()
		return email.utils.formatdate(A,usegmt=M)
	def log_date_time_string(A):B=k.time();C,D,E,F,G,H,J,K,L=k.localtime(B);I='%02d/%3s/%04d %02d:%02d:%02d'%(E,A.monthname[D],C,F,G,H);return I
	weekdayname=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];monthname=[C,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	def address_string(A):return A.client_address[0]
	protocol_version=Ag;MessageClass=http.client.HTTPMessage;responses={A:(A.phrase,A.description)for A in D.__members__.values()}
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	server_version='SimpleHTTP/'+__version__
	def __init__(D,*E,directory=C,**F):
		A=directory
		if A is C:A=B.getcwd()
		D.directory=A;super().__init__(*E,**F)
	def do_GET(A):
		B=A.send_head()
		if B:
			try:A.copyfile(B,A.wfile)
			finally:B.close()
	def do_HEAD(B):
		A=B.send_head()
		if A:A.close()
	def do_POST(B):
		B.range=C;D,E=B.deal_post_data();J((D,E,'by: ',B.client_address));A=d.BytesIO();A.write(b'<!DOCTYPE html>');A.write(b'<html>\n<title>Upload Result Page</title>\n');A.write(b'<body>\n<h2>Upload Result Page</h2>\n');A.write(b'<hr>\n')
		if D:A.write(b'<strong>Success:</strong>')
		else:A.write(b'<strong>Failed:</strong>')
		A.write(E.encode());A.write(('<br><a href="%s">back</a>'%B.headers[Ah]).encode());A.write(b'<hr><small>Powerd By: bones7456');F=A.tell();A.seek(0);B.send_response(200);B.send_header(Y,'text/html');B.send_header(V,H(F));B.end_headers()
		if A:B.copyfile(A,B.wfile);A.close()
	def deal_post_data(C):
		R='Content NOT begin with boundary';N=[];O=C.headers[x]
		if not O:return E,"Content-Type header doesn't contain boundary"
		I=O.split(z)[1].encode();D=P(C.headers[Ai]);A=C.rfile.readline();D-=G(A)
		if not I in A:return E,R
		A=C.rfile.readline();D-=G(A);A=C.rfile.readline();D-=G(A);K=C.rfile.readline();J('post password: ',K)
		if K!=A9+Af:return E,'Incorrect password'
		D-=G(K);A=C.rfile.readline();D-=G(A)
		if not I in A:return E,R
		while D>0:
			A=C.rfile.readline();D-=G(A);H=re.findall('Content-Disposition.*name="file"; filename="(.*)"',A.decode())
			if not H:return E,"Can't find out file name..."
			Q=C.translate_path(C.path);H=B.path.join(Q,H[0]);A=C.rfile.readline();D-=G(A);A=C.rfile.readline();D-=G(A)
			try:L=A4(H,'wb')
			except IOError:return E,"Can't create file to write, do you have permission to write?"
			else:
				with L:
					F=C.rfile.readline();D-=G(F)
					while D>0:
						A=C.rfile.readline();D-=G(A)
						if I in A:
							F=F[0:-1]
							if F.endswith(b'\r'):F=F[0:-1]
							L.write(F);N.append(H);break
						else:L.write(F);F=A
		return M,"File '%s' upload success!"%','.join(N)
	def send_head(A):
		AR='If-Modified-Since';AQ='vid%3F';AP=':\\';AO='</h1>';AN='==================== current path';AL=' : ';AK='</h1><br>';AH='Range';i='.zip';global j,T,c
		if AH not in A.headers:A.range=C;s,g=0,0
		else:
			try:A.range=AM(A.headers[AH]);s,g=A.range
			except X as Z:A.send_error(400,'Invalid byte range');return C
		I=A.translate_path(A.path);S=B.path.split(A.path);N=B.path.split(I);P=A.path.split(F);a=C;J('path',I,'\nself.path',A.path,'\nspathtemp',S,'\npathtemp',N,'\nspathsplit',P)
		if P[-1]=='?reload?':j=M;l.server_close();l.shutdown()
		elif N[-1].startswith('mkdir?'):
			J(N)
			try:B.mkdir(B.path.join(N[0],N[1][6:]));b='Directory created!'
			except A5 as Z:b='Failed To Create folder '+N[1][6:]+AK+Z.__class__.__name__+AL+H(Z)
			R=b.encode(e,q);K=d.BytesIO();K.write(R);K.seek(0);A.send_response(D.OK);A.send_header(Y,r%e);A.send_header(V,H(G(R)));A.end_headers();return K
		elif P[-2].startswith('recycleD%3F')or P[-1].startswith('recycleF%3F'):
			J(AN,I);Q=I.replace('recycleD?',L,1).replace('recycleF?',L,1)
			if Q.endswith((F,'\\')):J(Q);Q=Q[:-1]
			J('Recycling',Q);b='<!doctype HTML><h1>Recycled successfully  '+Q+AO
			try:
				try:AE(Q)
				except AF:
					if B.path.isfile(Q):B.remove(Q)
					else:o.rmtree(Q)
					b=b='<!doctype HTML><h1>Recycling unavailable. FORCE DELETING  '+Q+AO
			except A5 as Z:J(Z);b='<!doctype HTML><h1>Recycling failed  '+Q+AK+Z.__class__.__name__+AL+H(Z)
			R=b.encode(e,q);K=d.BytesIO();K.write(R);K.seek(0);A.send_response(D.OK);A.send_header(Y,r%e);A.send_header(V,H(G(R)));A.end_headers();return K
		elif P[-1].startswith('dlY%3F'):
			a=N[-1][4:-29];id=N[1][-24:];m=y;J(T);J(id in T.keys());J(id in c)
			if id in T.keys():I=m+F+id+i;a=T[id]+i
			elif id in c:
				while id in c:k.sleep(1)
				I=m+F+id+i;a=T[id]+i
			else:c.append(id);J(AN,H(m));call(['7z/7za','a','-mx=0',H(m)+F+id+i,N[0]+'\\'+N[-1][4:-29]]);c.remove(id);T[id]=a;I=m+F+id+i;a=T[id]+i
		elif A.path.endswith(F)and P[-2].startswith('dl%3F'):
			I=A.translate_path(F.join(P[:-2])+F+P[-2][5:]+F)
			if not B.path.isdir(I):A9='<!DOCTYPE HTML><h1>Directory not found</h1>'
			else:J('init');z,W=AI(I,8*1024*1024*1024,M);id=L.join((random.choice(A2.ascii_uppercase+A2.digits)for A in range(6)))+'_'+H(k.time());id+='0'*(24-G(id));AB=z==A7;J('Directory size: '+H(z));A9='<!DOCTYPE HTML><h1>The folder size is too big</h1>\t\t\t\t\t'if AB else'"<!DOCTYPE HTML><h1> Download will start shortly</h1>\n\t\t\t\t\t<pre style=\'font-size:20px; font-weight: 600;\'><b>Directory size:</b> '+AJ(z)+'</pre>\n\t\t\t\t\t<br><br>The directory has:\n<hr>'+(A8.join(['<u>'+A+'</u><br>'for A in W])+'\n\t\t\t\t\t<script>window.location.href="../dlY%3F'+P[-2][5:]+'%3Fid='+id+'";</script>')
			R=A9.encode(e,q);K=d.BytesIO();K.write(R);K.seek(0);A.send_response(D.OK);A.send_header(Y,r%e);A.send_header(V,H(G(R)));A.end_headers();return K
		elif S[0].startswith('/drive%3E'):
			if B.path.isdir(S[0][9:]+AP):
				A.path=S[0][9]+AP;A.directory=A.path
				try:A.path+=S[0][10:]
				except:pass
				A.path=S[1];I=A.translate_path(A.path);S=B.path.split(A.path);N=B.path.split(I)
		elif P[-1].startswith(AQ)or B.path.exists(I):
			if P[-1].startswith(AQ)and A.guess_type(B.path.join(N[0],P[-1][6:])).startswith(Aj):
				A.path=S[0]+F+S[1][6:];I=B.path.join(N[0],N[1][4:]);W=[]
				try:t=urllib.parse.unquote(A.path,errors=f)
				except A6:t=urllib.parse.unquote(I)
				t=U.escape(t,quote=E);A0=O.getfilesystemencoding();AA=Ak%t;W.append(A3%(A0,AA,AA))
				if A.guess_type(B.path.join(N[0],P[-1][6:]))not in['video/mp4','video/ogg','video/webm']:W.append("<h2>It seems HTML player can't play this Video format, Try Downloading</h2>")
				else:u=A.guess_type(B.path.join(N[0],P[-1][6:]));W.append('\n<!-- stolen from http://plyr.io -->\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/RaSan147/httpserver_with_many_feat@main/video.css" />\n\n<link rel="preload" as="font" crossorigin type="font/woff2" href="https://cdn.plyr.io/static/fonts/gordita-medium.woff2" />\n<link rel="preload" as="font" crossorigin type="font/woff2" href="https://cdn.plyr.io/static/fonts/gordita-bold.woff2" />\n\n<div id="container">\n\t<video controls crossorigin playsinline data-poster="https://i.imgur.com/jQZ5DoV.jpg" id="player">\n\t\n\t<source src="%s" type="%s"/>\n\t<a href="%s" download>Download</a>\n\t</video>\n\n\t\n<script src="https://cdn.plyr.io/3.6.9/demo.js" crossorigin="anonymous"></script>\n\t</div><br>'%(A.path,u,A.path))
				W.append('<br><a href="%s"><div class=\'pagination\'>Download</div></a></li>'%A.path);W.append('\n<hr>\n</body>\n</html>\n');R=A8.join(W).encode(A0,q);K=d.BytesIO();K.write(R);K.seek(0);A.send_response(D.OK);A.send_header(Y,r%A0);A.send_header(V,H(G(R)));A.end_headers();return K
		K=C
		if B.path.isdir(I):
			h=urllib.parse.urlsplit(A.path)
			if not h.path.endswith(F):A.send_response(D.MOVED_PERMANENTLY);AC=h[0],h[1],h[2]+F,h[3],h[4];AD=urllib.parse.urlunsplit(AC);A.send_header('Location',AD);A.end_headers();return C
			for v in ('index.html','index.htm'):
				v=B.path.join(I,v)
				if B.path.exists(v):I=v;break
			else:return A.list_directory(I)
		if I.endswith(F):A.send_error(D.NOT_FOUND,'File not found');return C
		else:
			u=A.guess_type(I);K=A4(I,'rb')
			try:
				w=B.fstat(K.fileno());x=w[6]
				if A.range and s>=x:A.send_error(416,'Requested Range Not Satisfiable');return C
				if AR in A.headers and'If-None-Match'not in A.headers:
					try:n=email.utils.parsedate_to_datetime(A.headers[AR])
					except (AY,AW,OverflowError,X):pass
					else:
						if n.tzinfo is C:n=n.replace(tzinfo=p.timezone.utc)
						if n.tzinfo is p.timezone.utc:
							A1=p.datetime.fromtimestamp(w.st_mtime,p.timezone.utc);A1=A1.replace(microsecond=0)
							if A1<=n:A.send_response(D.NOT_MODIFIED);A.end_headers();K.close();return C
				if A.range:
					A.send_response(206);A.send_header(Y,u);A.send_header('Accept-Ranges','bytes')
					if g is C or g>=x:g=x-1
					AG=g-s+1;A.send_header('Content-Range','bytes %s-%s/%s'%(s,g,x));A.send_header(V,H(AG))
				else:A.send_response(D.OK);A.send_header(Y,u);A.send_header(V,H(w[6]))
				A.send_header('Last-Modified',A.date_time_string(w.st_mtime));A.send_header('Content-Disposition','filename="%s"'%(B.path.basename(I)if a is C else a));A.end_headers();return K
			except:K.close();raise
	def list_directory(A,path):
		R=path
		try:list=B.listdir(R)
		except u:A.send_error(D.NOT_FOUND,'No permission to list directory');return C
		list.sort(key=lambda a:a.lower());K=[]
		try:Q=urllib.parse.unquote(A.path,errors=f)
		except A6:Q=urllib.parse.unquote(R)
		Q=U.escape(Q,quote=E);S=O.getfilesystemencoding();X=Ak%Q;K.append(A3%(S,X,X));K.append('<hr>\n<ul id= "linkss">');L=[];N=[]
		for P in list:
			T=B.path.join(R,P);I=J=P;Z=M
			if B.path.isdir(T):I=P+F;J=P+F
			elif B.path.islink(T):I=P+'@'
			else:
				Z=E;__,b=g.splitext(T)
				if b=='.html':L.append('h'+urllib.parse.quote(J,errors=f));N.append(U.escape(I,quote=E))
				elif A.guess_type(J).startswith(Aj):L.append('v'+urllib.parse.quote(J,errors=f));N.append(U.escape(I,quote=E))
				else:L.append('f'+urllib.parse.quote(J,errors=f));N.append(U.escape(I,quote=E))
			if Z:L.append('d'+urllib.parse.quote(J,errors=f));N.append(U.escape(I,quote=E))
			K
		K.append(AG%(H(L),H(N)));a=A8.join(K).encode(S,q);W=d.BytesIO();W.write(a);W.seek(0);A.send_response(D.OK);A.send_header(Y,r%S);A.send_header(V,H(G(a)));A.end_headers();return W
	def translate_path(G,path):
		A=path;A=A.split(a,1)[0];A=A.split('#',1)[0];H=A.rstrip().endswith(F)
		try:A=urllib.parse.unquote(A,errors=f)
		except A6:A=urllib.parse.unquote(A)
		A=g.normpath(A);D=A.split(F);D=AZ(C,D);A=G.directory
		for E in D:
			if B.path.dirname(E)or E in(B.curdir,B.pardir):continue
			A=B.path.join(A,E)
		if H:A+=F
		return A
	def copyfile(C,source,outputfile):
		D=outputfile;A=source
		if not C.range:
			A.read(1);A.seek(0)
			try:o.copyfileobj(A,D)
			except Aa as B:J(B)
		else:
			E,F=C.range
			try:AK(A,D,E,F)
			except Aa as B:J(B)
	def guess_type(B,path):
		C,A=g.splitext(path)
		if A in B.extensions_map:return B.extensions_map[A]
		A=A.lower()
		if A in B.extensions_map:return B.extensions_map[A]
		else:return B.extensions_map[L]
	if not b.inited:b.init()
	extensions_map=b.types_map.copy();extensions_map.update({L:'application/octet-stream',Al:A0,'.c':A0,'.h':A0})
def AP(path):
	J='..';B=path;B,K,G=B.partition(a);B=urllib.parse.unquote(B);E=B.split(F);C=[]
	for D in E[:-1]:
		if D==J:C.pop()
		elif D and D!=Z:C.append(D)
	if E:
		A=E.pop()
		if A:
			if A==J:C.pop();A=L
			elif A==Z:A=L
	else:A=L
	if G:A=a.join((A,G))
	H=F+F.join(C),A;I=F.join(H);return I
K=C
def AQ():
	global K
	if K:return K
	try:import pwd
	except ImportError:return-1
	try:K=pwd.getpwnam('nobody')[2]
	except AX:K=1+max((A[2]for A in pwd.getpwall()))
	return K
def AR(path):return B.access(path,B.X_OK)
class CGIHTTPRequestHandler(SimpleHTTPRequestHandler):
	have_fork=W(B,'fork');rbufsize=0
	def do_POST(A):
		if A.is_cgi():A.run_cgi()
		else:A.send_error(D.NOT_IMPLEMENTED,'Can only POST to CGI scripts')
	def send_head(A):
		if A.is_cgi():return A.run_cgi()
		else:return SimpleHTTPRequestHandler.send_head(A)
	def is_cgi(A):
		B=AP(A.path);C=B.find(F,1);D,G=B[:C],B[C+1:]
		if D in A.cgi_directories:A.cgi_info=D,G;return M
		return E
	cgi_directories=['/cgi-bin','/htbin']
	def is_executable(A,path):return AR(path)
	def is_python(C,path):D,A=B.path.splitext(path);return A.lower()in(Al,'.pyw')
	def run_cgi(A):
		A9='CGI script exit status %#x';A8='HTTP_COOKIE';A7='HTTP_USER_AGENT';A6='HTTP_REFERER';A5='CONTENT_LENGTH';A4='CONTENT_TYPE';A3='ascii';A2='QUERY_STRING';dir,J=A.cgi_info;U=dir+F+J;K=U.find(F,G(dir)+1)
		while K>=0:
			e=U[:K];p=U[K+1:];q=A.translate_path(e)
			if B.path.isdir(q):dir,J=e,p;K=U.find(F,G(dir)+1)
			else:break
		J,_,Q=J.partition(a);K=J.find(F)
		if K>=0:Y,J=J[:K],J[K:]
		else:Y,J=J,L
		M=dir+F+Y;N=A.translate_path(M)
		if not B.path.exists(N):A.send_error(D.NOT_FOUND,'No such CGI script (%r)'%M);return
		if not B.path.isfile(N):A.send_error(D.FORBIDDEN,'CGI script is not a plain file (%r)'%M);return
		r=A.is_python(M)
		if A.have_fork or not r:
			if not A.is_executable(N):A.send_error(D.FORBIDDEN,'CGI script is not executable (%r)'%M);return
		E=copy.deepcopy(B.environ);E['SERVER_SOFTWARE']=A.version_string();E['SERVER_NAME']=A.server.server_name;E['GATEWAY_INTERFACE']='CGI/1.1';E['SERVER_PROTOCOL']=A.protocol_version;E['SERVER_PORT']=H(A.server.server_port);E['REQUEST_METHOD']=A.command;f=urllib.parse.unquote(J);E['PATH_INFO']=f;E['PATH_TRANSLATED']=A.translate_path(f);E['SCRIPT_NAME']=M
		if Q:E[A2]=Q
		E['REMOTE_ADDR']=A.client_address[0];I=A.headers.get('authorization')
		if I:
			I=I.split()
			if G(I)==2:
				import base64 as t,binascii as v;E['AUTH_TYPE']=I[0]
				if I[0].lower()=='basic':
					try:I=I[1].encode(A3);I=t.decodebytes(I).decode(A3)
					except (v.Error,UnicodeError):pass
					else:
						I=I.split(':')
						if G(I)==2:E['REMOTE_USER']=I[0]
		if A.headers.get(x)is C:E[A4]=A.headers.get_content_type()
		else:E[A4]=A.headers[x]
		Z=A.headers.get(Ai)
		if Z:E[A5]=Z
		g=A.headers.get(Ah)
		if g:E[A6]=g
		V=[]
		for b in A.headers.getallmatchingheaders('accept'):
			if b[:1]in'\t\n\r ':V.append(b.strip())
			else:V=V+b[7:].split(',')
		E['HTTP_ACCEPT']=','.join(V);h=A.headers.get('user-agent')
		if h:E[A7]=h
		w=AZ(C,A.headers.get_all('cookie',[]));i=', '.join(w)
		if i:E[A8]=i
		for y in (A2,'REMOTE_HOST',A5,A7,A8,A6):E.setdefault(y,L)
		A.send_response(D.OK,'Script output follows');A.flush_headers();j=Q.replace('+',' ')
		if A.have_fork:
			k=[Y]
			if z not in j:k.append(j)
			A0=AQ();A.wfile.flush();c=B.fork()
			if c!=0:
				c,l=B.waitpid(c,0)
				while s.select([A.rfile],[],[],0)[0]:
					if not A.rfile.read(1):break
				if l:A.log_error(A9,l)
				return
			try:
				try:B.setuid(A0)
				except u:pass
				B.dup2(A.rfile.fileno(),0);B.dup2(A.wfile.fileno(),1);B.execve(N,k,E)
			except:A.server.handle_error(A.request,A.client_address);B._exit(127)
		else:
			import subprocess as R;S=[N]
			if A.is_python(N):
				T=O.executable
				if T.lower().endswith('w.exe'):T=T[:-5]+T[-4:]
				S=[T,'-u']+S
			if z not in Q:S.append(Q)
			A.log_message('command: %s',R.list2cmdline(S))
			try:d=P(Z)
			except (AY,X):d=0
			W=R.Popen(S,stdin=R.PIPE,stdout=R.PIPE,stderr=R.PIPE,env=E)
			if A.command.lower()=='post'and d>0:m=A.rfile.read(d)
			else:m=C
			while s.select([A.rfile._sock],[],[],0)[0]:
				if not A.rfile._sock.recv(1):break
			A1,n=W.communicate(m);A.wfile.write(A1)
			if n:A.log_error('%s',n)
			W.stderr.close();W.stdout.close();o=W.returncode
			if o:A.log_error(A9,o)
			else:A.log_message('CGI script exited OK')
def AS(*A):B=I.getaddrinfo(*A,type=I.SOCK_STREAM,flags=I.AI_PASSIVE);C,type,E,F,D=next(iter(B));return C,D
def t(HandlerClass=BaseHTTPRequestHandler,ServerClass=ThreadingHTTPServer,protocol=Ag,port=8000,bind=C):
	F=ServerClass;E=HandlerClass;D=bind;A=port;global l
	if O.version_info>(3,7,2):F.address_family,G=AS(D,A)
	else:G=D if D!=C else L,A
	E.protocol_version=protocol;l=F(G,E);B,A=l.socket.getsockname()[:2];H=f"[{B}]"if':'in B else B;K=I.gethostname();M=I.gethostbyname(K);J(f"Serving HTTP on {B} port {A} \n(http://{H}:{A}/) ...\nServer is probably running on {M}:{A}")
	try:l.serve_forever()
	except KeyboardInterrupt:
		J('\nKeyboard interrupt received, exiting.')
		if not j:O.exit(0)
	except u:
		J('\nOSError received, exiting.')
		if not j:O.exit(0)
class AT(ThreadingHTTPServer):
	def server_bind(A):
		with AH.suppress(A5):A.socket.setsockopt(I.IPPROTO_IPV6,I.IPV6_V6ONLY,0)
		return super().server_bind()
import pathlib as h
J(h.Path(__file__))
if __name__=='__main__':
	import argparse as AU;N=AU.ArgumentParser();N.add_argument('--cgi',action='store_true',help='Run as CGI Server');N.add_argument('--bind','-b',metavar='ADDRESS',help='Specify alternate bind address [default: all interfaces]');N.add_argument('--directory','-d',default=Q,help='Specify alternative directory [default:current directory]');N.add_argument('port',action='store',default=A1,type=P,nargs=a,help='Specify alternate port [default: 8000]');A=N.parse_args()
	if A.directory==Q and not B.path.isdir(Q):J(Q,'not found!\nReseting directory to current directory');A.directory=Z
	if A.cgi:i=CGIHTTPRequestHandler
	else:i=partial(SimpleHTTPRequestHandler,directory=A.directory)
	if O.version_info>(3,7,2):t(HandlerClass=i,ServerClass=AT,port=A.port,bind=A.bind)
	else:t(HandlerClass=i,ServerClass=ThreadingHTTPServer,port=A.port,bind=A.bind)
if j==M:import pathlib as h;AV=H(h.Path(__file__));call([O.executable,AV,*O.argv[1:]]);O.exit(0)
