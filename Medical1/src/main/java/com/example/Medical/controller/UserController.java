package com.example.Medical.controller;

import com.example.Medical.dto.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.example.Medical.service.UserService;

import java.util.List;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping("/registration")
    public String createUser(@RequestBody User user){
    userService.register(user);
    return "Resgistered Sucsessfully";
    }

    @GetMapping("/registration")
    public List<User> displayUser( ){
        return userService.displayUsers();
    }

    @GetMapping("/login")
    public String login(@RequestParam String email, @RequestParam String password){
        return "Logged Successfully";
    }
}
