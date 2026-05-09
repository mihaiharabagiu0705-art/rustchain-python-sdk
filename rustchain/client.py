import httpx
class RustChainClient:
      def __init__(self, base_url='http://localhost:8080'): self.base_url = base_url.rstrip('/')
            def get_status(self): return httpx.get(f'{self.base_url}/status').json()
                  def get_balance(self, addr): return httpx.get(f'{self.base_url}/balance/{addr}').json()
