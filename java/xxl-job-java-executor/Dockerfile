FROM openjdk:21-jdk-slim
# FROM openjdk:8-jre-slim
LABEL maintainer="xuxueli"

ENV TZ=PRC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY application.properties /application.properties

ADD xxl-job-executor-sample-springboot-3.3.0-SNAPSHOT.jar /app.jar

EXPOSE 9998

ENTRYPOINT ["sh", "-c", "java -jar $JAVA_OPTS /app.jar --spring.config.location=application.properties"]

