package com.akasec.idrive.controller.config.request;

import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;
import org.springframework.util.StreamUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.io.InputStream;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Order(Ordered.LOWEST_PRECEDENCE)
@Component
@WebFilter(filterName = "DasFilter", urlPatterns = "/*")
public class Requesty extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res,
            FilterChain filterChain) throws ServletException, IOException {
        InputStream inputStream = req.getInputStream();
        byte[] rawBody = StreamUtils.copyToByteArray(inputStream);
        String body = new String(rawBody);

        String[] payloads = {
                "$",
                ";",
                "&&",
                "||",
                "`",
                "$",
                ">>",
                ">",
                "<",
                "2>",
                "@",
                "!",
                "${",
                "java",
                "javax",
                "com",
                "org",
                "jboss",
                "tomcat",
                "class",
                "Runtime",
                "ProcessBuilder",
                "Process",
                "getRuntime",
                "exec",
                "getInputStream",
                "getOutputStream",
                "forName",
                "getConstructor",
                "org.apache",
                "System",
                "lang",
                "reflect",
                "Method",
                "getDeclaredMethod",
                "_",
                "springframework",
                "copy",
                "Character",
                "TYPE",
                "char",
                "value",
                "cat",
                "flag",
                "grep",
                "awk",
                "sed",
                "sh",
                "bash",
                "netcat",
                "python",
                "perl",
                "ruby",
                "lua",
                "php",
                "java",
                "base64",
                "id",
                "curl",
                "wget",
                "dig",
                "tac",
                "tail",
                "head",
                "cut",
                "sort",
                "uniq",
                "tr",
                "nslookup",
                "ncat",
        };
        for (String payload : payloads) {
            if (body.contains(payload)) {
                res.sendRedirect("/blocked");
                return;
            }
        }
        filterChain.doFilter(req, res);
    }
}
