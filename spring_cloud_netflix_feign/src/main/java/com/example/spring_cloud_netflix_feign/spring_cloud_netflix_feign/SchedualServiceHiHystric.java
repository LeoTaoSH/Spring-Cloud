package com.example.spring_cloud_netflix_feign.spring_cloud_netflix_feign;

import org.springframework.stereotype.Component;

@Component
public class SchedualServiceHiHystric implements SchedualServiceHi {
    @Override
    public String sayHiFromClientOne(String name) {
        return "sorry feign:"+name;
    }
}