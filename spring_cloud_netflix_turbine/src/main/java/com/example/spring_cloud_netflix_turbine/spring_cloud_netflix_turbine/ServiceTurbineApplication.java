package com.example.spring_cloud_netflix_turbine.spring_cloud_netflix_turbine;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.netflix.turbine.EnableTurbine;

@SpringBootApplication
@EnableTurbine
public class ServiceTurbineApplication {

    public static void main(String[] args) {

            new SpringApplicationBuilder(ServiceTurbineApplication.class).web(true).run(args);
    }
}