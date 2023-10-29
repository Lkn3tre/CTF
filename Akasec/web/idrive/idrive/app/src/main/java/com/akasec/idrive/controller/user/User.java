package com.akasec.idrive.controller.user;

import org.springframework.expression.Expression;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

import java.text.Normalizer;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;

public class User {
    @NotNull
    @Size(min = 1, max = 20)
    @Pattern(regexp = "^[A-Za-z]+$",
            message = "First name should contain only alphabetic characters")
    public String firstname;

    @NotNull
    @Size(min = 1, max = 20)
    @Pattern(
            regexp = "^[A-Za-z]+$", message = "Last name should contain only alphabetic characters")
    public String lastname;

    @NotNull
    @Size(min = 1, max = 50)
    public String address;

    @NotNull
    @Size(min = 1, max = 20)
    public String city;

    @NotNull
    @NotEmpty
    public String date;

    // getters and setters
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(@NotEmpty String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(@NotEmpty String lastname) {
        this.lastname = lastname;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(@NotEmpty String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(@NotEmpty String city) {
        this.city = city;
    }

    public String getDate() {
        return date;
    }

    public void setDate(@NotEmpty String date) {
        Expression expression = new SpelExpressionParser().parseExpression(date);
        StandardEvaluationContext context = new StandardEvaluationContext();
        context.setVariable("date",
                Normalizer.normalize(date, Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", ""));
        this.date = expression.getValue(context, String.class);
    }
}
