import base64,hashlib,json,os,time,urllib.request,zipfile,subprocess,secrets
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
root=Path(os.environ['RUNNER_TEMP'])
repo=os.environ['GITHUB_REPOSITORY']
run=os.environ['GITHUB_RUN_ID']
context=b'OPENPOS-4.6.1'
private=rsa.generate_private_key(public_exponent=65537,key_size=2048)
public=private.public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo).decode()
info={'run_id':run,'public_key':public}
payload={'message':'Public one-time encryption key for authorized installer publication','content':base64.b64encode(json.dumps(info).encode()).decode()}
keyfile=root/'public-key-request.json';keyfile.write_text(json.dumps(payload))
existing=subprocess.run(['gh','api','repos/'+repo+'/contents/publication/handoff-public.json'],capture_output=True,text=True)
if existing.returncode==0:payload['sha']=json.loads(existing.stdout)['sha'];keyfile.write_text(json.dumps(payload))
subprocess.run(['gh','api','--method','PUT','repos/'+repo+'/contents/publication/handoff-public.json','--input',str(keyfile)],check=True,stdout=subprocess.DEVNULL)
sealed_path='publication/sealed-'+run+'.json'
print('Clave publica de transferencia preparada. Esperando archivo cifrado.',flush=True)
sealed=None
for _ in range(90):
    result=subprocess.run(['gh','api','repos/'+repo+'/contents/'+sealed_path],capture_output=True,text=True)
    if result.returncode==0:
        sealed=json.loads(base64.b64decode(json.loads(result.stdout)['content']))
        break
    time.sleep(3)
if not sealed:raise SystemExit('La transferencia cifrada no llego a tiempo.')
decode=lambda s:base64.b64decode(s)
key=private.decrypt(decode(sealed['key']),padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=context))
request=json.loads(AESGCM(key).decrypt(decode(sealed['nonce']),decode(sealed['ciphertext']),context))
assert request['run_id']==run
from urllib.parse import urlparse
parsed=urlparse(request['download_url'])
assert parsed.scheme=='https' and parsed.hostname.endswith('.oaiusercontent.com') and not parsed.username and not parsed.password
archive_path=root/'installer.zip'
try:
    with urllib.request.urlopen(request['download_url'],timeout=120) as response,archive_path.open('wb') as target:
        import shutil
        shutil.copyfileobj(response,target)
except Exception:raise SystemExit('No se pudo descargar el instalador autorizado.') from None
out=Path('release-files');out.mkdir(exist_ok=True)
with zipfile.ZipFile(archive_path) as archive:
    assert archive.namelist()==['OpenPOS-Setup-4.6.1.exe']
    raw=archive.read('OpenPOS-Setup-4.6.1.exe')
expected='8b934f7e467c9621cacb11bb1cbc9286318124539badf0f769101e8dc51462de'
assert len(raw)==61439386 and hashlib.sha256(raw).hexdigest()==expected
token=request['manifest'].strip()
body,signature=token.split('.')
unb64=lambda s:base64.urlsafe_b64decode(s+'='*((-len(s))%4))
data=json.loads(unb64(body))
assert data=={'product':'OPENPOS_INSTALLER','platform':'windows-x64','version':'4.6.1','filename':'OpenPOS-Setup-4.6.1.exe','size':len(raw),'sha256':expected}
public=request['public_key'];n=int(public['n'],16);e=int(public['e']);width=(n.bit_length()+7)//8
digest=bytes.fromhex('3031300d060960864801650304020105000420')+hashlib.sha256(unb64(body)).digest()
assert pow(int.from_bytes(unb64(signature),'big'),e,n).to_bytes(width,'big')==b'\x00\x01'+b'\xff'*(width-len(digest)-3)+b'\x00'+digest
(out/data['filename']).write_bytes(raw)
(out/'installer-manifest.txt').write_text(token)
(out/'SHA256SUMS.txt').write_text(expected+'  '+data['filename']+'\n')
Path('release-notes.md').write_text('OpenPOS 4.6.1 incluye PostgreSQL 18.6 y lo configura automaticamente.\n\nCierre OpenPOS y ejecute OpenPOS-Setup-4.6.1.exe. Se conserva una copia previa y se verifica la migracion de datos. No hace falta descargar PostgreSQL ni crear bases o claves manualmente.\n\nInstalacion nueva, migracion, reinstalacion y desinstalacion conservando datos comprobadas en Windows. Firma RSA y SHA256 verificados.\n\nKTEL - +593 978 796 312 - https://wa.me/593978796312 (por accion del usuario).\n',encoding='utf-8')
print('Instalador y firma verificados.',flush=True)
