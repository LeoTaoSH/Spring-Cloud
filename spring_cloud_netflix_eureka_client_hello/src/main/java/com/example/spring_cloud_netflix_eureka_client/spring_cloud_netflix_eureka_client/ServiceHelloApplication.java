package com.example.spring_cloud_netflix_eureka_client.spring_cloud_netflix_eureka_client;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.cloud.netflix.hystrix.dashboard.EnableHystrixDashboard;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.netflix.hystrix.contrib.javanica.annotation.HystrixCommand;

@SpringBootApplication
@EnableEurekaClient
@RestController
@EnableHystrixDashboard
@EnableCircuitBreaker
public class ServiceHelloApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServiceHelloApplication.class, args);
    }

    @Value("${server.port}")
    String port;
    @RequestMapping("/hello")
    @HystrixCommand(fallbackMethod = "helloError")
    public String home(@RequestParam String name) {
        return "hello "+name+",i am from port:" +port;
    }

    public String helloError(String name) {
        return "hello,"+name+",sorry,error!";
    }

}