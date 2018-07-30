# Spring-Cloud
This is Spring cloud modules verification workspace
all modules have been created for creating prototypes
Author: Leo Tao
Email: taoxb@163.com


8), Spring Cloud Bus
Need to add management.endpoints.web.exposure.include=bus-refresh in bootstrap.properties as it aboveSpring 2.0 which is using actuator expose web service.
POST config refresh request: curl -v -X POST "http://localhost:8771/actuator/bus-refresh"

