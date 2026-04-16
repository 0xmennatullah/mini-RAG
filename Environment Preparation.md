## Notes
- MUST HAVE at least gitignore + licence t begin with
- always leave an empty last line
- never in req. file leave a tool wo its version
- boiler plate => القالب الاساسي للمشروع بتاعي
- can use postman t monitor my APIs
## Explenations
### Requirements
- leaving req wo version => unprofessional
- versions master => pypi

### Configurations
- stored in system vars
- public config
- private config => .env بيكون برايفت علشان فيه secret keys ومينفعش حد ياخدها
- بنعرف اليوزر ايه مفروض يعمله عن طريق فايل تاني .env example
### API config
- can use postman t monitor all API access/tests; run collections instead of uvicorn/fastapi?
- if i want anyone t access the app => --host 0.0.0.0 + can specify the port as well
- 