Internet Requests
===

### CORS

    Cross-Origin Resource Sharing

- uses HTTP headers to give web application (running at 1 origin), access to selected resources from a different origin  
- Browsers restrict cross-origin HTTP requests from scripts, if resource does not explicitly allow resource to be shared with header `"Access-Control-Allow-Origin"`
- eg. frontend JS from `domain-a` asks uses Resource XMLHttpRequest to request `domain-b/data.json`, access is disallowed unless `domain-b` has an access header

---

### CORS Preflight Request

Happens when you try to send a complex request   
eg `{"Content-Type":"json/application"}`

    OPTIONS REQUEST
    
Browser will query server for headers returned via OPTIONS Request, and will allow access if correct headers returned

Needs 3 HTTP headers to be returned:
1. Access-Control-Request-Method
2. Access-Control-Request-Headers (for specific request eg.`Content-Type`)
3. Origin header 

---


