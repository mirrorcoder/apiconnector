ApiConnector

Project needs for joining different API's.


Current List Tasks:
  *Intro*
 - Config unittests
 - Add checking pylint
 - Add login for Account

   *Scheme*
 - Auth methods
    a. No auth
    b. Secret Key auth
    c. Pre-auth method through credentionals
 - Add CRUD-endpoints for Scheme's
   a. POST /api/scheme
   b. GET /api/scheme
   c. GET /api/scheme/<scheme_id>
   d. PUT /api/scheme/<scheme_id>
   e. DELETE /api/scheme/<scheme_id>
 - Add mongodb-model Scheme
 - Add endpoint for execute method in scheme
   a. GET/POST/PUT/DELETE /method/scheme/<scheme_id>/method/<name_method>

   *Adv scheme*
 - Add grouping scheme's for one method. Scheme of scheme's

   *CI/CD*
 - Config CI/CD

   *SWAGGER*
 - Add swagger
 - Add auto-generate swagger for every project

   *Queue messages*
   *RPC*

Release v0.0.1
 - Add Flask-Server. Base.
 - Config Logger
 - Add scheme for HTTP-client
 - Add deep-apply params by pattern
 - Processing json-answer
 - Logger