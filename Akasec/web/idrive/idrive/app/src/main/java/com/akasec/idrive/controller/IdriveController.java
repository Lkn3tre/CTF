package com.akasec.idrive.controller;

import com.akasec.idrive.controller.user.User;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
@ComponentScan(basePackages = "com.akasec.idrive")
public class IdriveController {
    @GetMapping("/")
    public ModelAndView index() {
        return new ModelAndView("index");
    }

    @GetMapping("/survey")
    public ModelAndView survey() {
        return new ModelAndView("survey");
    }

    @PostMapping("/📝")
    ModelAndView cite(@RequestBody User user) {
        ModelAndView modelAndView = new ModelAndView("receipt");
        modelAndView.addObject("User", user);
        return modelAndView;
    }
}
