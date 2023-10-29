package com.akasec.idrive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ErrorController {
    @GetMapping("/blocked")
    ModelAndView blocked() {
        return new ModelAndView("blocked");
    }
}
