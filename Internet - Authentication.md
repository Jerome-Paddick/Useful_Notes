AUTHENTICATION
===

- HTTP is a stateless protocol -> each request is self contained -> must maintain authorization in each request
- for persistent session, must use tokens
- if stored in cookie, authentication-id will be sent with each request in `cookie` header
- Because of mulitple servers serving website, needs sessions to be sticky to specific server or shared session cache server

---
 ### JWT 

    JSON WEB TOKEN
    
- VALUE TOKEN
- Signed Json payload returned to user after each request
- JWT acts as signed session certificate
- Server only needs to authenticate payload -> does'nt need to persist sessions
- Structure, base 64 encoded string, split by dots `.`
    1. Header - `{"type":"JWT", "alg":"HS256"}`
    2. Payload - `{"id":"1234", "name":"asdf", "ist":"1234"}`
    3. Signature - `secret which validates agaist modifications`
    
- [Testing](https://jwt.io/)
- `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9  .eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9  .TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ`

---
### Classic Token

- REFERENCE TOKEN
- stores reference to session on the server (and authentication) in cookies
